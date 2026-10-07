"""Drill #9: 방향키로 움직이는 소년."""


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024


def main():
    import pico2d as pico

    pico.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        pico.clear_canvas()
        pico.update_canvas()
    finally:
        pico.close_canvas()


if __name__ == "__main__":
    main()
