#![cfg(not(any(feature = "gen1", feature = "gen2", feature = "gen3")))]

use poke_engine::choices::Choices;
use poke_engine::engine::generate_instructions::generate_instructions_from_move_pair;
use poke_engine::instruction::{
    ApplyVolatileStatusInstruction, DamageInstruction, Instruction,
    RemoveVolatileStatusInstruction, SetLastUsedMoveInstruction, StateInstructions,
    SwitchInstruction,
};

#[cfg(not(feature = "terastallization"))]
use poke_engine::instruction::ChangeSubsituteHealthInstruction;

#[cfg(not(feature = "terastallization"))]
use poke_engine::engine::abilities::Abilities;

#[cfg(not(feature = "gen4"))]
use poke_engine::state::PokemonBoostableStat;

#[cfg(not(feature = "gen4"))]
use poke_engine::instruction::{BoostInstruction, ChangeVolatileStatusDurationInstruction};

use poke_engine::engine::state::{MoveChoice, PokemonVolatileStatus};

use poke_engine::state::{LastUsedMove, PokemonIndex, PokemonMoveIndex, SideReference, State};

#[test]
fn test_last_used_move_is_set_on_switch() {
    let mut state = State::default();
    state.use_last_used_move = true;
    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Switch(PokemonIndex::P1),
        &MoveChoice::None,
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Switch(SwitchInstruction {
                side_ref: SideReference::SideOne,
                previous_index: PokemonIndex::P0,
                next_index: PokemonIndex::P1,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Switch(PokemonIndex::P1),
                previous_last_used_move: LastUsedMove::None,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_last_used_move_is_set_on_move() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_last_used_move_overwritten_when_dragged_out() {
    let mut state = State::default();
    state.use_last_used_move = true;

    // Only one drag option available to keep test simple
    state.side_one.pokemon.pkmn[2].hp = 0;
    state.side_one.pokemon.pkmn[3].hp = 0;
    state.side_one.pokemon.pkmn[4].hp = 0;
    state.side_one.pokemon.pkmn[5].hp = 0;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::WHIRLWIND);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 48,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Switch(SwitchInstruction {
                side_ref: SideReference::SideOne,
                previous_index: PokemonIndex::P0,
                next_index: PokemonIndex::P1,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Switch(PokemonIndex::P1),
                previous_last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(not(feature = "terastallization"))]
fn test_encore_causes_get_all_options_to_only_allow_last_used_move() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state
        .side_one
        .volatile_statuses
        .insert(PokemonVolatileStatus::ENCORE);
    state.side_one.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M0);
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    let (side_one_moves, _side_two_moves) = state.get_all_options();

    assert_eq!(
        vec![
            MoveChoice::Move(PokemonMoveIndex::M0),
            MoveChoice::Switch(PokemonIndex::P1),
            MoveChoice::Switch(PokemonIndex::P2),
            MoveChoice::Switch(PokemonIndex::P3),
            MoveChoice::Switch(PokemonIndex::P4),
            MoveChoice::Switch(PokemonIndex::P5),
        ],
        side_one_moves
    );
}

#[test]
#[cfg(not(feature = "terastallization"))]
fn test_encore_and_arenatrapped_together() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_two.get_active().ability = Abilities::ARENATRAP;
    state
        .side_one
        .volatile_statuses
        .insert(PokemonVolatileStatus::ENCORE);
    state.side_one.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M0);
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    let (side_one_moves, _side_two_moves) = state.get_all_options();

    assert_eq!(
        vec![MoveChoice::Move(PokemonMoveIndex::M0),],
        side_one_moves
    );
}

#[test]
#[cfg(not(feature = "terastallization"))]
fn test_encore_slow() {
    let mut state = State::default();
    state.use_last_used_move = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::WATERGUN);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);

    // now, apply those instructions and look for the options for next turn
    // ensure that M1 watergun is not an option
    state.apply_instructions(&vec_of_instructions[0].instruction_list);
    let (_side_one_moves, side_two_moves) = state.get_all_options();
    assert_eq!(
        vec![
            MoveChoice::Move(PokemonMoveIndex::M0),
            MoveChoice::Switch(PokemonIndex::P1),
            MoveChoice::Switch(PokemonIndex::P2),
            MoveChoice::Switch(PokemonIndex::P3),
            MoveChoice::Switch(PokemonIndex::P4),
            MoveChoice::Switch(PokemonIndex::P5),
        ],
        side_two_moves
    );
}

#[test]
#[cfg(not(feature = "terastallization"))]
fn test_encore_slow_into_substitute() {
    let mut state = State::default();
    state.use_last_used_move = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::SUBSTITUTE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::WATERGUN);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 25,
            }),
            Instruction::ChangeSubstituteHealth(ChangeSubsituteHealthInstruction {
                side_ref: SideReference::SideTwo,
                health_change: 25,
            }),
            Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::SUBSTITUTE,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);

    // now, apply those instructions and look for the options for next turn
    // ensure that M1 watergun is not an option
    state.apply_instructions(&vec_of_instructions[0].instruction_list);
    let (_side_one_moves, side_two_moves) = state.get_all_options();
    assert_eq!(
        vec![
            MoveChoice::Move(PokemonMoveIndex::M0),
            MoveChoice::Switch(PokemonIndex::P1),
            MoveChoice::Switch(PokemonIndex::P2),
            MoveChoice::Switch(PokemonIndex::P3),
            MoveChoice::Switch(PokemonIndex::P4),
            MoveChoice::Switch(PokemonIndex::P5),
        ],
        side_two_moves
    );
}

#[test]
fn test_encore_fast_fails_with_lastusedmove_equal_to_switch() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::WATERGUN);
    state.side_two.last_used_move = LastUsedMove::Switch(PokemonIndex::P0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::Switch(PokemonIndex::P0),
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_encore_fast_fails_with_lastusedmove_equal_to_none() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::WATERGUN);
    state.side_two.last_used_move = LastUsedMove::None;

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_encore_second_fails_when_opponent_switches() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.pokemon[PokemonIndex::P1].speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state.side_two.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Switch(PokemonIndex::P1),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Switch(SwitchInstruction {
                side_ref: SideReference::SideTwo,
                previous_index: PokemonIndex::P0,
                next_index: PokemonIndex::P1,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Switch(PokemonIndex::P1),
                previous_last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(not(feature = "gen4"))]
fn test_fast_encore_into_using_a_different_move_from_lum() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::ENCORE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::SWORDSDANCE);
    state.side_two.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M1);

    // side_two will try to use tackle, but will encored into watergun from last turn
    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
            }),
            Instruction::ChangeVolatileStatusDuration(ChangeVolatileStatusDurationInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
                amount: 1,
            }),
            // no setting last used move for s2 because it didn't change
            Instruction::Boost(BoostInstruction {
                side_ref: SideReference::SideTwo,
                stat: PokemonBoostableStat::Attack,
                amount: 2,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(not(feature = "gen4"))]
fn test_encore_expires_at_2_turns() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state.side_two.volatile_status_durations.encore = 2;
    state
        .side_two
        .volatile_statuses
        .insert(PokemonVolatileStatus::ENCORE);
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::NONE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::SWORDSDANCE);
    state.side_two.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M1);

    // side_two will try to use tackle, but will encored into watergun from last turn
    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::RemoveVolatileStatus(RemoveVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
            }),
            Instruction::ChangeVolatileStatusDuration(ChangeVolatileStatusDurationInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
                amount: -2,
            }),
            // no setting last used move for s2 because it didn't change
            Instruction::Boost(BoostInstruction {
                side_ref: SideReference::SideTwo,
                stat: PokemonBoostableStat::Attack,
                amount: 2,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(not(feature = "gen4"))]
fn test_encore_counter_increment() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state.side_two.volatile_status_durations.encore = 1;
    state
        .side_two
        .volatile_statuses
        .insert(PokemonVolatileStatus::ENCORE);
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::NONE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M1, Choices::SWORDSDANCE);
    state.side_two.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M1);

    // side_two will try to use tackle, but will encored into watergun from last turn
    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::ChangeVolatileStatusDuration(ChangeVolatileStatusDurationInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::ENCORE,
                amount: 1,
            }),
            // no setting last used move for s2 because it didn't change
            Instruction::Boost(BoostInstruction {
                side_ref: SideReference::SideTwo,
                stat: PokemonBoostableStat::Attack,
                amount: 2,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_fakeout_first_turn_switched_in() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FAKEOUT);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    state.side_one.last_used_move = LastUsedMove::Switch(PokemonIndex::P0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::Switch(PokemonIndex::P0),
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 48,
            }),
            Instruction::ApplyVolatileStatus(ApplyVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::FLINCH,
            }),
            // no setting last used move for s2 because it flinched and didnt get to use a move
            Instruction::RemoveVolatileStatus(RemoveVolatileStatusInstruction {
                side_ref: SideReference::SideTwo,
                volatile_status: PokemonVolatileStatus::FLINCH,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_fakeout_with_last_used_move_of_non_switch() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FAKEOUT);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    state.side_one.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::None,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_firstimpression_first_turn_switched_in() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FIRSTIMPRESSION);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    state.side_one.last_used_move = LastUsedMove::Switch(PokemonIndex::P0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideOne,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
                previous_last_used_move: LastUsedMove::Switch(PokemonIndex::P0),
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 71,
            }),
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                previous_last_used_move: LastUsedMove::None,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_firstimpression_with_last_used_move_of_non_switch() {
    let mut state = State::default();
    state.use_last_used_move = true;
    state.side_one.get_active().speed = 200;
    state.side_two.get_active().speed = 100;
    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FIRSTIMPRESSION);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);

    state.side_one.last_used_move = LastUsedMove::Move(PokemonMoveIndex::M0);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::SetLastUsedMove(SetLastUsedMoveInstruction {
                side_ref: SideReference::SideTwo,
                previous_last_used_move: LastUsedMove::None,
                last_used_move: LastUsedMove::Move(PokemonMoveIndex::M0),
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}
