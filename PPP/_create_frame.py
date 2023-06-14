import PySimpleGUI as sg
import pygame as py

py.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1000 # 가로 크기
screen_height = 800 # 세로 크기
screen = py.display.set_mode( (screen_width, screen_height) )

# 화면 타이틀 설정
py.display.set_caption("Hannah Farm") # 게임 이름 설정

# 배경 이미지 불러오기
background = py.image.load("_background.png")

def f_field_position(field_position, field_position_x_pos, field_position_y_pos):
    for i in range(3):
        field_x = []
        field_y = []

        field_position_y_pos -= 100
        field_position_x_pos = 30
        for i in range(5):
            screen.blit(field_position, (field_position_x_pos, field_position_y_pos))
            field_x.append(field_position_x_pos)# field_1 위치 설정
            field_y.append(field_position_y_pos)# field_1 위치 설정
            field_position_x_pos += 100

def main():
    # 캐릭터(스프라이트) 불러오기
    character = py.image.load("_character.png")
    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    print(character_size)
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 밭_위치 지정 이미지 생성하기
    field_position = py.image.load("_field_position.png")
    field_position_size = field_position.get_rect().size  # 이미지의 크기를 구해옴
    field_position_width = field_position_size[0]  # 캐릭터의 가로 크기
    field_position_height = field_position_size[1]  # 캐릭터의 세로 크기
    field_position_x_pos = 30
    field_position_y_pos = screen_height - field_position_height - 30

    # 밭_1 이미지 생성하기
    field_1 = py.image.load("_field_1.jpg")
    field_1_size = field_1.get_rect().size  # 이미지의 크기를 구해옴
    print(field_1_size)
    field_1_width = field_1_size[0]  # 캐릭터의 가로 크기
    field_1_height = field_1_size[1]  # 캐릭터의 세로 크기
    field_1_x_pos = 0  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    field_1_y_pos = 0  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 밭_2 이미지 생성하기
    field_2 = py.image.load("_field_2.jpg")
    field_2_size = field_2.get_rect().size  # 이미지의 크기를 구해옴
    print(field_2_size)
    field_2_width = field_2_size[0]  # 캐릭터의 가로 크기
    field_2_height = field_2_size[1]  # 캐릭터의 세로 크기
    field_2_x_pos = 0  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    field_2_y_pos = 0  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 상점 이미지 생성하기
    store = py.image.load("_store.png")
    store_size = store.get_rect().size  # 이미지의 크기를 구해옴
    store_width = store_size[0]  # 캐릭터의 가로 크기
    store_height = store_size[1]  # 캐릭터의 세로 크기
    store_x_pos = screen_width - store_width - 70  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    store_y_pos = +70   # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 우물 이미지 생성하기
    well = py.image.load("_well.jpg")
    well_size = well.get_rect().size  # 이미지의 크기를 구해옴
    well_width = well_size[0]  # 캐릭터의 가로 크기
    well_height = well_size[1]  # 캐릭터의 세로 크기
    well_x_pos = 70  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    well_y_pos = +70  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

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
                    to_x -= 0.3
                elif event.key == py.K_RIGHT:
                    to_x += 0.3
                elif event.key == py.K_UP:
                    to_y -= 0.3
                elif event.key == py.K_DOWN:
                    to_y += 0.3

                elif event.key == py.K_p: # 밭 위치 설정
                    field_1_x_pos = character_x_pos
                    field_1_y_pos = character_y_pos

                elif event.key == py.MOUSEBUTTONDOWN:
                    print("구매하시겠습니까?")

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    to_x = 0
                elif event.key == py.K_UP or event.key == py.K_DOWN:
                    to_y = 0





            if event.type == py.KEYDOWN:  # 밭 위치 설정
                    if event.key == py.K_o:
                        field_2_x_pos = character_x_pos
                        field_2_y_pos = character_y_pos




        character_x_pos += to_x
        character_y_pos += to_y



        # 제가 직접 짠 부분 ( 화면 밖으로 캐릭터가 나가지 않도록 설정 )
        # 가로 경계값 처리
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width-character_width:
            character_x_pos = screen_width-character_width
        # 세로 경계값 처리
        elif character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        # 밭 고정 시키고 새로운 밭 생성하기

        # screen.fill((0,0,255))
        screen.blit(background, (0,0)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정
        screen.blit(character, (character_x_pos,character_y_pos)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정
        screen.blit(field_1, (field_1_x_pos, field_1_y_pos)) # field_1 설정
        screen.blit(field_2, (field_2_x_pos, field_2_y_pos)) # field_2 위치 설정
        f_field_position(field_position,field_position_x_pos,field_position_y_pos) #  밭 생성하기 (x5)
        screen.blit(store, (store_x_pos, store_y_pos)) # store 위치 설정
        screen.blit(well, (well_x_pos, well_y_pos)) # well 위치 설정





        py.display.update() # 게임화면을 다시 그리기

    # pygame 종료
    py.quit()


if __name__=="__main__":
    main()