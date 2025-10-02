use super::abilities::{
    ability_after_damage_hit, ability_end_of_turn, ability_modify_attack_against,
    ability_modify_attack_being_used, ability_on_switch_in, ability_on_switch_out, Abilities,
};
use super::choice_effects::{
    charge_choice_to_volatile, choice_after_damage_hit, choice_before_move, choice_hazard_clear,
    choice_special_effect, modify_choice,
};
use crate::choices::{
    Boost, Choices, Effect, Heal, MoveTarget, MultiHitMove, Secondary, SideCondition, Status,
    VolatileStatus, MOVES,
};
use crate::instruction::DecrementFutureSightInstruction;
use crate::instruction::{
    ApplyVolatileStatusInstruction, BoostInstruction, ChangeDamageDealtDamageInstruction,
    ChangeDamageDealtMoveCategoryInstruction, ChangeItemInstruction,
    ChangeSideConditionInstruction, ChangeVolatileStatusDurationInstruction, ChangeWeather,
    DecrementRestTurnsInstruction, DecrementWishInstruction, HealInstruction,
    RemoveVolatileStatusInstruction, SetSecondMoveSwitchOutMoveInstruction,
    SetSleepTurnsInstruction, ToggleBatonPassingInstruction,
    ToggleDamageDealtHitSubstituteInstruction,
};
use crate::instruction::{DecrementPPInstruction, SetLastUsedMoveInstruction};

use super::damage_calc::calculate_futuresight_damage;
use super::damage_calc::{calculate_damage, type_effectiveness_modifier, DamageRolls};
use super::items::{
    item_before_move, item_end_of_turn, item_modify_attack_against, item_modify_attack_being_used,
    Items,
};
use super::state::{MoveChoice, PokemonVolatileStatus, Weather};
use crate::choices::{Choice, MoveCategory};
use crate::instruction::{
    ChangeStatusInstruction, DamageInstruction, Instruction, StateInstructions, SwitchInstruction,
};
use crate::state::{
    LastUsedMove, PokemonBoostableStat, PokemonIndex, PokemonMoveIndex, PokemonSideCondition,
    PokemonStatus, PokemonType, Side, SideMovesFirst, SideReference, State,
};
use std::cmp;

pub const BASE_CRIT_CHANCE: f32 = 1.0 / 16.0;
pub const MAX_SLEEP_TURNS: i8 = 4;
pub const HIT_SELF_IN_CONFUSION_CHANCE: f32 = 1.0 / 2.0;
pub const CONSECUTIVE_PROTECT_CHANCE: f32 = 1.0 / 2.0;
pub const SIDE_CONDITION_DURATION: i8 = 5;

fn chance_to_wake_up(turns_asleep: i8) -> f32 {
    if turns_asleep == 0 {
        0.0
    } else {
        1.0 / (1 + MAX_SLEEP_TURNS - turns_asleep) as f32
    }
}

fn set_last_used_move_as_switch(
    side: &mut Side,
    new_pokemon_index: PokemonIndex,
    switching_side_ref: SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    incoming_instructions
        .instruction_list
        .push(Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
            side_ref: switching_side_ref,
            last_used_move: LastUsedMove::Switch(new_pokemon_index),
            previous_last_used_move: side.last_used_move,
        }));
    side.last_used_move = LastUsedMove::Switch(new_pokemon_index);
}

fn set_last_used_move_as_move(
    side: &mut Side,
    used_move: PokemonMoveIndex,
    switching_side_ref: SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    if side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::FLINCH)
    {
        return;
    }
    match side.last_used_move {
        LastUsedMove::Move(last_used_move) => {
            if last_used_move == used_move {
                return;
            }
        }
        _ => {}
    }
    incoming_instructions
        .instruction_list
        .push(Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
            side_ref: switching_side_ref,
            last_used_move: LastUsedMove::Move(used_move),
            previous_last_used_move: side.last_used_move,
        }));
    side.last_used_move = LastUsedMove::Move(used_move);
}

fn generate_instructions_from_switch(
    state: &mut State,
    new_pokemon_index: PokemonIndex,
    switching_side_ref: SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    let should_last_used_move = state.use_last_used_move;
    state.apply_instructions(&incoming_instructions.instruction_list);

    let (side, opposite_side) = state.get_both_sides(&switching_side_ref);
    if side.force_switch {
        side.force_switch = false;
        match switching_side_ref {
            SideReference::SideOne => {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::ToggleSideOneForceSwitch);
            }
            SideReference::SideTwo => {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::ToggleSideTwoForceSwitch);
            }
        }
    }

    let mut baton_passing = false;
    if side.baton_passing {
        baton_passing = true;
        side.baton_passing = false;
        match switching_side_ref {
            SideReference::SideOne => {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::ToggleBatonPassing(
                        ToggleBatonPassingInstruction {
                            side_ref: SideReference::SideOne,
                        },
                    ));
            }
            SideReference::SideTwo => {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::ToggleBatonPassing(
                        ToggleBatonPassingInstruction {
                            side_ref: SideReference::SideTwo,
                        },
                    ));
            }
        }
    }

    if opposite_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::PARTIALLYTRAPPED)
    {
        incoming_instructions
            .instruction_list
            .push(Instruction::RemoveVolatileStatus(
                RemoveVolatileStatusInstruction {
                    side_ref: switching_side_ref.get_other_side(),
                    volatile_status: PokemonVolatileStatus::PARTIALLYTRAPPED,
                },
            ));
        opposite_side
            .volatile_statuses
            .remove(&PokemonVolatileStatus::PARTIALLYTRAPPED);
    }

    state.re_enable_disabled_moves(
        &switching_side_ref,
        &mut incoming_instructions.instruction_list,
    );
    state.remove_volatile_statuses_on_switch(
        &switching_side_ref,
        &mut incoming_instructions.instruction_list,
        baton_passing,
    );
    state.reset_toxic_count(
        &switching_side_ref,
        &mut incoming_instructions.instruction_list,
    );
    if !baton_passing {
        state.reset_boosts(
            &switching_side_ref,
            &mut incoming_instructions.instruction_list,
        );
    }

    ability_on_switch_out(state, &switching_side_ref, incoming_instructions);

    let switch_instruction = Instruction::Switch(SwitchInstruction {
        side_ref: switching_side_ref,
        previous_index: state.get_side(&switching_side_ref).active_index,
        next_index: new_pokemon_index,
    });

    let side = state.get_side(&switching_side_ref);
    side.active_index = new_pokemon_index;
    incoming_instructions
        .instruction_list
        .push(switch_instruction);

    if should_last_used_move {
        set_last_used_move_as_switch(
            side,
            new_pokemon_index,
            switching_side_ref,
            incoming_instructions,
        );
    }

    let side = state.get_side(&switching_side_ref);
    let switched_in_pkmn = side.get_active_immutable();
    if side.side_conditions.spikes > 0 && switched_in_pkmn.is_grounded() {
        let dmg_amount = cmp::min(
            switched_in_pkmn.maxhp * side.side_conditions.spikes as i16 / 8,
            switched_in_pkmn.hp,
        );
        let spikes_dmg_instruction = Instruction::Damage(DamageInstruction {
            side_ref: switching_side_ref,
            damage_amount: dmg_amount,
        });
        side.get_active().hp -= dmg_amount;
        incoming_instructions
            .instruction_list
            .push(spikes_dmg_instruction);
    }

    ability_on_switch_in(state, &switching_side_ref, incoming_instructions);

    state.reverse_instructions(&incoming_instructions.instruction_list);
}

fn generate_instructions_from_increment_side_condition(
    state: &mut State,
    side_condition: &SideCondition,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    let affected_side_ref;
    match side_condition.target {
        MoveTarget::Opponent => affected_side_ref = attacking_side_reference.get_other_side(),
        MoveTarget::User => affected_side_ref = *attacking_side_reference,
    }

    let max_layers = match side_condition.condition {
        PokemonSideCondition::Spikes => 3,
        _ => 1,
    };

    let affected_side = state.get_side(&affected_side_ref);
    if affected_side.get_side_condition(side_condition.condition) < max_layers {
        let ins = Instruction::ChangeSideCondition(ChangeSideConditionInstruction {
            side_ref: affected_side_ref,
            side_condition: side_condition.condition,
            amount: 1,
        });
        affected_side.update_side_condition(side_condition.condition, 1);
        incoming_instructions.instruction_list.push(ins);
    }
}

fn generate_instructions_from_duration_side_conditions(
    state: &mut State,
    side_condition: &SideCondition,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
    duration: i8,
) {
    let affected_side_ref = match side_condition.target {
        MoveTarget::Opponent => attacking_side_reference.get_other_side(),
        MoveTarget::User => *attacking_side_reference,
    };
    let affected_side = state.get_side(&affected_side_ref);
    if affected_side.get_side_condition(side_condition.condition) == 0 {
        let ins = Instruction::ChangeSideCondition(ChangeSideConditionInstruction {
            side_ref: affected_side_ref,
            side_condition: side_condition.condition,
            amount: duration,
        });
        affected_side.update_side_condition(side_condition.condition, duration);
        incoming_instructions.instruction_list.push(ins);
    }
}

fn generate_instructions_from_side_conditions(
    state: &mut State,
    side_condition: &SideCondition,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    match side_condition.condition {
        PokemonSideCondition::LightScreen | PokemonSideCondition::Reflect => {
            generate_instructions_from_duration_side_conditions(
                state,
                side_condition,
                attacking_side_reference,
                incoming_instructions,
                SIDE_CONDITION_DURATION,
            );
        }
        _ => generate_instructions_from_increment_side_condition(
            state,
            side_condition,
            attacking_side_reference,
            incoming_instructions,
        ),
    }
}

fn get_instructions_from_volatile_statuses(
    state: &mut State,
    attacker_choice: &Choice,
    volatile_status: &VolatileStatus,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    let target_side: SideReference;
    match volatile_status.target {
        MoveTarget::Opponent => target_side = attacking_side_reference.get_other_side(),
        MoveTarget::User => target_side = *attacking_side_reference,
    }

    if volatile_status.volatile_status == PokemonVolatileStatus::YAWN
        && immune_to_status(
            state,
            &MoveTarget::Opponent,
            &target_side,
            &PokemonStatus::SLEEP,
        )
    {
        return;
    }
    let side = state.get_side(&target_side);
    let affected_pkmn = side.get_active_immutable();
    if affected_pkmn.volatile_status_can_be_applied(
        &volatile_status.volatile_status,
        &side.volatile_statuses,
        attacker_choice.first_move,
    ) {
        let ins = Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
            side_ref: target_side,
            volatile_status: volatile_status.volatile_status,
        });

        side.volatile_statuses
            .insert(volatile_status.volatile_status);
        incoming_instructions.instruction_list.push(ins);
    }
}

pub fn add_remove_status_instructions(
    incoming_instructions: &mut StateInstructions,
    pokemon_index: PokemonIndex,
    side_reference: SideReference,
    side: &mut Side,
) {
    /*
    Single place to check for status removals, add the necessary instructions, and update the pokemon's status

    This is necessary because of some side effects to removing statuses
    i.e. a pre-mature wake-up from rest must set rest_turns to 0
    */
    let pkmn = &mut side.pokemon[pokemon_index];
    incoming_instructions
        .instruction_list
        .push(Instruction::ChangeStatus(ChangeStatusInstruction {
            side_ref: side_reference,
            pokemon_index: pokemon_index,
            old_status: pkmn.status,
            new_status: PokemonStatus::NONE,
        }));
    match pkmn.status {
        PokemonStatus::SLEEP => {
            if pkmn.rest_turns > 0 {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::SetRestTurns(SetSleepTurnsInstruction {
                        side_ref: side_reference,
                        pokemon_index,
                        new_turns: 0,
                        previous_turns: pkmn.rest_turns,
                    }));
                pkmn.rest_turns = 0;
            } else if pkmn.sleep_turns > 0 {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                        side_ref: side_reference,
                        pokemon_index,
                        new_turns: 0,
                        previous_turns: pkmn.sleep_turns,
                    }));
                pkmn.sleep_turns = 0;
            }
        }
        PokemonStatus::TOXIC => {
            if side.side_conditions.toxic_count != 0 {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::ChangeSideCondition(
                        ChangeSideConditionInstruction {
                            side_ref: side_reference,
                            side_condition: PokemonSideCondition::ToxicCount,
                            amount: -1 * side.side_conditions.toxic_count,
                        },
                    ));
                side.side_conditions.toxic_count = 0;
            }
        }
        _ => {}
    }
    pkmn.status = PokemonStatus::NONE;
}

pub fn immune_to_status(
    state: &State,
    status_target: &MoveTarget,
    target_side_ref: &SideReference,
    status: &PokemonStatus,
) -> bool {
    let target_side = state.get_side_immutable(target_side_ref);
    let target_pkmn = target_side.get_active_immutable();

    if target_pkmn.status != PokemonStatus::NONE || target_pkmn.hp <= 0 {
        true
    } else if (target_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::SUBSTITUTE)
        || target_side.side_conditions.safeguard > 0)
        && status_target == &MoveTarget::Opponent
    // substitute/safeguard don't block if the target is yourself (eg. rest)
    {
        true
    } else {
        // Specific status immunity
        match status {
            PokemonStatus::BURN => {
                target_pkmn.has_type(&PokemonType::FIRE)
                    || target_pkmn.ability == Abilities::WATERVEIL
            }
            PokemonStatus::FREEZE => {
                target_pkmn.has_type(&PokemonType::ICE)
                    || target_pkmn.ability == Abilities::MAGMAARMOR
                    || state.weather_is_active(&Weather::SUN)
            }
            PokemonStatus::SLEEP => {
                [Abilities::INSOMNIA, Abilities::VITALSPIRIT].contains(&target_pkmn.ability)
                    || (status_target == &MoveTarget::Opponent
                        && target_side.has_alive_non_rested_sleeping_pkmn())
                // sleep clause
            }

            PokemonStatus::PARALYZE => target_pkmn.ability == Abilities::LIMBER,

            PokemonStatus::POISON | PokemonStatus::TOXIC => {
                (target_pkmn.has_type(&PokemonType::POISON)
                    || target_pkmn.has_type(&PokemonType::STEEL))
                    || target_pkmn.ability == Abilities::IMMUNITY
            }
            _ => false,
        }
    }
}

fn get_instructions_from_status_effects(
    state: &mut State,
    status: &Status,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
    hit_sub: bool,
) {
    let target_side_ref: SideReference;
    match status.target {
        MoveTarget::Opponent => target_side_ref = attacking_side_reference.get_other_side(),
        MoveTarget::User => target_side_ref = *attacking_side_reference,
    }

    if hit_sub || immune_to_status(state, &status.target, &target_side_ref, &status.status) {
        return;
    }

    let target_side = state.get_side(&target_side_ref);
    let target_side_active = target_side.active_index;
    let target_pkmn = target_side.get_active();

    let instruction = if target_pkmn.item == Items::LUMBERRY {
        target_pkmn.item = Items::NONE;
        Instruction::ChangeItem(ChangeItemInstruction {
            side_ref: target_side_ref,
            current_item: Items::LUMBERRY,
            new_item: Items::NONE,
        })
    } else if target_pkmn.item == Items::CHESTOBERRY && status.status == PokemonStatus::SLEEP {
        target_pkmn.item = Items::NONE;
        Instruction::ChangeItem(ChangeItemInstruction {
            side_ref: target_side_ref,
            current_item: Items::CHESTOBERRY,
            new_item: Items::NONE,
        })
    } else {
        let old_status = target_pkmn.status;
        target_pkmn.status = status.status;
        Instruction::ChangeStatus(ChangeStatusInstruction {
            side_ref: target_side_ref,
            pokemon_index: target_side_active,
            old_status,
            new_status: status.status,
        })
    };
    incoming_instructions.instruction_list.push(instruction);
}

pub fn get_boost_amount(side: &Side, boost: &PokemonBoostableStat, amount: i8) -> i8 {
    /*
    returns that amount that can actually be applied from the attempted boost amount
        e.g. using swordsdance at +5 attack would result in a +1 boost instead of +2
    */
    let current_boost = side.get_boost_from_boost_enum(boost);

    if amount > 0 {
        return cmp::min(6 - current_boost, amount);
    } else if amount < 0 {
        return cmp::max(-6 - current_boost, amount);
    }
    0
}

pub fn apply_boost_instruction(
    target_side: &mut Side,
    stat: &PokemonBoostableStat,
    boost: &i8,
    attacking_side_ref: &SideReference,
    target_side_ref: &SideReference,
    instructions: &mut StateInstructions,
) -> bool {
    let mut boost_was_applied = false;
    let target_pkmn = target_side.get_active_immutable();

    if boost != &0
        && !(target_side_ref != attacking_side_ref
            && target_pkmn
                .immune_to_stats_lowered_by_opponent(&stat, &target_side.volatile_statuses))
        && target_pkmn.hp != 0
    {
        let mut boost_amount = *boost;
        boost_amount = get_boost_amount(target_side, &stat, boost_amount);
        if boost_amount != 0 {
            boost_was_applied = true;
            match stat {
                PokemonBoostableStat::Attack => target_side.attack_boost += boost_amount,
                PokemonBoostableStat::Defense => target_side.defense_boost += boost_amount,
                PokemonBoostableStat::SpecialAttack => {
                    target_side.special_attack_boost += boost_amount
                }
                PokemonBoostableStat::SpecialDefense => {
                    target_side.special_defense_boost += boost_amount
                }
                PokemonBoostableStat::Speed => target_side.speed_boost += boost_amount,
                PokemonBoostableStat::Evasion => target_side.accuracy_boost += boost_amount,
                PokemonBoostableStat::Accuracy => target_side.evasion_boost += boost_amount,
            }
            instructions
                .instruction_list
                .push(Instruction::Boost(BoostInstruction {
                    side_ref: *target_side_ref,
                    stat: *stat,
                    amount: boost_amount,
                }));
        }
    }
    boost_was_applied
}

fn get_instructions_from_boosts(
    state: &mut State,
    boosts: &Boost,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    let target_side_ref: SideReference;
    match boosts.target {
        MoveTarget::Opponent => target_side_ref = attacking_side_reference.get_other_side(),
        MoveTarget::User => target_side_ref = *attacking_side_reference,
    }
    let boostable_stats = boosts.boosts.get_as_pokemon_boostable();
    for (pkmn_boostable_stat, boost) in boostable_stats.iter().filter(|(_, b)| b != &0) {
        let side = state.get_side(&target_side_ref);
        apply_boost_instruction(
            side,
            pkmn_boostable_stat,
            boost,
            attacking_side_reference,
            &target_side_ref,
            incoming_instructions,
        );
    }
}

fn compare_health_with_damage_multiples(max_damage: i16, health: i16) -> (i16, i16) {
    let max_damage_f32 = max_damage as f32;
    let health_f32 = health as f32;

    let mut total_less_than = 0;
    let mut num_less_than = 0;
    let mut num_greater_than = 0;
    let increment = max_damage as f32 * 0.01;
    let mut damage = max_damage_f32 * 0.85;
    for _ in 0..16 {
        if damage < health_f32 {
            total_less_than += damage as i16;
            num_less_than += 1;
        } else if damage > health_f32 {
            num_greater_than += 1;
        }
        damage += increment;
    }

    (total_less_than / num_less_than, num_greater_than)
}

fn get_instructions_from_secondaries(
    state: &mut State,
    attacker_choice: &Choice,
    secondaries: &Vec<Secondary>,
    side_reference: &SideReference,
    incoming_instructions: StateInstructions,
    hit_sub: bool,
) -> Vec<StateInstructions> {
    let mut return_instruction_list = Vec::with_capacity(4);
    return_instruction_list.push(incoming_instructions);

    for secondary in secondaries {
        if secondary.target == MoveTarget::Opponent && hit_sub {
            continue;
        }
        let secondary_percent_hit = (secondary.chance / 100.0).min(1.0);

        let mut i = 0;
        while i < return_instruction_list.len() {
            let mut secondary_hit_instructions = return_instruction_list.remove(i);

            if secondary_percent_hit < 1.0 {
                let mut secondary_miss_instructions = secondary_hit_instructions.clone();
                secondary_miss_instructions.update_percentage(1.0 - secondary_percent_hit);
                return_instruction_list.insert(i, secondary_miss_instructions);
                i += 1;
            }

            if secondary_percent_hit > 0.0 {
                secondary_hit_instructions.update_percentage(secondary_percent_hit);

                state.apply_instructions(&secondary_hit_instructions.instruction_list);
                match &secondary.effect {
                    Effect::VolatileStatus(volatile_status) => {
                        get_instructions_from_volatile_statuses(
                            state,
                            attacker_choice,
                            &VolatileStatus {
                                target: secondary.target.clone(),
                                volatile_status: volatile_status.clone(),
                            },
                            side_reference,
                            &mut secondary_hit_instructions,
                        );
                    }
                    Effect::Boost(boost) => {
                        get_instructions_from_boosts(
                            state,
                            &Boost {
                                target: secondary.target.clone(),
                                boosts: boost.clone(),
                            },
                            side_reference,
                            &mut secondary_hit_instructions,
                        );
                    }
                    Effect::Status(status) => {
                        get_instructions_from_status_effects(
                            state,
                            &Status {
                                target: secondary.target.clone(),
                                status: status.clone(),
                            },
                            side_reference,
                            &mut secondary_hit_instructions,
                            hit_sub,
                        );
                    }
                    Effect::Heal(heal_amount) => {
                        get_instructions_from_heal(
                            state,
                            &Heal {
                                target: secondary.target.clone(),
                                amount: *heal_amount,
                            },
                            side_reference,
                            &mut secondary_hit_instructions,
                        );
                    }
                    Effect::RemoveItem => {
                        let secondary_target_side_ref: SideReference;
                        match secondary.target {
                            MoveTarget::Opponent => {
                                secondary_target_side_ref = side_reference.get_other_side();
                            }
                            MoveTarget::User => {
                                secondary_target_side_ref = *side_reference;
                            }
                        }
                        let target_pkmn = state.get_side(&secondary_target_side_ref).get_active();
                        secondary_hit_instructions
                            .instruction_list
                            .push(Instruction::ChangeItem(ChangeItemInstruction {
                                side_ref: secondary_target_side_ref,
                                current_item: target_pkmn.item.clone(),
                                new_item: Items::NONE,
                            }));
                        target_pkmn.item = Items::NONE;
                    }
                }
                state.reverse_instructions(&secondary_hit_instructions.instruction_list);
                return_instruction_list.insert(i, secondary_hit_instructions);
                i += 1; // Increment i only if we didn't remove an element
            }
        }
    }

    return_instruction_list
}

fn get_instructions_from_heal(
    state: &mut State,
    heal: &Heal,
    attacking_side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    let target_side_ref: SideReference;
    match heal.target {
        MoveTarget::Opponent => target_side_ref = attacking_side_reference.get_other_side(),
        MoveTarget::User => target_side_ref = *attacking_side_reference,
    }

    let target_pkmn = state.get_side(&target_side_ref).get_active();

    let mut health_recovered = (heal.amount * target_pkmn.maxhp as f32) as i16;
    let final_health = target_pkmn.hp + health_recovered;
    if final_health > target_pkmn.maxhp {
        health_recovered -= final_health - target_pkmn.maxhp;
    } else if final_health < 0 {
        health_recovered -= final_health;
    }

    if health_recovered != 0 {
        let ins = Instruction::Heal(HealInstruction {
            side_ref: target_side_ref,
            heal_amount: health_recovered,
        });
        target_pkmn.hp += health_recovered;
        incoming_instructions.instruction_list.push(ins);
    }
}

fn check_move_hit_or_miss(
    state: &mut State,
    choice: &Choice,
    attacking_side_ref: &SideReference,
    damage: Option<(i16, i16)>,
    incoming_instructions: &mut StateInstructions,
    frozen_instructions: &mut Vec<StateInstructions>,
) {
    /*
    Checks whether a move can miss

    If the move can miss - adds it to `frozen_instructions`, signifying that the rest of the
    half-turn will not run.

    Otherwise, update the incoming instructions' percent_hit to reflect the chance of the move hitting
    */
    let attacking_side = state.get_side_immutable(attacking_side_ref);
    let attacking_pokemon = attacking_side.get_active_immutable();

    let mut percent_hit = (choice.accuracy / 100.0).min(1.0);
    if Some((0, 0)) == damage {
        percent_hit = 0.0;
    }

    if percent_hit < 1.0 {
        let mut move_missed_instruction = incoming_instructions.clone();
        move_missed_instruction.update_percentage(1.0 - percent_hit);
        if let Some(crash_fraction) = choice.crash {
            let crash_amount = (attacking_pokemon.maxhp as f32 * crash_fraction) as i16;
            let crash_instruction = Instruction::Damage(DamageInstruction {
                side_ref: *attacking_side_ref,
                damage_amount: cmp::min(crash_amount, attacking_pokemon.hp),
            });

            move_missed_instruction
                .instruction_list
                .push(crash_instruction);
        }

        frozen_instructions.push(move_missed_instruction);
    }
    incoming_instructions.update_percentage(percent_hit);
}

fn get_instructions_from_drag(
    state: &mut State,
    attacking_side_reference: &SideReference,
    incoming_instructions: StateInstructions,
    frozen_instructions: &mut Vec<StateInstructions>,
) {
    let defending_side = state.get_side(&attacking_side_reference.get_other_side());
    if defending_side.get_active_immutable().hp == 0 {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        frozen_instructions.push(incoming_instructions);
        return;
    }

    let defending_side_alive_reserve_indices = defending_side.get_alive_pkmn_indices();

    state.reverse_instructions(&incoming_instructions.instruction_list);

    let num_alive_reserve = defending_side_alive_reserve_indices.len();
    if num_alive_reserve == 0 {
        frozen_instructions.push(incoming_instructions);
        return;
    }

    for pkmn_id in defending_side_alive_reserve_indices {
        let mut cloned_instructions = incoming_instructions.clone();
        generate_instructions_from_switch(
            state,
            pkmn_id,
            attacking_side_reference.get_other_side(),
            &mut cloned_instructions,
        );
        cloned_instructions.update_percentage(1.0 / num_alive_reserve as f32);
        frozen_instructions.push(cloned_instructions);
    }
}

fn reset_damage_dealt(
    side: &Side,
    side_reference: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    // This creates instructions but does not modify the side
    // because this function is called before the state applies the instructions

    if side.damage_dealt.damage != 0 {
        incoming_instructions
            .instruction_list
            .push(Instruction::ChangeDamageDealtDamage(
                ChangeDamageDealtDamageInstruction {
                    side_ref: *side_reference,
                    damage_change: 0 - side.damage_dealt.damage,
                },
            ));
    }
    if side.damage_dealt.move_category != MoveCategory::Physical {
        incoming_instructions
            .instruction_list
            .push(Instruction::ChangeDamageDealtMoveCatagory(
                ChangeDamageDealtMoveCategoryInstruction {
                    side_ref: *side_reference,
                    move_category: MoveCategory::Physical,
                    previous_move_category: side.damage_dealt.move_category,
                },
            ));
    }
    if side.damage_dealt.hit_substitute {
        incoming_instructions
            .instruction_list
            .push(Instruction::ToggleDamageDealtHitSubstitute(
                ToggleDamageDealtHitSubstituteInstruction {
                    side_ref: *side_reference,
                },
            ));
    }
}

fn set_damage_dealt(
    attacking_side: &mut Side,
    attacking_side_ref: &SideReference,
    damage_dealt: i16,
    choice: &Choice,
    hit_substitute: bool,
    incoming_instructions: &mut StateInstructions,
) {
    if attacking_side.damage_dealt.damage != damage_dealt {
        incoming_instructions
            .instruction_list
            .push(Instruction::ChangeDamageDealtDamage(
                ChangeDamageDealtDamageInstruction {
                    side_ref: *attacking_side_ref,
                    damage_change: damage_dealt - attacking_side.damage_dealt.damage,
                },
            ));
        attacking_side.damage_dealt.damage = damage_dealt;
    }

    if attacking_side.damage_dealt.move_category != choice.category {
        incoming_instructions
            .instruction_list
            .push(Instruction::ChangeDamageDealtMoveCatagory(
                ChangeDamageDealtMoveCategoryInstruction {
                    side_ref: *attacking_side_ref,
                    move_category: choice.category,
                    previous_move_category: attacking_side.damage_dealt.move_category,
                },
            ));
        attacking_side.damage_dealt.move_category = choice.category;
    }

    if attacking_side.damage_dealt.hit_substitute != hit_substitute {
        incoming_instructions
            .instruction_list
            .push(Instruction::ToggleDamageDealtHitSubstitute(
                ToggleDamageDealtHitSubstituteInstruction {
                    side_ref: *attacking_side_ref,
                },
            ));
        attacking_side.damage_dealt.hit_substitute = hit_substitute;
    }
}

fn generate_instructions_from_damage(
    mut state: &mut State,
    choice: &mut Choice,
    calculated_damage: i16,
    attacking_side_ref: &SideReference,
    mut incoming_instructions: &mut StateInstructions,
) -> bool {
    /*
    TODO:
        - arbitrary other after_move as well from the old engine (triggers on hit OR miss)
            - dig/dive/bounce/fly volatilestatus
    */
    let mut hit_sub = false;
    let attacking_side = state.get_side(attacking_side_ref);
    let attacking_pokemon = attacking_side.get_active();

    if calculated_damage <= 0 {
        if let Some(crash_fraction) = choice.crash {
            let crash_amount = (attacking_pokemon.maxhp as f32 * crash_fraction) as i16;
            let damage_taken = cmp::min(crash_amount, attacking_pokemon.hp);
            let crash_instruction = Instruction::Damage(DamageInstruction {
                side_ref: *attacking_side_ref,
                damage_amount: damage_taken,
            });
            attacking_pokemon.hp -= damage_taken;
            incoming_instructions
                .instruction_list
                .push(crash_instruction);
        }
        return hit_sub;
    }

    let percent_hit = (choice.accuracy / 100.0).min(1.0);

    if percent_hit > 0.0 {
        let should_use_damage_dealt = state.use_damage_dealt;
        let (attacking_side, defending_side) = state.get_both_sides(attacking_side_ref);
        let mut damage_dealt;
        if defending_side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::SUBSTITUTE)
        {
            damage_dealt = cmp::min(calculated_damage, defending_side.substitute_health);
            let substitute_damage_dealt = cmp::min(calculated_damage, damage_dealt);
            let substitute_instruction = Instruction::DamageSubstitute(DamageInstruction {
                side_ref: attacking_side_ref.get_other_side(),
                damage_amount: substitute_damage_dealt,
            });
            defending_side.substitute_health -= substitute_damage_dealt;
            incoming_instructions
                .instruction_list
                .push(substitute_instruction);

            if should_use_damage_dealt {
                set_damage_dealt(
                    attacking_side,
                    attacking_side_ref,
                    damage_dealt,
                    choice,
                    true,
                    &mut incoming_instructions,
                );
            }

            if defending_side
                .volatile_statuses
                .contains(&PokemonVolatileStatus::SUBSTITUTE)
                && defending_side.substitute_health == 0
            {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::RemoveVolatileStatus(
                        RemoveVolatileStatusInstruction {
                            side_ref: attacking_side_ref.get_other_side(),
                            volatile_status: PokemonVolatileStatus::SUBSTITUTE,
                        },
                    ));
                defending_side
                    .volatile_statuses
                    .remove(&PokemonVolatileStatus::SUBSTITUTE);
            }

            hit_sub = true;
        } else {
            let has_endure = defending_side
                .volatile_statuses
                .contains(&PokemonVolatileStatus::ENDURE);
            let attacking_pokemon = attacking_side.get_active();
            let defending_pokemon = defending_side.get_active();
            let mut knocked_out = false;
            damage_dealt = cmp::min(calculated_damage, defending_pokemon.hp);
            if damage_dealt != 0 {
                if has_endure
                    || ((defending_pokemon.ability == Abilities::STURDY
                        || defending_pokemon.item == Items::FOCUSSASH)
                        && defending_pokemon.maxhp == defending_pokemon.hp)
                {
                    damage_dealt -= 1;
                }

                if damage_dealt >= defending_pokemon.hp {
                    knocked_out = true;
                }

                let damage_instruction = Instruction::Damage(DamageInstruction {
                    side_ref: attacking_side_ref.get_other_side(),
                    damage_amount: damage_dealt,
                });
                defending_pokemon.hp -= damage_dealt;
                incoming_instructions
                    .instruction_list
                    .push(damage_instruction);

                if knocked_out
                    && defending_side
                        .volatile_statuses
                        .contains(&PokemonVolatileStatus::DESTINYBOND)
                {
                    let damage_instruction = Instruction::Damage(DamageInstruction {
                        side_ref: *attacking_side_ref,
                        damage_amount: attacking_pokemon.hp,
                    });
                    attacking_pokemon.hp = 0;
                    incoming_instructions
                        .instruction_list
                        .push(damage_instruction);
                }

                if should_use_damage_dealt {
                    set_damage_dealt(
                        attacking_side,
                        attacking_side_ref,
                        damage_dealt,
                        choice,
                        false,
                        &mut incoming_instructions,
                    );
                }

                ability_after_damage_hit(
                    &mut state,
                    choice,
                    attacking_side_ref,
                    damage_dealt,
                    &mut incoming_instructions,
                );
            }
        }

        let attacking_pokemon = state.get_side(attacking_side_ref).get_active();
        if let Some(drain_fraction) = choice.drain {
            let drain_amount = (damage_dealt as f32 * drain_fraction) as i16;
            let heal_amount =
                cmp::min(drain_amount, attacking_pokemon.maxhp - attacking_pokemon.hp);
            if heal_amount != 0 {
                let drain_instruction = Instruction::Heal(HealInstruction {
                    side_ref: *attacking_side_ref,
                    heal_amount: heal_amount,
                });
                attacking_pokemon.hp += heal_amount;
                incoming_instructions
                    .instruction_list
                    .push(drain_instruction);
            }
        }

        let attacking_pokemon = state.get_side(attacking_side_ref).get_active();
        if let Some(recoil_fraction) = choice.recoil {
            let recoil_amount = (damage_dealt as f32 * recoil_fraction) as i16;
            let damage_amount = cmp::min(recoil_amount, attacking_pokemon.hp);
            let recoil_instruction = Instruction::Damage(DamageInstruction {
                side_ref: *attacking_side_ref,
                damage_amount: damage_amount,
            });
            attacking_pokemon.hp -= damage_amount;
            incoming_instructions
                .instruction_list
                .push(recoil_instruction);
        }
        choice_after_damage_hit(
            &mut state,
            &choice,
            attacking_side_ref,
            &mut incoming_instructions,
            hit_sub,
        );
    }
    hit_sub
}

fn move_has_no_effect(state: &State, choice: &Choice, attacking_side_ref: &SideReference) -> bool {
    let (_attacking_side, defending_side) = state.get_both_sides_immutable(attacking_side_ref);
    let defender = defending_side.get_active_immutable();

    if choice.move_type == PokemonType::ELECTRIC
        && choice.target == MoveTarget::Opponent
        && defender.has_type(&PokemonType::GROUND)
    {
        return true;
    } else if choice.move_id == Choices::ENCORE {
        return match state
            .get_side_immutable(&attacking_side_ref.get_other_side())
            .last_used_move
        {
            LastUsedMove::None => true,
            LastUsedMove::Move(_) => false,
            LastUsedMove::Switch(_) => true,
        };
    }
    false
}

fn cannot_use_move(state: &State, choice: &Choice, attacking_side_ref: &SideReference) -> bool {
    let (attacking_side, defending_side) = state.get_both_sides_immutable(attacking_side_ref);
    if defending_side.get_active_immutable().hp == 0 {
        return true;
    }

    // If you were taunted, you can't use a Physical/Special move
    if attacking_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::TAUNT)
        && matches!(choice.category, MoveCategory::Status)
    {
        return true;
    } else if attacking_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::FLINCH)
    {
        return true;
    }
    false
}

fn before_move(
    state: &mut State,
    choice: &mut Choice,
    defender_choice: &Choice,
    attacking_side: &SideReference,
    incoming_instructions: &mut StateInstructions,
) {
    item_before_move(state, choice, attacking_side, incoming_instructions);
    choice_before_move(state, choice, attacking_side, incoming_instructions);

    modify_choice(state, choice, defender_choice, attacking_side);

    ability_modify_attack_being_used(state, choice, defender_choice, attacking_side);
    ability_modify_attack_against(state, choice, defender_choice, attacking_side);

    item_modify_attack_being_used(state, choice, attacking_side);
    item_modify_attack_against(state, choice, attacking_side);

    /*
        TODO: this needs to be here because from_drag is called after the substitute volatilestatus
            has already been removed
    */
    let (attacking_side, defending_side) = state.get_both_sides_immutable(attacking_side);
    if defending_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::SUBSTITUTE)
        && choice.category != MoveCategory::Status
    {
        choice.flags.drag = false;
    }

    // Update Choice for `charge` moves
    if choice.flags.charge {
        let charge_volatile_status = charge_choice_to_volatile(&choice.move_id);
        if !attacking_side
            .volatile_statuses
            .contains(&charge_volatile_status)
        {
            choice.remove_all_effects();
            choice.volatile_status = Some(VolatileStatus {
                target: MoveTarget::User,
                volatile_status: charge_volatile_status,
            });
        }
    }

    // modify choice if defender has protect active
    if defending_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::PROTECT)
        && choice.flags.protect
    {
        choice.remove_effects_for_protect();
        if choice.crash.is_some() {
            choice.accuracy = 0.0;
        }
    }
}

fn generate_instructions_from_existing_status_conditions(
    state: &mut State,
    attacking_side_ref: &SideReference,
    attacker_choice: &Choice,
    incoming_instructions: &mut StateInstructions,
    final_instructions: &mut Vec<StateInstructions>,
) {
    let (attacking_side, _defending_side) = state.get_both_sides(attacking_side_ref);
    let current_active_index = attacking_side.active_index;
    let attacker_active = attacking_side.get_active();
    match attacker_active.status {
        PokemonStatus::PARALYZE => {
            // Fully-Paralyzed Branch
            let mut fully_paralyzed_instruction = incoming_instructions.clone();
            fully_paralyzed_instruction.update_percentage(0.25);
            final_instructions.push(fully_paralyzed_instruction);

            // Non-Paralyzed Branch
            incoming_instructions.update_percentage(0.75);
        }
        PokemonStatus::FREEZE => {
            let mut still_frozen_instruction = incoming_instructions.clone();
            still_frozen_instruction.update_percentage(0.80);
            final_instructions.push(still_frozen_instruction);

            incoming_instructions.update_percentage(0.20);
            attacker_active.status = PokemonStatus::NONE;
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeStatus(ChangeStatusInstruction {
                    side_ref: attacking_side_ref.clone(),
                    pokemon_index: current_active_index,
                    old_status: PokemonStatus::FREEZE,
                    new_status: PokemonStatus::NONE,
                }));
        }
        PokemonStatus::SLEEP => {
            match attacker_active.rest_turns {
                // Pokemon is not asleep because of Rest.
                0 => {
                    let current_sleep_turns = attacker_active.sleep_turns;
                    let chance_to_wake = chance_to_wake_up(current_sleep_turns);
                    if chance_to_wake == 1.0 {
                        attacker_active.status = PokemonStatus::NONE;
                        attacker_active.sleep_turns = 0;
                        incoming_instructions
                            .instruction_list
                            .push(Instruction::ChangeStatus(ChangeStatusInstruction {
                                side_ref: *attacking_side_ref,
                                pokemon_index: current_active_index,
                                old_status: PokemonStatus::SLEEP,
                                new_status: PokemonStatus::NONE,
                            }));
                        incoming_instructions
                            .instruction_list
                            .push(Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                side_ref: *attacking_side_ref,
                                pokemon_index: current_active_index,
                                new_turns: 0,
                                previous_turns: current_sleep_turns,
                            }));
                    } else if chance_to_wake == 0.0 {
                        if attacker_choice.move_id == Choices::SLEEPTALK {
                            // if we are using sleeptalk we want to continue using this move
                            incoming_instructions.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: current_sleep_turns + 1,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                        } else {
                            let mut still_asleep_instruction = incoming_instructions.clone();
                            still_asleep_instruction.update_percentage(1.0);
                            still_asleep_instruction.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: current_sleep_turns + 1,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                            final_instructions.push(still_asleep_instruction);
                            incoming_instructions.update_percentage(0.0);
                        }
                    } else {
                        // This code deals with the situation where there is a chance to wake up
                        // as well as a chance to stay asleep.
                        // This logic will branch the state and one branch will represent where
                        // nothing happens and the other will represent where something happens
                        // Normally "nothing happens" means you stay asleep and "something happens"
                        // means you wake up. If the move is sleeptalk these are reversed.
                        let do_nothing_percentage;
                        let mut do_nothing_instructions = incoming_instructions.clone();
                        if attacker_choice.move_id == Choices::SLEEPTALK {
                            do_nothing_percentage = chance_to_wake;
                            do_nothing_instructions.instruction_list.push(
                                Instruction::ChangeStatus(ChangeStatusInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    old_status: PokemonStatus::SLEEP,
                                    new_status: PokemonStatus::NONE,
                                }),
                            );
                            do_nothing_instructions.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: 0,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                            incoming_instructions.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: current_sleep_turns + 1,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                            attacker_active.sleep_turns += 1;
                        } else {
                            do_nothing_percentage = 1.0 - chance_to_wake;
                            do_nothing_instructions.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: current_sleep_turns + 1,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                            incoming_instructions
                                .instruction_list
                                .push(Instruction::ChangeStatus(ChangeStatusInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    old_status: PokemonStatus::SLEEP,
                                    new_status: PokemonStatus::NONE,
                                }));
                            incoming_instructions.instruction_list.push(
                                Instruction::SetSleepTurns(SetSleepTurnsInstruction {
                                    side_ref: *attacking_side_ref,
                                    pokemon_index: current_active_index,
                                    new_turns: 0,
                                    previous_turns: current_sleep_turns,
                                }),
                            );
                            attacker_active.status = PokemonStatus::NONE;
                            attacker_active.sleep_turns = 0;
                        }
                        do_nothing_instructions.update_percentage(do_nothing_percentage);
                        incoming_instructions.update_percentage(1.0 - do_nothing_percentage);
                        final_instructions.push(do_nothing_instructions);
                    }
                }
                // Pokemon is asleep because of Rest, and will wake up this turn
                1 => {
                    attacker_active.status = PokemonStatus::NONE;
                    attacker_active.rest_turns -= 1;
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::ChangeStatus(ChangeStatusInstruction {
                            side_ref: *attacking_side_ref,
                            pokemon_index: current_active_index,
                            old_status: PokemonStatus::SLEEP,
                            new_status: PokemonStatus::NONE,
                        }));
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::DecrementRestTurns(
                            DecrementRestTurnsInstruction {
                                side_ref: *attacking_side_ref,
                            },
                        ));
                }
                // Pokemon is asleep because of Rest, and will stay asleep this turn
                2 | 3 => {
                    attacker_active.rest_turns -= 1;
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::DecrementRestTurns(
                            DecrementRestTurnsInstruction {
                                side_ref: *attacking_side_ref,
                            },
                        ));
                }
                _ => panic!("Invalid rest_turns value: {}", attacker_active.rest_turns),
            }
        }
        _ => {}
    }

    if attacking_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::CONFUSION)
    {
        let mut hit_yourself_instruction = incoming_instructions.clone();
        hit_yourself_instruction.update_percentage(HIT_SELF_IN_CONFUSION_CHANCE);

        let attacking_stat = attacking_side.calculate_boosted_stat(PokemonBoostableStat::Attack);
        let defending_stat = attacking_side.calculate_boosted_stat(PokemonBoostableStat::Defense);

        let attacker_active = attacking_side.get_active();
        let mut damage_dealt = 2.0 * attacker_active.level as f32;
        damage_dealt = damage_dealt.floor() / 5.0;
        damage_dealt = damage_dealt.floor() + 2.0;
        damage_dealt = damage_dealt.floor() * 40.0; // 40 is the base power of confusion damage
        damage_dealt = damage_dealt * attacking_stat as f32 / defending_stat as f32;
        damage_dealt = damage_dealt.floor() / 50.0;
        damage_dealt = damage_dealt.floor() + 2.0;
        if attacker_active.status == PokemonStatus::BURN {
            damage_dealt /= 2.0;
        }

        let damage_dealt = cmp::min(damage_dealt as i16, attacker_active.hp);
        let damage_instruction = Instruction::Damage(DamageInstruction {
            side_ref: *attacking_side_ref,
            damage_amount: damage_dealt,
        });
        hit_yourself_instruction
            .instruction_list
            .push(damage_instruction);

        final_instructions.push(hit_yourself_instruction);

        incoming_instructions.update_percentage(1.0 - HIT_SELF_IN_CONFUSION_CHANCE);
    }

    if attacking_side.side_conditions.protect > 0 {
        let protect_success_chance =
            CONSECUTIVE_PROTECT_CHANCE.powi(attacking_side.side_conditions.protect as i32);
        let mut protect_fail_instruction = incoming_instructions.clone();
        protect_fail_instruction.update_percentage(1.0 - protect_success_chance);
        final_instructions.push(protect_fail_instruction);
        incoming_instructions.update_percentage(protect_success_chance);
    }
}

pub fn generate_instructions_from_move(
    state: &mut State,
    choice: &mut Choice,
    defender_choice: &Choice,
    attacking_side: SideReference,
    mut incoming_instructions: StateInstructions,
    mut final_instructions: &mut Vec<StateInstructions>,
    branch_on_damage: bool,
) {
    if state.use_damage_dealt {
        reset_damage_dealt(
            state.get_side(&attacking_side),
            &attacking_side,
            &mut incoming_instructions,
        );
    }

    if choice.category == MoveCategory::Switch {
        generate_instructions_from_switch(
            state,
            choice.switch_id,
            attacking_side,
            &mut incoming_instructions,
        );
        final_instructions.push(incoming_instructions);
        return;
    }

    let attacker_side = state.get_side(&attacking_side);

    if choice.move_id == Choices::NONE {
        if attacker_side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::MUSTRECHARGE)
        {
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: attacking_side,
                        volatile_status: PokemonVolatileStatus::MUSTRECHARGE,
                    },
                ));
        }
        final_instructions.push(incoming_instructions);
        return;
    }

    if attacker_side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::TRUANT)
    {
        incoming_instructions
            .instruction_list
            .push(Instruction::RemoveVolatileStatus(
                RemoveVolatileStatusInstruction {
                    side_ref: attacking_side,
                    volatile_status: PokemonVolatileStatus::TRUANT,
                },
            ));
        final_instructions.push(incoming_instructions);
        return;
    }

    // TODO: test first-turn dragontail missing - it should not trigger this early return
    if !choice.first_move && defender_choice.flags.drag {
        final_instructions.push(incoming_instructions);
        return;
    }

    state.apply_instructions(&incoming_instructions.instruction_list);

    let side = state.get_side(&attacking_side);
    if side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::ENCORE)
    {
        match side.last_used_move {
            LastUsedMove::Move(last_used_move) => {
                if choice.move_index != last_used_move {
                    *choice = MOVES
                        .get(&side.get_active_immutable().moves[&last_used_move].id)
                        .unwrap()
                        .clone();
                    choice.move_index = last_used_move;
                }
            }
            _ => panic!("Encore should not be active when last used move is not a move"),
        }
    }

    if !choice.first_move
        && state
            .get_side(&attacking_side.get_other_side())
            .force_switch
    {
        state
            .get_side(&attacking_side)
            .switch_out_move_second_saved_move = choice.move_id;
        state.reverse_instructions(&incoming_instructions.instruction_list);
        final_instructions.push(incoming_instructions);
        return;
    }

    if state
        .get_side_immutable(&attacking_side)
        .get_active_immutable()
        .hp
        == 0
    {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        final_instructions.push(incoming_instructions);
        return;
    }

    // If the move is a charge move, remove the volatile status if damage was done
    if choice.flags.charge {
        let side = state.get_side(&attacking_side);
        let volatile_status = charge_choice_to_volatile(&choice.move_id);
        if side.volatile_statuses.contains(&volatile_status) {
            choice.flags.charge = false;
            let instruction = Instruction::RemoveVolatileStatus(RemoveVolatileStatusInstruction {
                side_ref: attacking_side,
                volatile_status: volatile_status,
            });
            incoming_instructions.instruction_list.push(instruction);
            side.volatile_statuses.remove(&volatile_status);
        }
    }

    if cannot_use_move(state, &choice, &attacking_side) {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        final_instructions.push(incoming_instructions);
        return;
    }

    before_move(
        state,
        choice,
        defender_choice,
        &attacking_side,
        &mut incoming_instructions,
    );
    if incoming_instructions.percentage == 0.0 {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        return;
    }

    // most of the time pp decrement doesn't matter and just adds another instruction
    // so we only decrement pp if the move is at 10 or less pp since that is when it starts
    // to matter
    let (attacker_side, defender_side) = state.get_both_sides(&attacking_side);
    let active = attacker_side.get_active();
    if active.moves[&choice.move_index].pp < 10 {
        let pp_decrement_amount = if choice.target == MoveTarget::Opponent
            && defender_side.get_active_immutable().ability == Abilities::PRESSURE
        {
            2
        } else {
            1
        };
        incoming_instructions
            .instruction_list
            .push(Instruction::DecrementPP(DecrementPPInstruction {
                side_ref: attacking_side,
                move_index: choice.move_index,
                amount: pp_decrement_amount,
            }));
        active.moves[&choice.move_index].pp -= pp_decrement_amount;
    }

    if state.use_last_used_move {
        set_last_used_move_as_move(
            state.get_side(&attacking_side),
            choice.move_index,
            attacking_side,
            &mut incoming_instructions,
        );
    }

    if !choice.sleep_talk_move {
        generate_instructions_from_existing_status_conditions(
            state,
            &attacking_side,
            &choice,
            &mut incoming_instructions,
            &mut final_instructions,
        );
    }
    let attacker = state
        .get_side_immutable(&attacking_side)
        .get_active_immutable();
    if choice.move_id == Choices::SLEEPTALK && attacker.status == PokemonStatus::SLEEP {
        let new_choices = attacker.get_sleep_talk_choices();
        state.reverse_instructions(&incoming_instructions.instruction_list);
        let num_choices = new_choices.len() as f32;
        for mut new_choice in new_choices {
            new_choice.sleep_talk_move = true;
            let mut sleep_talk_instructions = incoming_instructions.clone();
            sleep_talk_instructions.update_percentage(1.0 / num_choices);
            generate_instructions_from_move(
                state,
                &mut new_choice,
                defender_choice,
                attacking_side,
                sleep_talk_instructions,
                &mut final_instructions,
                false,
            );
        }
        return;
    } else if attacker.status == PokemonStatus::SLEEP && !choice.sleep_talk_move {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        if incoming_instructions.percentage > 0.0 {
            final_instructions.push(incoming_instructions);
        }
        return;
    }

    if move_has_no_effect(state, &choice, &attacking_side) {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        final_instructions.push(incoming_instructions);
        return;
    }
    choice_special_effect(state, choice, &attacking_side, &mut incoming_instructions);
    let damage = calculate_damage(state, &attacking_side, &choice, DamageRolls::Max);
    check_move_hit_or_miss(
        state,
        &choice,
        &attacking_side,
        damage,
        &mut incoming_instructions,
        &mut final_instructions,
    );

    if incoming_instructions.percentage == 0.0 {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        return;
    }

    // start multi-hit
    let hit_count;
    match choice.multi_hit() {
        MultiHitMove::None => {
            hit_count = 1;
        }
        MultiHitMove::DoubleHit => {
            hit_count = 2;
        }
        MultiHitMove::TripleHit => {
            hit_count = 3;
        }
        MultiHitMove::TwoToFiveHits => {
            // too lazy to implement branching here. Average is 3.2 so this is a fine approximation
            hit_count = 3;
        }
        MultiHitMove::PopulationBomb => {
            // population bomb checks accuracy each time but lets approximate
            hit_count = if state.get_side(&attacking_side).get_active().item == Items::WIDELENS {
                9
            } else {
                6
            };
        }
        MultiHitMove::TripleAxel => {
            // triple axel checks accuracy each time but until multi-accuracy is implemented this
            // is the best we can do
            hit_count = 3
        }
    }

    let (_attacker_side, defender_side) = state.get_both_sides(&attacking_side);
    let defender_active = defender_side.get_active();
    let mut does_damage = false;
    let (mut branch_damage, mut regular_damage) = (0, 0);
    let mut branch_instructions: Option<StateInstructions> = None;
    if let Some((max_damage_dealt, max_crit_damage)) = damage {
        does_damage = true;
        let avg_damage_dealt = (max_damage_dealt as f32 * 0.925) as i16;
        let min_damage_dealt = (max_damage_dealt as f32 * 0.85) as i16;
        if branch_on_damage
            && max_damage_dealt >= defender_active.hp
            && min_damage_dealt < defender_active.hp
        {
            let (average_non_kill_damage, num_kill_rolls) =
                compare_health_with_damage_multiples(max_damage_dealt, defender_active.hp);

            let crit_rate = if defender_active.ability == Abilities::BATTLEARMOR
                || defender_active.ability == Abilities::SHELLARMOR
            {
                0.0
            } else if choice.move_id.guaranteed_crit() {
                1.0
            } else if choice.move_id.increased_crit_ratio() {
                1.0 / 8.0
            } else {
                BASE_CRIT_CHANCE
            };

            // the chance of a branch is the chance of the roll killing + the chance of a crit
            let branch_chance = ((1.0 - crit_rate) * (num_kill_rolls as f32 / 16.0)) + crit_rate;

            let mut branch_ins = incoming_instructions.clone();
            branch_ins.update_percentage(branch_chance);
            branch_instructions = Some(branch_ins);
            branch_damage = defender_active.hp;

            incoming_instructions.update_percentage(1.0 - branch_chance);
            regular_damage = average_non_kill_damage;
        } else if branch_on_damage && max_damage_dealt < defender_active.hp {
            let crit_rate = if defender_active.ability == Abilities::BATTLEARMOR
                || defender_active.ability == Abilities::SHELLARMOR
            {
                0.0
            } else if choice.move_id.guaranteed_crit() {
                1.0
            } else if choice.move_id.increased_crit_ratio() {
                1.0 / 8.0
            } else {
                BASE_CRIT_CHANCE
            };
            let mut branch_ins = incoming_instructions.clone();
            branch_ins.update_percentage(crit_rate);
            branch_instructions = Some(branch_ins);
            branch_damage = (max_crit_damage as f32 * 0.925) as i16;
            incoming_instructions.update_percentage(1.0 - crit_rate);
            regular_damage = (max_damage_dealt as f32 * 0.925) as i16;
        } else {
            regular_damage = avg_damage_dealt;
        }
    }

    if incoming_instructions.percentage != 0.0 {
        run_move(
            state,
            attacking_side,
            incoming_instructions,
            hit_count,
            does_damage,
            regular_damage,
            choice,
            defender_choice,
            &mut final_instructions,
        );
    } else {
        state.reverse_instructions(&incoming_instructions.instruction_list);
    }

    // A branch representing either a roll that kills the opponent or a crit
    if let Some(branch_ins) = branch_instructions {
        if branch_ins.percentage != 0.0 {
            state.apply_instructions(&branch_ins.instruction_list);
            run_move(
                state,
                attacking_side,
                branch_ins,
                hit_count,
                does_damage,
                branch_damage,
                choice,
                defender_choice,
                &mut final_instructions,
            );
        }
    }

    combine_duplicate_instructions(&mut final_instructions);
    return;
}

fn combine_duplicate_instructions(list_of_instructions: &mut Vec<StateInstructions>) {
    for i in 0..list_of_instructions.len() {
        let mut j = i + 1;
        while j < list_of_instructions.len() {
            if list_of_instructions[i].instruction_list == list_of_instructions[j].instruction_list
            {
                list_of_instructions[i].percentage += list_of_instructions[j].percentage;
                list_of_instructions.remove(j);
            } else {
                j += 1;
            }
        }
    }
}

fn get_effective_speed(state: &State, side_reference: &SideReference) -> i16 {
    let side = state.get_side_immutable(side_reference);
    let active_pkmn = side.get_active_immutable();

    let mut boosted_speed = side.calculate_boosted_stat(PokemonBoostableStat::Speed) as f32;

    match state.weather.weather_type {
        Weather::SUN if active_pkmn.ability == Abilities::CHLOROPHYLL => boosted_speed *= 2.0,
        Weather::RAIN if active_pkmn.ability == Abilities::SWIFTSWIM => boosted_speed *= 2.0,
        _ => {}
    }

    if side
        .volatile_statuses
        .contains(&PokemonVolatileStatus::SLOWSTART)
    {
        boosted_speed *= 0.5;
    }

    if active_pkmn.status == PokemonStatus::PARALYZE {
        boosted_speed *= 0.25;
    }

    boosted_speed as i16
}

fn moves_first(
    state: &State,
    side_one_choice: &Choice,
    side_two_choice: &Choice,
) -> SideMovesFirst {
    let side_one_effective_speed = get_effective_speed(&state, &SideReference::SideOne);
    let side_two_effective_speed = get_effective_speed(&state, &SideReference::SideTwo);

    if side_one_choice.category == MoveCategory::Switch
        && side_two_choice.category == MoveCategory::Switch
    {
        return if side_one_effective_speed > side_two_effective_speed {
            SideMovesFirst::SideOne
        } else if side_one_effective_speed == side_two_effective_speed {
            SideMovesFirst::SpeedTie
        } else {
            SideMovesFirst::SideTwo
        };
    } else if side_one_choice.category == MoveCategory::Switch {
        return if side_two_choice.move_id != Choices::PURSUIT {
            SideMovesFirst::SideOne
        } else {
            SideMovesFirst::SideTwo
        };
    } else if side_two_choice.category == MoveCategory::Switch {
        return if side_one_choice.move_id == Choices::PURSUIT {
            SideMovesFirst::SideOne
        } else {
            SideMovesFirst::SideTwo
        };
    }

    if side_one_choice.priority == side_two_choice.priority {
        if side_one_effective_speed == side_two_effective_speed {
            return SideMovesFirst::SpeedTie;
        }
        if side_one_effective_speed > side_two_effective_speed {
            SideMovesFirst::SideOne
        } else {
            SideMovesFirst::SideTwo
        }
    } else {
        if side_one_choice.priority > side_two_choice.priority {
            SideMovesFirst::SideOne
        } else {
            SideMovesFirst::SideTwo
        }
    }
}

fn add_end_of_turn_instructions(
    state: &mut State,
    mut incoming_instructions: &mut StateInstructions,
    first_move_side: &SideReference,
) {
    state.apply_instructions(&incoming_instructions.instruction_list);
    if state.side_one.force_switch || state.side_two.force_switch {
        state.reverse_instructions(&incoming_instructions.instruction_list);
        return;
    }

    let sides = [first_move_side, &first_move_side.get_other_side()];

    // Weather decrement / dissipation
    if state.weather.turns_remaining > 0 && state.weather.weather_type != Weather::NONE {
        let weather_dissipate_instruction = Instruction::DecrementWeatherTurnsRemaining;
        incoming_instructions
            .instruction_list
            .push(weather_dissipate_instruction);
        state.weather.turns_remaining -= 1;
        if state.weather.turns_remaining == 0 {
            let weather_end_instruction = Instruction::ChangeWeather(ChangeWeather {
                new_weather: Weather::NONE,
                new_weather_turns_remaining: 0,
                previous_weather: state.weather.weather_type,
                previous_weather_turns_remaining: 0,
            });
            incoming_instructions
                .instruction_list
                .push(weather_end_instruction);
            state.weather.weather_type = Weather::NONE;
        }
    }

    // Side Condition decrement
    for side_ref in sides {
        let side = state.get_side(side_ref);
        if side.side_conditions.reflect > 0 {
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeSideCondition(
                    ChangeSideConditionInstruction {
                        side_ref: *side_ref,
                        side_condition: PokemonSideCondition::Reflect,
                        amount: -1,
                    },
                ));
            side.side_conditions.reflect -= 1;
        }
        if side.side_conditions.light_screen > 0 {
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeSideCondition(
                    ChangeSideConditionInstruction {
                        side_ref: *side_ref,
                        side_condition: PokemonSideCondition::LightScreen,
                        amount: -1,
                    },
                ));
            side.side_conditions.light_screen -= 1;
        }
    }

    // Weather Damage
    for side_ref in sides {
        if state.weather_is_active(&Weather::HAIL) {
            let active_pkmn = state.get_side(side_ref).get_active();
            if active_pkmn.hp == 0 || active_pkmn.has_type(&PokemonType::ICE) {
                continue;
            }

            let damage_amount =
                cmp::min((active_pkmn.maxhp as f32 * 0.0625) as i16, active_pkmn.hp);
            let hail_damage_instruction = Instruction::Damage(DamageInstruction {
                side_ref: *side_ref,
                damage_amount: damage_amount,
            });

            active_pkmn.hp -= damage_amount;
            incoming_instructions
                .instruction_list
                .push(hail_damage_instruction);
        } else if state.weather_is_active(&Weather::SAND) {
            let active_pkmn = state.get_side(side_ref).get_active();
            if active_pkmn.hp == 0
                || active_pkmn.has_type(&PokemonType::GROUND)
                || active_pkmn.has_type(&PokemonType::STEEL)
                || active_pkmn.has_type(&PokemonType::ROCK)
            {
                continue;
            }
            let damage_amount =
                cmp::min((active_pkmn.maxhp as f32 * 0.0625) as i16, active_pkmn.hp);
            let sand_damage_instruction = Instruction::Damage(DamageInstruction {
                side_ref: *side_ref,
                damage_amount: damage_amount,
            });
            active_pkmn.hp -= damage_amount;
            incoming_instructions
                .instruction_list
                .push(sand_damage_instruction);
        }
    }

    // future sight
    for side_ref in sides {
        let (attacking_side, defending_side) = state.get_both_sides(side_ref);
        if attacking_side.future_sight.0 > 0 {
            let decrement_future_sight_instruction =
                Instruction::DecrementFutureSight(DecrementFutureSightInstruction {
                    side_ref: *side_ref,
                });
            if attacking_side.future_sight.0 == 1 {
                let mut damage = calculate_futuresight_damage(
                    &attacking_side,
                    &defending_side,
                    &attacking_side.future_sight.1,
                );
                let defender = defending_side.get_active();
                damage = cmp::min(damage, defender.hp);
                let future_sight_damage_instruction = Instruction::Damage(DamageInstruction {
                    side_ref: side_ref.get_other_side(),
                    damage_amount: damage,
                });
                incoming_instructions
                    .instruction_list
                    .push(future_sight_damage_instruction);
                defender.hp -= damage;
            }
            attacking_side.future_sight.0 -= 1;
            incoming_instructions
                .instruction_list
                .push(decrement_future_sight_instruction);
        }
    }

    // wish
    for side_ref in sides {
        let side = state.get_side(side_ref);
        let side_wish = side.wish;
        let active_pkmn = side.get_active();

        if side_wish.0 > 0 {
            let decrement_wish_instruction = Instruction::DecrementWish(DecrementWishInstruction {
                side_ref: *side_ref,
            });
            if side_wish.0 == 1 && 0 < active_pkmn.hp && active_pkmn.hp < active_pkmn.maxhp {
                let heal_amount =
                    cmp::min(active_pkmn.maxhp - active_pkmn.hp, active_pkmn.maxhp / 2);

                let wish_heal_instruction = Instruction::Heal(HealInstruction {
                    side_ref: *side_ref,
                    heal_amount: heal_amount,
                });
                incoming_instructions
                    .instruction_list
                    .push(wish_heal_instruction);
                active_pkmn.hp += heal_amount;
            }
            side.wish.0 -= 1;
            incoming_instructions
                .instruction_list
                .push(decrement_wish_instruction);
        }
    }

    // status damage
    for side_ref in sides {
        let side = state.get_side(side_ref);
        let toxic_count = side.side_conditions.toxic_count as f32;
        let active_pkmn = side.get_active();
        if active_pkmn.hp == 0 {
            continue;
        }

        match active_pkmn.status {
            PokemonStatus::BURN => {
                let damage_factor = 0.125;

                let damage_amount = cmp::max(
                    cmp::min(
                        (active_pkmn.maxhp as f32 * damage_factor) as i16,
                        active_pkmn.hp,
                    ),
                    1,
                );
                let burn_damage_instruction = Instruction::Damage(DamageInstruction {
                    side_ref: *side_ref,
                    damage_amount,
                });
                active_pkmn.hp -= damage_amount;
                incoming_instructions
                    .instruction_list
                    .push(burn_damage_instruction);
            }
            PokemonStatus::POISON => {
                let damage_amount = cmp::max(
                    1,
                    cmp::min((active_pkmn.maxhp as f32 * 0.125) as i16, active_pkmn.hp),
                );

                let poison_damage_instruction = Instruction::Damage(DamageInstruction {
                    side_ref: *side_ref,
                    damage_amount,
                });
                active_pkmn.hp -= damage_amount;
                incoming_instructions
                    .instruction_list
                    .push(poison_damage_instruction);
            }
            PokemonStatus::TOXIC => {
                let toxic_multiplier = (1.0 / 16.0) * toxic_count + (1.0 / 16.0);
                let damage_amount = cmp::max(
                    cmp::min(
                        (active_pkmn.maxhp as f32 * toxic_multiplier) as i16,
                        active_pkmn.hp,
                    ),
                    1,
                );
                let toxic_damage_instruction = Instruction::Damage(DamageInstruction {
                    side_ref: *side_ref,
                    damage_amount,
                });

                active_pkmn.hp -= damage_amount;
                incoming_instructions
                    .instruction_list
                    .push(toxic_damage_instruction);

                let toxic_counter_increment_instruction =
                    Instruction::ChangeSideCondition(ChangeSideConditionInstruction {
                        side_ref: *side_ref,
                        side_condition: PokemonSideCondition::ToxicCount,
                        amount: 1,
                    });
                side.side_conditions.toxic_count += 1;
                incoming_instructions
                    .instruction_list
                    .push(toxic_counter_increment_instruction);
            }
            _ => {}
        }
    }

    // ability/item end-of-turn effects
    for side_ref in sides {
        let side = state.get_side(side_ref);
        let active_pkmn = side.get_active();
        if active_pkmn.hp == 0 {
            continue;
        }
        item_end_of_turn(state, side_ref, &mut incoming_instructions);
        ability_end_of_turn(state, side_ref, &mut incoming_instructions);
    }

    // leechseed sap
    for side_ref in sides {
        let (leechseed_side, other_side) = state.get_both_sides(side_ref);
        if leechseed_side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::LEECHSEED)
        {
            let active_pkmn = leechseed_side.get_active();
            let other_active_pkmn = other_side.get_active();
            if active_pkmn.hp == 0 || other_active_pkmn.hp == 0 {
                continue;
            }

            let health_sapped = cmp::min((active_pkmn.maxhp as f32 * 0.125) as i16, active_pkmn.hp);
            let damage_ins = Instruction::Damage(DamageInstruction {
                side_ref: *side_ref,
                damage_amount: health_sapped,
            });
            active_pkmn.hp -= health_sapped;
            incoming_instructions.instruction_list.push(damage_ins);

            let health_recovered = cmp::min(
                health_sapped,
                other_active_pkmn.maxhp - other_active_pkmn.hp,
            );
            if health_recovered > 0 {
                let heal_ins = Instruction::Heal(HealInstruction {
                    side_ref: side_ref.get_other_side(),
                    heal_amount: health_recovered,
                });
                other_active_pkmn.hp += health_recovered;
                incoming_instructions.instruction_list.push(heal_ins);
            }
        }
    }

    // volatile statuses
    for side_ref in sides {
        let side = state.get_side(side_ref);
        if side.get_active().hp == 0 {
            continue;
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::SLOWSTART)
        {
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeVolatileStatusDuration(
                    ChangeVolatileStatusDurationInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::SLOWSTART,
                        amount: -1,
                    },
                ));
            side.volatile_status_durations.slowstart -= 1;
            if side.volatile_status_durations.slowstart == 0 {
                incoming_instructions
                    .instruction_list
                    .push(Instruction::RemoveVolatileStatus(
                        RemoveVolatileStatusInstruction {
                            side_ref: *side_ref,
                            volatile_status: PokemonVolatileStatus::SLOWSTART,
                        },
                    ));
                side.volatile_statuses
                    .remove(&PokemonVolatileStatus::SLOWSTART);
            }
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::LOCKEDMOVE)
        {
            // the number says 2 but this is 3 turns of using a locking move
            // because turn 0 is the first turn the move is used
            // branching is not implemented here so the engine assumes it always lasts 3 turns
            if side.volatile_status_durations.lockedmove == 2 {
                side.volatile_status_durations.lockedmove = 0;
                side.volatile_statuses
                    .remove(&PokemonVolatileStatus::LOCKEDMOVE);
                incoming_instructions.instruction_list.push(
                    Instruction::ChangeVolatileStatusDuration(
                        ChangeVolatileStatusDurationInstruction {
                            side_ref: *side_ref,
                            volatile_status: PokemonVolatileStatus::LOCKEDMOVE,
                            amount: -2,
                        },
                    ),
                );
                incoming_instructions
                    .instruction_list
                    .push(Instruction::RemoveVolatileStatus(
                        RemoveVolatileStatusInstruction {
                            side_ref: *side_ref,
                            volatile_status: PokemonVolatileStatus::LOCKEDMOVE,
                        },
                    ));
                if !side
                    .volatile_statuses
                    .contains(&PokemonVolatileStatus::CONFUSION)
                {
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::ApplyVolatileStatus(
                            ApplyVolatileStatusInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::CONFUSION,
                            },
                        ));
                    side.volatile_statuses
                        .insert(PokemonVolatileStatus::CONFUSION);
                }
            } else {
                side.volatile_status_durations.lockedmove += 1;
                incoming_instructions.instruction_list.push(
                    Instruction::ChangeVolatileStatusDuration(
                        ChangeVolatileStatusDurationInstruction {
                            side_ref: *side_ref,
                            volatile_status: PokemonVolatileStatus::LOCKEDMOVE,
                            amount: 1,
                        },
                    ),
                );
            }
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::YAWN)
        {
            match side.volatile_status_durations.yawn {
                0 => {
                    incoming_instructions.instruction_list.push(
                        Instruction::ChangeVolatileStatusDuration(
                            ChangeVolatileStatusDurationInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::YAWN,
                                amount: 1,
                            },
                        ),
                    );
                    side.volatile_status_durations.yawn += 1;
                }
                1 => {
                    side.volatile_statuses.remove(&PokemonVolatileStatus::YAWN);
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::RemoveVolatileStatus(
                            RemoveVolatileStatusInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::YAWN,
                            },
                        ));
                    incoming_instructions.instruction_list.push(
                        Instruction::ChangeVolatileStatusDuration(
                            ChangeVolatileStatusDurationInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::YAWN,
                                amount: -1,
                            },
                        ),
                    );
                    side.volatile_status_durations.yawn -= 1;

                    let active = side.get_active();
                    if active.status == PokemonStatus::NONE {
                        active.status = PokemonStatus::SLEEP;
                        incoming_instructions
                            .instruction_list
                            .push(Instruction::ChangeStatus(ChangeStatusInstruction {
                                side_ref: *side_ref,
                                pokemon_index: side.active_index,
                                old_status: PokemonStatus::NONE,
                                new_status: PokemonStatus::SLEEP,
                            }));
                    }
                }
                _ => panic!(
                    "Yawn duration cannot be {} when yawn volatile is active",
                    side.volatile_status_durations.yawn
                ),
            }
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::PERISH1)
        {
            let active_pkmn = side.get_active();
            incoming_instructions
                .instruction_list
                .push(Instruction::Damage(DamageInstruction {
                    side_ref: *side_ref,
                    damage_amount: active_pkmn.hp,
                }));
            active_pkmn.hp = 0;
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::PERISH2)
        {
            side.volatile_statuses
                .remove(&PokemonVolatileStatus::PERISH2);
            side.volatile_statuses
                .insert(PokemonVolatileStatus::PERISH1);
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH2,
                    },
                ));
            incoming_instructions
                .instruction_list
                .push(Instruction::ApplyVolatileStatus(
                    ApplyVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH1,
                    },
                ));
        }
        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::PERISH3)
        {
            side.volatile_statuses
                .remove(&PokemonVolatileStatus::PERISH3);
            side.volatile_statuses
                .insert(PokemonVolatileStatus::PERISH2);
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH3,
                    },
                ));
            incoming_instructions
                .instruction_list
                .push(Instruction::ApplyVolatileStatus(
                    ApplyVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH2,
                    },
                ));
        }
        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::PERISH4)
        {
            side.volatile_statuses
                .remove(&PokemonVolatileStatus::PERISH4);
            side.volatile_statuses
                .insert(PokemonVolatileStatus::PERISH3);
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH4,
                    },
                ));
            incoming_instructions
                .instruction_list
                .push(Instruction::ApplyVolatileStatus(
                    ApplyVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::PERISH3,
                    },
                ));
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::FLINCH)
        {
            side.volatile_statuses
                .remove(&PokemonVolatileStatus::FLINCH);
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: PokemonVolatileStatus::FLINCH,
                    },
                ));
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::PARTIALLYTRAPPED)
        {
            let active_pkmn = side.get_active();
            let damage_amount = cmp::min((active_pkmn.maxhp as f32 / 16.0) as i16, active_pkmn.hp);

            incoming_instructions
                .instruction_list
                .push(Instruction::Damage(DamageInstruction {
                    side_ref: *side_ref,
                    damage_amount,
                }));
            active_pkmn.hp -= damage_amount;
        }

        let possible_statuses = [
            PokemonVolatileStatus::PROTECT,
            PokemonVolatileStatus::ENDURE,
        ];

        let mut protect_vs = None;
        for status in &possible_statuses {
            if side.volatile_statuses.contains(status) {
                protect_vs = Some(*status);
                break;
            }
        }

        if let Some(protect_vs) = protect_vs {
            incoming_instructions
                .instruction_list
                .push(Instruction::RemoveVolatileStatus(
                    RemoveVolatileStatusInstruction {
                        side_ref: *side_ref,
                        volatile_status: protect_vs,
                    },
                ));
            side.volatile_statuses.remove(&protect_vs);
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeSideCondition(
                    ChangeSideConditionInstruction {
                        side_ref: *side_ref,
                        side_condition: PokemonSideCondition::Protect,
                        amount: 1,
                    },
                ));
            side.side_conditions.protect += 1;
        } else if side.side_conditions.protect > 0 {
            incoming_instructions
                .instruction_list
                .push(Instruction::ChangeSideCondition(
                    ChangeSideConditionInstruction {
                        side_ref: *side_ref,
                        side_condition: PokemonSideCondition::Protect,
                        amount: -1 * side.side_conditions.protect,
                    },
                ));
            side.side_conditions.protect -= side.side_conditions.protect;
        }

        if side
            .volatile_statuses
            .contains(&PokemonVolatileStatus::TAUNT)
        {
            match side.volatile_status_durations.taunt {
                0 => {
                    incoming_instructions.instruction_list.push(
                        Instruction::ChangeVolatileStatusDuration(
                            ChangeVolatileStatusDurationInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::TAUNT,
                                amount: 1,
                            },
                        ),
                    );
                    side.volatile_status_durations.taunt += 1;
                }
                1 => {
                    side.volatile_statuses.remove(&PokemonVolatileStatus::TAUNT);
                    incoming_instructions
                        .instruction_list
                        .push(Instruction::RemoveVolatileStatus(
                            RemoveVolatileStatusInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::TAUNT,
                            },
                        ));
                    incoming_instructions.instruction_list.push(
                        Instruction::ChangeVolatileStatusDuration(
                            ChangeVolatileStatusDurationInstruction {
                                side_ref: *side_ref,
                                volatile_status: PokemonVolatileStatus::TAUNT,
                                amount: -1,
                            },
                        ),
                    );
                    side.volatile_status_durations.taunt -= 1;
                    state.re_enable_disabled_moves(
                        side_ref,
                        &mut incoming_instructions.instruction_list,
                    );
                }
                _ => panic!(
                    "Taunt duration cannot be {} when taunt volatile is active",
                    side.volatile_status_durations.taunt
                ),
            }
        }
    } // end volatile statuses

    state.reverse_instructions(&incoming_instructions.instruction_list);
}

fn end_of_turn_triggered(side_one_move: &MoveChoice, side_two_move: &MoveChoice) -> bool {
    !(matches!(side_one_move, &MoveChoice::Switch(_)) && side_two_move == &MoveChoice::None)
        && !(side_one_move == &MoveChoice::None && matches!(side_two_move, &MoveChoice::Switch(_)))
}

fn run_move(
    state: &mut State,
    attacking_side: SideReference,
    mut instructions: StateInstructions,
    hit_count: i8,
    does_damage: bool,
    damage_amount: i16,
    choice: &mut Choice,
    defender_choice: &Choice,
    final_instructions: &mut Vec<StateInstructions>,
) {
    let mut hit_sub = false;
    for _ in 0..hit_count {
        if does_damage {
            hit_sub = generate_instructions_from_damage(
                state,
                choice,
                damage_amount,
                &attacking_side,
                &mut instructions,
            );
        }
        if let Some(side_condition) = &choice.side_condition {
            generate_instructions_from_side_conditions(
                state,
                side_condition,
                &attacking_side,
                &mut instructions,
            );
        }
        choice_hazard_clear(state, &choice, &attacking_side, &mut instructions);
        if let Some(volatile_status) = &choice.volatile_status {
            get_instructions_from_volatile_statuses(
                state,
                &choice,
                volatile_status,
                &attacking_side,
                &mut instructions,
            );
        }
        if let Some(status) = &choice.status {
            get_instructions_from_status_effects(
                state,
                status,
                &attacking_side,
                &mut instructions,
                hit_sub,
            );
        }
        if let Some(heal) = &choice.heal {
            get_instructions_from_heal(state, heal, &attacking_side, &mut instructions);
        }
    } // end multi-hit
      // this is wrong, but I am deciding it is good enough for this engine (for now)
      // each multi-hit move should trigger a chance for a secondary effect,
      // but the way this engine was structured makes it difficult to implement
      // without some performance hits.

    if let Some(boost) = &choice.boost {
        get_instructions_from_boosts(state, boost, &attacking_side, &mut instructions);
    }

    if choice.flags.drag {
        get_instructions_from_drag(state, &attacking_side, instructions, final_instructions);
        return;
    }

    // Only entered if the move causes a switch-out
    // U-turn, Volt Switch, Baton Pass, etc.
    // This deals with a bunch of flags that are required for the next turn to run properly
    if choice.flags.pivot {
        match attacking_side {
            SideReference::SideOne => {
                if state.side_one.visible_alive_pkmn() > 1 {
                    if choice.move_id == Choices::BATONPASS {
                        state.side_one.baton_passing = !state.side_one.baton_passing;
                        instructions
                            .instruction_list
                            .push(Instruction::ToggleBatonPassing(
                                ToggleBatonPassingInstruction {
                                    side_ref: SideReference::SideOne,
                                },
                            ));
                    }
                    state.side_one.force_switch = !state.side_one.force_switch;
                    instructions
                        .instruction_list
                        .push(Instruction::ToggleSideOneForceSwitch);

                    if choice.first_move {
                        instructions.instruction_list.push(
                            Instruction::SetSideTwoMoveSecondSwitchOutMove(
                                SetSecondMoveSwitchOutMoveInstruction {
                                    new_choice: defender_choice.move_id,
                                    previous_choice: state
                                        .side_two
                                        .switch_out_move_second_saved_move,
                                },
                            ),
                        );
                        state.side_two.switch_out_move_second_saved_move = defender_choice.move_id;
                    } else {
                        instructions.instruction_list.push(
                            Instruction::SetSideTwoMoveSecondSwitchOutMove(
                                SetSecondMoveSwitchOutMoveInstruction {
                                    new_choice: Choices::NONE,
                                    previous_choice: state
                                        .side_two
                                        .switch_out_move_second_saved_move,
                                },
                            ),
                        );
                        state.side_two.switch_out_move_second_saved_move = defender_choice.move_id;
                    }
                }
            }
            SideReference::SideTwo => {
                if state.side_two.visible_alive_pkmn() > 1 {
                    if choice.move_id == Choices::BATONPASS {
                        state.side_two.baton_passing = !state.side_two.baton_passing;
                        instructions
                            .instruction_list
                            .push(Instruction::ToggleBatonPassing(
                                ToggleBatonPassingInstruction {
                                    side_ref: SideReference::SideTwo,
                                },
                            ));
                    }
                    state.side_two.force_switch = !state.side_two.force_switch;
                    instructions
                        .instruction_list
                        .push(Instruction::ToggleSideTwoForceSwitch);

                    if choice.first_move {
                        instructions.instruction_list.push(
                            Instruction::SetSideOneMoveSecondSwitchOutMove(
                                SetSecondMoveSwitchOutMoveInstruction {
                                    new_choice: defender_choice.move_id,
                                    previous_choice: state
                                        .side_one
                                        .switch_out_move_second_saved_move,
                                },
                            ),
                        );
                        state.side_one.switch_out_move_second_saved_move = defender_choice.move_id;
                    } else {
                        instructions.instruction_list.push(
                            Instruction::SetSideOneMoveSecondSwitchOutMove(
                                SetSecondMoveSwitchOutMoveInstruction {
                                    new_choice: Choices::NONE,
                                    previous_choice: state
                                        .side_one
                                        .switch_out_move_second_saved_move,
                                },
                            ),
                        );
                        state.side_one.switch_out_move_second_saved_move = defender_choice.move_id;
                    }
                }
            }
        }
    }

    if let Some(secondaries_vec) = &choice.secondaries {
        state.reverse_instructions(&instructions.instruction_list);
        let instructions_vec_after_secondaries = get_instructions_from_secondaries(
            state,
            &choice,
            secondaries_vec,
            &attacking_side,
            instructions,
            hit_sub,
        );
        final_instructions.extend(instructions_vec_after_secondaries);
    } else {
        state.reverse_instructions(&instructions.instruction_list);
        final_instructions.push(instructions);
    }
}

fn handle_both_moves(
    state: &mut State,
    first_move_side_choice: &mut Choice,
    second_move_side_choice: &mut Choice,
    first_move_side_ref: SideReference,
    incoming_instructions: StateInstructions,
    state_instructions_vec: &mut Vec<StateInstructions>,
    branch_on_damage: bool,
) {
    generate_instructions_from_move(
        state,
        first_move_side_choice,
        second_move_side_choice,
        first_move_side_ref,
        incoming_instructions,
        state_instructions_vec,
        branch_on_damage,
    );

    let mut i = 0;
    let vec_len = state_instructions_vec.len();
    second_move_side_choice.first_move = false;
    while i < vec_len {
        let state_instruction = state_instructions_vec.remove(0);
        generate_instructions_from_move(
            state,
            &mut second_move_side_choice.clone(), // this clone is needed because the choice may be modified in this loop
            first_move_side_choice,
            first_move_side_ref.get_other_side(),
            state_instruction,
            state_instructions_vec,
            branch_on_damage,
        );
        i += 1;
    }
}

pub fn generate_instructions_from_move_pair(
    state: &mut State,
    side_one_move: &MoveChoice,
    side_two_move: &MoveChoice,
    branch_on_damage: bool,
) -> Vec<StateInstructions> {
    let mut side_one_choice;
    match side_one_move {
        MoveChoice::Switch(switch_id) => {
            side_one_choice = Choice::default();
            side_one_choice.switch_id = *switch_id;
            side_one_choice.category = MoveCategory::Switch;
        }
        MoveChoice::Move(move_index) => {
            side_one_choice = state.side_one.get_active().moves[move_index].choice.clone();
            side_one_choice.move_index = *move_index;
        }
        MoveChoice::None => {
            side_one_choice = Choice::default();
        }
    }

    let mut side_two_choice;
    match side_two_move {
        MoveChoice::Switch(switch_id) => {
            side_two_choice = Choice::default();
            side_two_choice.switch_id = *switch_id;
            side_two_choice.category = MoveCategory::Switch;
        }
        MoveChoice::Move(move_index) => {
            side_two_choice = state.side_two.get_active().moves[move_index].choice.clone();
            side_two_choice.move_index = *move_index;
        }
        MoveChoice::None => {
            side_two_choice = Choice::default();
        }
    }

    let mut state_instructions_vec: Vec<StateInstructions> = Vec::with_capacity(4);
    let mut incoming_instructions: StateInstructions = StateInstructions::default();
    match moves_first(&state, &side_one_choice, &side_two_choice) {
        SideMovesFirst::SideOne => {
            handle_both_moves(
                state,
                &mut side_one_choice,
                &mut side_two_choice,
                SideReference::SideOne,
                incoming_instructions,
                &mut state_instructions_vec,
                branch_on_damage,
            );
            if end_of_turn_triggered(side_one_move, side_two_move) {
                for state_instruction in state_instructions_vec.iter_mut() {
                    add_end_of_turn_instructions(state, state_instruction, &SideReference::SideOne);
                }
            }
        }
        SideMovesFirst::SideTwo => {
            handle_both_moves(
                state,
                &mut side_two_choice,
                &mut side_one_choice,
                SideReference::SideTwo,
                incoming_instructions,
                &mut state_instructions_vec,
                branch_on_damage,
            );
            if end_of_turn_triggered(side_one_move, side_two_move) {
                for state_instruction in state_instructions_vec.iter_mut() {
                    add_end_of_turn_instructions(state, state_instruction, &SideReference::SideTwo);
                }
            }
        }
        SideMovesFirst::SpeedTie => {
            let mut side_one_moves_first_instruction = incoming_instructions.clone();
            incoming_instructions.update_percentage(0.5);
            side_one_moves_first_instruction.update_percentage(0.5);

            // side_one moves first
            handle_both_moves(
                state,
                &mut side_one_choice,
                &mut side_two_choice,
                SideReference::SideOne,
                side_one_moves_first_instruction,
                &mut state_instructions_vec,
                branch_on_damage,
            );
            if end_of_turn_triggered(side_one_move, side_two_move) {
                for state_instruction in state_instructions_vec.iter_mut() {
                    add_end_of_turn_instructions(state, state_instruction, &SideReference::SideOne);
                }
            }

            // side_two moves first
            let mut side_two_moves_first_si = Vec::with_capacity(4);
            handle_both_moves(
                state,
                &mut side_two_choice,
                &mut side_one_choice,
                SideReference::SideTwo,
                incoming_instructions,
                &mut side_two_moves_first_si,
                branch_on_damage,
            );
            if end_of_turn_triggered(side_one_move, side_two_move) {
                for state_instruction in side_two_moves_first_si.iter_mut() {
                    add_end_of_turn_instructions(state, state_instruction, &SideReference::SideTwo);
                }
            }

            // combine both vectors into the final vector
            state_instructions_vec.extend(side_two_moves_first_si);
        }
    }
    state_instructions_vec
}

pub fn calculate_damage_rolls(
    mut state: State,
    attacking_side_ref: &SideReference,
    mut choice: Choice,
    defending_choice: &Choice,
) -> Option<Vec<i16>> {
    let mut incoming_instructions = StateInstructions::default();

    if choice.flags.charge {
        choice.flags.charge = false;
    }
    if choice.move_id == Choices::FAKEOUT {
        state.get_side(attacking_side_ref).last_used_move = LastUsedMove::Switch(PokemonIndex::P0);
    }

    let attacker_active = state
        .get_side_immutable(attacking_side_ref)
        .get_active_immutable();
    let defender_active = state
        .get_side_immutable(&attacking_side_ref.get_other_side())
        .get_active_immutable();
    match choice.move_id {
        Choices::SEISMICTOSS => {
            if type_effectiveness_modifier(&PokemonType::NORMAL, &defender_active) == 0.0 {
                return None;
            }
            return Some(vec![attacker_active.level as i16]);
        }
        Choices::NIGHTSHADE => {
            if type_effectiveness_modifier(&PokemonType::GHOST, &defender_active) == 0.0 {
                return None;
            }
            return Some(vec![attacker_active.level as i16]);
        }
        Choices::ENDEAVOR => {
            if type_effectiveness_modifier(&PokemonType::GHOST, &defender_active) == 0.0
                || defender_active.hp <= attacker_active.hp
            {
                return None;
            }
            return Some(vec![defender_active.hp - attacker_active.hp]);
        }
        Choices::PAINSPLIT => {
            if type_effectiveness_modifier(&PokemonType::GHOST, &defender_active) == 0.0
                || defender_active.hp <= attacker_active.hp
            {
                return None;
            }
            return Some(vec![
                defender_active.hp - (attacker_active.hp + defender_active.hp) / 2,
            ]);
        }
        Choices::SUPERFANG
            if type_effectiveness_modifier(&PokemonType::NORMAL, &defender_active) == 0.0 =>
        {
            return None;
        }
        Choices::SUPERFANG => {
            return Some(vec![defender_active.hp / 2]);
        }

        _ => {}
    }

    before_move(
        &mut state,
        &mut choice,
        defending_choice,
        attacking_side_ref,
        &mut incoming_instructions,
    );

    if choice.move_id == Choices::FUTURESIGHT {
        choice = MOVES.get(&Choices::FUTURESIGHT)?.clone();
    }

    let mut return_vec = Vec::with_capacity(4);
    if let Some((damage, crit_damage)) =
        calculate_damage(&state, attacking_side_ref, &choice, DamageRolls::Max)
    {
        return_vec.push(damage);
        return_vec.push(crit_damage);
        Some(return_vec)
    } else {
        None
    }
}

pub fn calculate_both_damage_rolls(
    state: &State,
    mut s1_choice: Choice,
    mut s2_choice: Choice,
    side_one_moves_first: bool,
) -> (Option<Vec<i16>>, Option<Vec<i16>>) {
    if side_one_moves_first {
        s1_choice.first_move = true;
        s2_choice.first_move = false;
    } else {
        s1_choice.first_move = false;
        s2_choice.first_move = true;
    }

    let damages_dealt_s1 = calculate_damage_rolls(
        state.clone(),
        &SideReference::SideOne,
        s1_choice.clone(),
        &s2_choice,
    );
    let damages_dealt_s2 = calculate_damage_rolls(
        state.clone(),
        &SideReference::SideTwo,
        s2_choice,
        &s1_choice,
    );

    (damages_dealt_s1, damages_dealt_s2)
}
