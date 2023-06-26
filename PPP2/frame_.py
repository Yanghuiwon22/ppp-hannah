import PySimpleGUI as sg
import pygame as py
import pyautogui as pa
import tkinter as tk

py.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1000 # 가로 크기
screen_height = 800 # 세로 크기
screen = py.display.set_mode( (screen_width, screen_height) )

# 화면 타이틀 설정
py.display.set_caption("Hannah Farm") # 게임 이름 설정

# FPS
clock = py.time.Clock()

# 배경 이미지 불러오기
background = py.image.load("_background.png")

def field_set():
    field_1 = py.image.load("gross_.png")
    field_1_size = field_1.get_rect().size  # 이미지의 크기를 구해옴

    field_1_list = []
    field_y_pos = 500

    for i in range(3):  # y축으로 3번 반복
        field_y_pos += 70
        field_x_pos = -30

        for j in range(5):  # x축으로 5번 반복
            field_x_pos += 70
            screen.blit(field_1, (field_x_pos, field_y_pos))  # field_1 설정

            field_1_list.append((field_x_pos, field_y_pos))

            field_rect = field_1.get_rect()
            field_rect.topleft = (field_x_pos, field_y_pos)

    return field_1_list

def fence_set():
    fence_setting = py.image.load("_yellow.png")
    fence_setting_size = fence_setting.get_rect().size
    fence_width = fence_setting_size[0]
    fence_height = fence_setting_size[1]
    fence_x_pos = 0
    fence_y_pos = 450 - 80

    while fence_x_pos < 460:
        if fence_x_pos == int(240) and fence_x_pos == int(270):
            fence_x_pos += 10
        else:
            screen.blit(fence_setting, (fence_x_pos, fence_y_pos))
            fence_x_pos += 10

    fence_x_pos = 450
    while fence_y_pos < 1000:
        screen.blit(fence_setting, (fence_x_pos, fence_y_pos))
        fence_y_pos += 10

def buy_rice():
    print("쌀을 구매하였습니다")

def store_gui():
    row0 = [sg.Text("농작물")]
    row1 = [sg.Image(filename="_rice.png", size=(70,70)), sg.Text("벼"), sg.Button("구매"), sg.Button("판매") ]
    row2 = [sg.Image(filename="_bean.png", size=(70,70)), sg.Text("콩"), sg.Button("구매"), sg.Button("판매")]
    row3 = [sg.Image(filename="_corn.png", size=(70,70)), sg.Text("옥수수"), sg.Button("구매"), sg.Button("판매")]
    row4 = [sg.Image(filename="_pumkin.png", size=(70,70)), sg.Text("호박"), sg.Button("구매"), sg.Button("판매")]
    row5 = [sg.Image(filename="_eggplant.png", size=(70,70)), sg.Text("가지"), sg.Button("구매"), sg.Button("판매")]

    layout = [ [row0, row1],
               [row2, row3, row4, row5]
               ]
    window = sg.Window("상점", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

    window.close()

def forge_gui():
    row0 = [sg.Button("도구")]
    row1 = [sg.Image(filename="_wateringcan_1.png", size=(70, 70)), sg.Text("플라스틱으로 만든 \n 기본적인 물뿌리개이다."), sg.Button("구매", key='--RICE--')]
    row2 = [sg.Image(filename="_spary.png"), sg.Text("분무기"), sg.Button("구매")]
    row3 = [sg.Image(filename="_wateringcan.png"), sg.Text("좋은 물뿌리개"), sg.Button("구매"),]


    layout = [[row0, row1, row2, row3]
              ]
    window = sg.Window("대장간", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event.key == "--RICE--":
            print("쌀을 구매하였습니다.")


    window.close()

def bag_gui():
    row1 = [sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png")]
    # row1_1 = [sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수")]
    row2 = [sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png")]
    # row2_1 = [sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수")]
    row3 = [sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png")]
    # row3_1 = [sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수")]
    row4 = [sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png")]
    # row4_1 = [sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수")]
    row5 = [sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png"), sg.Image(filename="_bag_set.png")]
    # row5_1 = [sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수"), sg.Text("갯수")]

    layout = [[ row1, row2, row3, row4, row5]]
    window = sg.Window("가방", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
    window.close()


def bean_farming(start_time):
    # 농작물 자라기 세팅

    print("bean_farming 실행중입니다")
    bean_b = py.image.load("_bean_b.png")
    bean = py.image.load("_bean_1.png")

    current_time = py.time.get_ticks()
    elapsed_time = current_time - start_time

    if elapsed_time >= 5000:
        screen.blit(bean, field_set()[0])
    else:
        screen.blit(bean_b, field_set()[0])

def main():

    # 캐릭터(스프라이트) 불러오기
    character = py.image.load("_character.png")
    character_size = character.get_rect().size  # 이미지의 크기를 구해옴

    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = 50  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = 480  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 상점 세팅
    store_setting = py.image.load("_store.png")
    store_setting_size = store_setting.get_rect().size  # 이미지의 크기를 구해옴

    store_x_pos = int(40)
    store_y_pos = int(100)

    # 대장간 세팅
    forge_setting = py.image.load("_forge.png")
    forge_setting_size = forge_setting.get_rect().size

    forge_x_pos = 170
    forge_y_pos = store_y_pos

    # 집 세팅
    house_setting = py.image.load("_house.png")
    house_setting_size = house_setting.get_rect().size
    house_width = house_setting_size[0]
    house_height = house_setting_size[1]

    house_x_pos = 40
    house_y_pos = 400

    # 가방 세팅
    bag_setting = py.image.load("_bag.png")
    bag_setting_size = bag_setting.get_rect().size
    bag_width = bag_setting_size[0]
    bag_height = bag_setting_size[1]

    bag_x_pos = screen_width - bag_setting_size[0]
    bag_y_pos = screen_height - bag_setting_size[1]

    bag_rect = bag_setting.get_rect()
    bag_rect.topleft = (bag_x_pos, bag_y_pos)

    # 밭 세팅
    field_1 = py.image.load("gross_.png")
    field_1_size = field_1.get_rect().size  # 이미지의 크기를 구해옴
    field_set_rect = field_1.get_rect()

    field_set_1_rect = field_1.get_rect()
    field_set_1_rect.topleft = field_set()[0]

    field_set_2_rect = field_1.get_rect()
    field_set_2_rect.topleft = (field_set()[1])

    field_set_3_rect = field_1.get_rect()
    field_set_3_rect.topleft = (field_set()[2])

    field_set_4_rect = field_1.get_rect()
    field_set_4_rect.topleft = (field_set()[3])

    field_set_5_rect = field_1.get_rect()
    field_set_5_rect.topleft = (field_set()[4])

    field_set_6_rect = field_1.get_rect()
    field_set_6_rect.topleft = (field_set()[5])

    field_set_7_rect = field_1.get_rect()
    field_set_7_rect.topleft = (field_set()[6])

    field_set_8_rect = field_1.get_rect()
    field_set_8_rect.topleft = (field_set()[7])

    field_set_9_rect = field_1.get_rect()
    field_set_9_rect.topleft = (field_set()[8])

    field_set_10_rect = field_1.get_rect()
    field_set_10_rect.topleft = (field_set()[9])

    field_set_11_rect = field_1.get_rect()
    field_set_11_rect.topleft = (field_set()[10])

    field_set_12_rect = field_1.get_rect()
    field_set_12_rect.topleft = (field_set()[11])

    field_set_13_rect = field_1.get_rect()
    field_set_13_rect.topleft = (field_set()[12])

    field_set_14_rect = field_1.get_rect()
    field_set_14_rect.topleft = (field_set()[13])

    field_set_15_rect = field_1.get_rect()
    field_set_15_rect.topleft = (field_set()[14])


    # 울타리 세팅
    fence_setting = py.image.load("_yellow.png")
    fence_setting_size = fence_setting.get_rect().size
    fence_width = fence_setting_size[0]
    fence_height = fence_setting_size[1]
    fence_x_pos = 0
    fence_y_pos = 450-80

    # 농작물 자라기 세팅
    bean_b = py.image.load("_bean_b.png")
    bean = py.image.load("_bean.png")
    bean_s = bean_b

    start_time = 0

    # 이동할 좌표
    to_x = 0
    to_y = 0

    # 이동 속도
    character_speed = 3

    # 이벤트 루프
    running = True
    while running:

        dt = clock.tick(60)


        for event in py.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == py.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                running = False  # 게임이 진행중이 아님

            # 마우스 상대위치 설정
            # mouse_positon = py.mouse.get_pos()

            if event.type == py.KEYDOWN: # 키가 눌러졌는지 확인
                if event.key == py.K_LEFT:
                    to_x -= character_speed
                elif event.key == py.K_RIGHT:
                    to_x += character_speed
                elif event.key == py.K_UP:
                    to_y -= character_speed
                elif event.key == py.K_DOWN:
                    to_y += character_speed

            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                if bag_rect.collidepoint(event.pos):
                    start_time = py.time.get_ticks()
                    bag_gui()
                    print("가방을 클릭")

                elif field_set_1_rect.collidepoint(event.pos):
                    print("1번 농지를 클릭")
                    bean_farming(start_time)
                    screen.blit(bean_s, (field_set())[0])  # 집 위치 설정

                    print("수확하세요")

                elif field_set_2_rect.collidepoint(event.pos):
                    print("2번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_3_rect.collidepoint(event.pos):
                    print("3번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_4_rect.collidepoint(event.pos):
                    print("4번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")


                elif field_set_5_rect.collidepoint(event.pos):
                    print("5번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_6_rect.collidepoint(event.pos):
                    print("6번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_7_rect.collidepoint(event.pos):
                    print("7번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_8_rect.collidepoint(event.pos):
                    print("8번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_9_rect.collidepoint(event.pos):
                    print("9번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_10_rect.collidepoint(event.pos):
                    print("10번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_11_rect.collidepoint(event.pos):
                    print("11번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_12_rect.collidepoint(event.pos):
                    print("12번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_13_rect.collidepoint(event.pos):
                    print("13번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_14_rect.collidepoint(event.pos):
                    print("14번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")

                elif field_set_15_rect.collidepoint(event.pos):
                    print("15번 농지를 클릭")
                    bean_farming(start_time)
                    print("수확하세요")



                # if bag_x_pos < mouse_positon[0] < bag_x_pos + bag_width and bag_y_pos < mouse_positon[1] < bag_y_pos + bag_height:

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    to_x = 0
                elif event.key == py.K_UP or event.key == py.K_DOWN:
                    to_y = 0

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width-character_width:
            character_x_pos = screen_width-character_width
        # 세로 경계값 처리
        elif character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        if 0 < character_x_pos < 450 - 30 and 450-80 + 30 < character_y_pos < 1000:
            # print("농장 작업 가능")
            pass

        screen.blit(background, (0,0)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정
        screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 위치 설정
        field_set() # 밭 15개 기본 위치 설정
        screen.blit(store_setting, (store_x_pos, store_y_pos))  # 상점 위치 설정
        screen.blit(forge_setting, (forge_x_pos, forge_y_pos))  # 대장간 위치 설정
        screen.blit(bag_setting, (bag_x_pos, bag_y_pos)) # 가방 위치 설정
        screen.blit(house_setting, (house_x_pos, house_y_pos)) # 집 위치 설정
        fence_set() # 울타리 설치

        # 상점 접근시 gui창 띄우기
        if store_x_pos < character_x_pos < store_x_pos + store_setting_size[0] and store_y_pos < character_y_pos < store_y_pos + store_setting_size[1]:
            store_gui()
            character_y_pos += 5

        # 대장간 접근시 gui창 띄우기
        if forge_x_pos < character_x_pos < forge_x_pos + forge_setting_size[0] and forge_y_pos < character_y_pos < forge_y_pos + forge_setting_size[1]:
            forge_gui()
            character_y_pos += 5

        character_x_pos += to_x
        character_y_pos += to_y

        # print(character_x_pos, character_y_pos)

        # 가로 경계값 처리


        # (콩) 농사



        py.display.update() # 게임화면을 다시 그리

    py.quit() # pygame 종료

if __name__=="__main__":
    main()