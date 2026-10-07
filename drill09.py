"""Drill #9: 방향키로 움직이는 소년."""

from pathlib import Path
from dataclasses import dataclass, field


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
ASSET_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 100


@dataclass
class GameState:
    x: float = CANVAS_WIDTH / 2
    y: float = CANVAS_HEIGHT / 2
    running: bool = True
    pressed: set[str] = field(default_factory=set)


def process_event(state, event, pico):
    arrow_keys = {
        pico.SDLK_LEFT: "left",
        pico.SDLK_RIGHT: "right",
        pico.SDLK_UP: "up",
        pico.SDLK_DOWN: "down",
    }
    if event.type == pico.SDL_QUIT:
        state.running = False
    elif event.type == pico.SDL_KEYDOWN and event.key == pico.SDLK_ESCAPE:
        state.running = False
    elif event.type == pico.SDL_KEYDOWN and event.key in arrow_keys:
        state.pressed.add(arrow_keys[event.key])


def main():
    import pico2d as pico

    pico.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        state = GameState()
        background = pico.load_image(str(ASSET_DIR / "TUK_GROUND.png"))
        character = pico.load_image(str(ASSET_DIR / "animation_sheet.png"))
        while state.running:
            for event in pico.get_events():
                process_event(state, event, pico)
            if not state.running:
                break

            pico.clear_canvas()
            background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            character.clip_draw(0, 300, SPRITE_SIZE, SPRITE_SIZE, state.x, state.y)
            pico.update_canvas()
            pico.delay(1 / 60)
    finally:
        pico.close_canvas()


if __name__ == "__main__":
    main()
