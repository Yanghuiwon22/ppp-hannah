import pygame as py

py.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = py.display.set_mode( (screen_width, screen_height) )

# 화면 타이틀 설정
py.display.set_caption("Hannah Farm") # 게임 이름 설정

# 배경 이미지 불러오기
background = py.image.load("C:\code\ppp-main\PPP_progect\_background.png")



def main():
    # 캐릭터(스프라이트) 불러오기
    character = py.image.load("C:\code\ppp-main\PPP_progect\_character.png")
    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 이동할 좌표
    to_x = 0
    to_y = 0

    # 이벤트 루프
    running = True
    while running:
        for event in py.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == py.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                running = False  # 게임이 진행중이 아님

            if event.type == py.KEYDOWN: # 키가 눌러졌는지 확인
                if event.key == py.K_LEFT:
                    to_x -= 0.5
                elif event.key == py.K_RIGHT:
                    to_x += 0.5
                elif event.key == py.K_UP:
                    to_y -= 0.5
                elif event.key == py.K_DOWN:
                    to_y += 0.5

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or py.K_RIGHT:
                    to_x = 0
                elif event.key == py.K_UP or py.K_DOWN:
                    to_y = 0

        character_x_pos += to_x
        character_y_pos += to_y





        # screen.fill((0,0,255))
        screen.blit(background, (0,0)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정
        screen.blit(character, (character_x_pos,character_y_pos)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정




        py.display.update() # 게임화면을 다시 그리기




    # pygame 종료
    py.quit()


if __name__=="__main__":
    main()