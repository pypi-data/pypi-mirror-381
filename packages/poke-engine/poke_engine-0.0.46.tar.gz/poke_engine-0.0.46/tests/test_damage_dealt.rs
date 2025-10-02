#![cfg(not(any(feature = "gen1", feature = "gen2", feature = "gen3")))]

use poke_engine::choices::{Choices, MoveCategory};
use poke_engine::engine::generate_instructions::generate_instructions_from_move_pair;
use poke_engine::engine::state::{MoveChoice, PokemonVolatileStatus, Weather};
use poke_engine::instruction::{
    ChangeDamageDealtDamageInstruction, ChangeDamageDealtMoveCategoryInstruction,
    DamageInstruction, Instruction, RemoveVolatileStatusInstruction, StateInstructions,
    ToggleDamageDealtHitSubstituteInstruction,
};
use poke_engine::state::{PokemonMoveIndex, PokemonType, SideReference, State};

#[test]
fn test_previous_damage_dealt_resets_and_then_goes_to_a_new_value() {
    let mut state = State::default();
    state.use_damage_dealt = true;
    state.side_two.damage_dealt.damage = 10;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COUNTER);
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
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: -10,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 96,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_counter_after_physical_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COUNTER);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 96,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_counter_cannot_hit_ghost_type() {
    let mut state = State::default();
    state.use_damage_dealt = true;
    state.side_two.get_active().types.0 = PokemonType::GHOST;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COUNTER);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 32,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 32,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(feature = "gen3")]
fn test_counter_reflects_special_hiddenpower() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COUNTER);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::HIDDENPOWERWATER70);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 55,
            }),
            Instruction::SetDamageDealtSideTwo(SetDamageDealtSideTwoInstruction {
                damage_change: 55,
                move_category: MoveCategory::Special,
                previous_move_category: MoveCategory::Physical,
                toggle_hit_substitute: false,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 100,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
#[cfg(feature = "gen3")]
fn test_mirrorcoat_does_not_reflect_special_hiddenpower() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::MIRRORCOAT);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::HIDDENPOWERWATER70);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 55,
            }),
            Instruction::SetDamageDealtSideTwo(SetDamageDealtSideTwoInstruction {
                damage_change: 55,
                move_category: MoveCategory::Special,
                previous_move_category: MoveCategory::Physical,
                toggle_hit_substitute: false,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_metalburst_after_physical_move() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::METALBURST);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 72,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_comeuppance_after_physical_move() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COMEUPPANCE);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 72,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_metalburst_after_special_move() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::METALBURST);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::WATERGUN);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 32,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 32,
            }),
            Instruction::ChangeDamageDealtMoveCatagory(ChangeDamageDealtMoveCategoryInstruction {
                side_ref: SideReference::SideTwo,
                move_category: MoveCategory::Special,
                previous_move_category: MoveCategory::Physical,
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
fn test_metalburst_after_substitute_being_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::METALBURST);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state
        .side_one
        .volatile_statuses
        .insert(PokemonVolatileStatus::SUBSTITUTE);
    state.side_one.substitute_health = 5;

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::DamageSubstitute(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 5,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 5,
            }),
            Instruction::ToggleDamageDealtHitSubstitute(
                ToggleDamageDealtHitSubstituteInstruction {
                    side_ref: SideReference::SideTwo,
                },
            ),
            Instruction::RemoveVolatileStatus(RemoveVolatileStatusInstruction {
                side_ref: SideReference::SideOne,
                volatile_status: PokemonVolatileStatus::SUBSTITUTE,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_metalburst_fails_moving_first() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::METALBURST);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::TACKLE);
    state.side_one.get_active().speed = 100;
    state.side_two.get_active().speed = 50;

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_metalburst_after_status_move() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::METALBURST);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::SPLASH);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_counter_after_special_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::COUNTER);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::WATERGUN);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 32,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 32,
            }),
            Instruction::ChangeDamageDealtMoveCatagory(ChangeDamageDealtMoveCategoryInstruction {
                side_ref: SideReference::SideTwo,
                move_category: MoveCategory::Special,
                previous_move_category: MoveCategory::Physical,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_mirrorcoat_after_special_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::MIRRORCOAT);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::WATERGUN);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 32,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 32,
            }),
            Instruction::ChangeDamageDealtMoveCatagory(ChangeDamageDealtMoveCategoryInstruction {
                side_ref: SideReference::SideTwo,
                move_category: MoveCategory::Special,
                previous_move_category: MoveCategory::Physical,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 64,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_mirrorcoat_after_physical_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::MIRRORCOAT);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_focuspunch_after_getting_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;
    state.weather.weather_type = Weather::SUN;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FOCUSPUNCH);
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
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 48,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 48,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_focuspunch_after_substitute_getting_hit() {
    let mut state = State::default();
    state.use_damage_dealt = true;
    state
        .side_one
        .volatile_statuses
        .insert(PokemonVolatileStatus::SUBSTITUTE);
    state.side_one.substitute_health = 1;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FOCUSPUNCH);
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
            Instruction::DamageSubstitute(DamageInstruction {
                side_ref: SideReference::SideOne,
                damage_amount: 1,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_change: 1,
            }),
            Instruction::ToggleDamageDealtHitSubstitute(
                ToggleDamageDealtHitSubstituteInstruction {
                    side_ref: SideReference::SideTwo,
                },
            ),
            Instruction::RemoveVolatileStatus(RemoveVolatileStatusInstruction {
                side_ref: SideReference::SideOne,
                volatile_status: PokemonVolatileStatus::SUBSTITUTE,
            }),
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 100,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideOne,
                damage_change: 100,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}

#[test]
fn test_focuspunch_after_status_move() {
    let mut state = State::default();
    state.use_damage_dealt = true;

    state
        .side_one
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::FOCUSPUNCH);
    state
        .side_two
        .get_active()
        .replace_move(PokemonMoveIndex::M0, Choices::SPLASH);

    let vec_of_instructions = generate_instructions_from_move_pair(
        &mut state,
        &MoveChoice::Move(PokemonMoveIndex::M0),
        &MoveChoice::Move(PokemonMoveIndex::M0),
        false,
    );

    let expected_instructions = vec![StateInstructions {
        percentage: 100.0,
        instruction_list: vec![
            Instruction::Damage(DamageInstruction {
                side_ref: SideReference::SideTwo,
                damage_amount: 100,
            }),
            Instruction::ChangeDamageDealtDamage(ChangeDamageDealtDamageInstruction {
                side_ref: SideReference::SideOne,
                damage_change: 100,
            }),
        ],
    }];
    assert_eq!(expected_instructions, vec_of_instructions);
}
