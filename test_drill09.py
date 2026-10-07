"""Drill #9 입력과 이동 상태를 확인한다."""

import unittest
from types import SimpleNamespace

from drill09 import GameState, process_event


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


if __name__ == "__main__":
    unittest.main()
