"""Drill #9: 방향키로 움직이는 소년."""

from pathlib import Path
from dataclasses import dataclass


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
ASSET_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 100


@dataclass
class GameState:
    x: float = CANVAS_WIDTH / 2
    y: float = CANVAS_HEIGHT / 2


def main():
    import pico2d as pico

    pico.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        state = GameState()
        background = pico.load_image(str(ASSET_DIR / "TUK_GROUND.png"))
        character = pico.load_image(str(ASSET_DIR / "animation_sheet.png"))
        pico.clear_canvas()
        background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        character.clip_draw(0, 300, SPRITE_SIZE, SPRITE_SIZE, state.x, state.y)
        pico.update_canvas()
    finally:
        pico.close_canvas()


if __name__ == "__main__":
    main()
