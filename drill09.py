"""Drill #9: 방향키로 움직이는 소년."""

from pathlib import Path
from dataclasses import dataclass, field


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
ASSET_DIR = Path(__file__).resolve().parent
SPRITE_SIZE = 100
MOVE_STEP = 5
SPRITE_ROWS = {
    ("left", True): 0,
    ("right", True): 1,
    ("left", False): 2,
    ("right", False): 3,
}


@dataclass
class GameState:
    x: float = CANVAS_WIDTH / 2
    y: float = CANVAS_HEIGHT / 2
    running: bool = True
    pressed: set[str] = field(default_factory=set)
    facing: str = "right"
    moving: bool = False


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
        direction = arrow_keys[event.key]
        state.pressed.add(direction)
        if direction in ("left", "right"):
            state.facing = direction
    elif event.type == pico.SDL_KEYUP and event.key in arrow_keys:
        state.pressed.discard(arrow_keys[event.key])


def update(state):
    dx = int("right" in state.pressed) - int("left" in state.pressed)
    dy = int("up" in state.pressed) - int("down" in state.pressed)
    state.x += dx * MOVE_STEP
    state.y += dy * MOVE_STEP
    state.moving = bool(dx or dy)


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

            update(state)
            pico.clear_canvas()
            background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            row = SPRITE_ROWS[(state.facing, state.moving)]
            character.clip_draw(0, row * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE, state.x, state.y)
            pico.update_canvas()
            pico.delay(1 / 60)
    finally:
        pico.close_canvas()


if __name__ == "__main__":
    main()
