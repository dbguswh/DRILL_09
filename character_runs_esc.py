from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# fill here

running = True #함수 안에서 만든 running은 지역변수이므로 바깥 running을 사용하기 위해 global 사용
x = 800 // 2

def handle_events(): #이벤트 처리
    # fill here

    global running #바깥에 정의가 되어있는 running을 사용하겠다
    global dir
    events = get_events() #list

    for event in events: #이벤트가 여러개 들어있음
        if event.type== SDL_QUIT: #이벤트 타입
            running = False 
        
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


frame = 0
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    # fill here
    handle_events()

    if not running:
        break


    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)


close_canvas()
