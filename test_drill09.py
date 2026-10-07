"""Drill #9 입력과 이동 상태를 확인한다."""

import unittest
from types import SimpleNamespace
from math import hypot

from drill09 import (
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    MOVE_SPEED,
    SPRITE_SIZE,
    GameState,
    process_event,
    update,
)


PICO = SimpleNamespace(
    SDL_QUIT=0,
    SDL_KEYDOWN=1,
    SDL_KEYUP=2,
    SDLK_ESCAPE=27,
    SDLK_LEFT=100,
    SDLK_RIGHT=101,
    SDLK_UP=102,
    SDLK_DOWN=103,
)


def key_event(event_type, key):
    return SimpleNamespace(type=event_type, key=key)


class InputTests(unittest.TestCase):
    def test_vertical_input_keeps_horizontal_facing(self):
        state = GameState()
        process_event(state, key_event(PICO.SDL_KEYDOWN, PICO.SDLK_LEFT), PICO)
        process_event(state, key_event(PICO.SDL_KEYDOWN, PICO.SDLK_UP), PICO)
        self.assertEqual(state.facing, "left")
        self.assertEqual(state.pressed, {"left", "up"})

    def test_releasing_one_key_keeps_the_other_pressed(self):
        state = GameState()
        for key in (PICO.SDLK_RIGHT, PICO.SDLK_DOWN):
            process_event(state, key_event(PICO.SDL_KEYDOWN, key), PICO)
        process_event(state, key_event(PICO.SDL_KEYUP, PICO.SDLK_RIGHT), PICO)
        self.assertEqual(state.pressed, {"down"})

    def test_escape_and_window_close_stop_the_game(self):
        state = GameState()
        process_event(state, key_event(PICO.SDL_KEYDOWN, PICO.SDLK_ESCAPE), PICO)
        self.assertFalse(state.running)
        state = GameState()
        process_event(state, SimpleNamespace(type=PICO.SDL_QUIT), PICO)
        self.assertFalse(state.running)


class MovementTests(unittest.TestCase):
    def test_diagonal_distance_matches_straight_speed(self):
        state = GameState(pressed={"right", "up"})
        start_x, start_y = state.x, state.y
        update(state, 0.5)
        self.assertAlmostEqual(hypot(state.x - start_x, state.y - start_y), MOVE_SPEED * 0.5)

    def test_boundaries_hold_full_sprite_inside_canvas(self):
        state = GameState(x=CANVAS_WIDTH / 2, y=CANVAS_HEIGHT / 2, pressed={"right", "up"})
        update(state, 10)
        self.assertEqual(state.x, CANVAS_WIDTH - SPRITE_SIZE / 2)
        self.assertEqual(state.y, CANVAS_HEIGHT - SPRITE_SIZE / 2)
        update(state, 0.1)
        self.assertFalse(state.moving)
        state.pressed = {"left", "down"}
        update(state, 10)
        self.assertEqual(state.x, SPRITE_SIZE / 2)
        self.assertEqual(state.y, SPRITE_SIZE / 2)

    def test_idle_animation_continues_and_resets_after_movement(self):
        state = GameState()
        update(state, 0.11)
        self.assertEqual(state.frame, 1)
        self.assertFalse(state.moving)
        state.pressed.add("right")
        update(state, 0.01)
        self.assertEqual(state.frame, 0)
        self.assertTrue(state.moving)
        state.pressed.clear()
        update(state, 0.01)
        self.assertEqual(state.frame, 0)
        self.assertFalse(state.moving)


if __name__ == "__main__":
    unittest.main()
