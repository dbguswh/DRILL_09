"""Drill #9: 방향키로 움직이는 소년."""

from pathlib import Path


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
ASSET_DIR = Path(__file__).resolve().parent


def main():
    import pico2d as pico

    pico.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        background = pico.load_image(str(ASSET_DIR / "TUK_GROUND.png"))
        pico.clear_canvas()
        background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        pico.update_canvas()
    finally:
        pico.close_canvas()


if __name__ == "__main__":
    main()
