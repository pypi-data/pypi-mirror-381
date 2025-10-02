import pytest

from poke_engine import (
    State,
    Side,
    Move,
    Pokemon,
    monte_carlo_tree_search,
    generate_instructions,
    calculate_damage,
    iterative_deepening_expectiminimax,
    Weather,
    Terrain,
)

state = State(
    side_one=Side(
        pokemon=[
            Pokemon(
                id="squirtle",
                level=100,
                types=("water", "typeless"),
                base_types=("water", "rock"),
                hp=100,
                maxhp=100,
                attack=100,
                defense=100,
                special_attack=100,
                special_defense=100,
                speed=100,
                status="none",
                moves=[
                    Move(id="watergun", pp=32),
                    Move(id="tackle", pp=32),
                    Move(id="quickattack", pp=32),
                    Move(id="leer", pp=32),
                ],
            ),
        ]
    ),
    side_two=Side(
        pokemon=[
            Pokemon(
                id="charmander",
                level=100,
                types=("fire", "typeless"),
                hp=100,
                maxhp=100,
                attack=100,
                defense=100,
                special_attack=100,
                special_defense=100,
                speed=100,
                status="none",
                moves=[
                    Move(id="ember", pp=32),
                    Move(id="tackle", pp=32),
                    Move(id="quickattack", pp=32),
                    Move(id="leer", pp=32),
                ],
            ),
        ]
    ),
    weather="none",
    weather_turns_remaining=-1,
    terrain="none",
    terrain_turns_remaining=-1,
    trick_room=False,
    trick_room_turns_remaining=-1,
)


def test_state_can_be_converted_to_and_from_a_string():
    serialized = state.to_string()
    State.from_string(serialized)
    serialized_again = state.to_string()
    assert serialized == serialized_again


def test_monte_carlo_search():
    monte_carlo_tree_search(state, 10)


def test_iterative_deepening_search():
    iterative_deepening_expectiminimax(state, 10)


def test_get_instructions():
    generate_instructions(state, "watergun", "ember")


def test_calculate_damage():
    calculate_damage(state, "watergun", "ember", True)


def test_generate_instructions_errors_when_move_does_not_exist():
    with pytest.raises(ValueError):
        generate_instructions(state, "not_a_move", "ember")
