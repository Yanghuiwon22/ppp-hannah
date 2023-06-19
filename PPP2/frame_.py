import PySimpleGUI as sg
import pygame as py

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
    # field_1_size = field_1.get_rect().size  # 이미지의 크기를 구해옴

    field_1_list = []
    field_y_pos = 500

    for i in range(3):  # y축으로 3번 반복
        field_y_pos += 70
        field_x_pos = -30

        for j in range(5):  # x축으로 5번 반복
            field_x_pos += 70
            screen.blit(field_1, (field_x_pos, field_y_pos))  # field_1 설정

            field_1_list.append((field_x_pos, field_y_pos))

    return field_1_list

def fence_set(store_y_pos):
    fence_setting = py.image.load("_fence.png")
    fence_setting_size = fence_setting.get_rect().size

    fence_set_x_pos = 0
    fence_set_y_pos = store_y_pos - fence_setting_size[1]

    for i in range(15):
        screen.blit(fence_setting, (fence_set_x_pos, fence_set_y_pos))
        fence_set_x_pos += fence_setting_size[0]
        print(i)

def store_gui():
    row0 = [sg.Text("물뿌리개")]
    row1 = [sg.Image(filename="_rice.png", size=(70,70)), sg.Text("벼"), sg.Button("구매"), sg.Button("판매")]
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
    row0 = [sg.Button("물뿌리개")]
    row1 = [sg.Image(filename="_wateringcan_1.png", size=(70, 70)), sg.Text("플라스틱으로 만든 \n 기본적인 물뿌리개이다."), sg.Button("구매"), sg.Button("판매")]
    row2 = [sg.Image(filename="_spary.png"), sg.Text("콩"), sg.Button("구매"), sg.Button("판매")]
    row3 = [sg.Image(filename="_wateringcan.png"), sg.Text("옥수수"), sg.Button("구매"), sg.Button("판매")]
    row4 = [sg.Image(filename="_pumkin.png", size=(70, 70)), sg.Text("호박"), sg.Button("구매"), sg.Button("판매")]
    row5 = [sg.Image(filename="_eggplant.png", size=(70, 70)), sg.Text("가지"), sg.Button("구매"), sg.Button("판매")]

    layout = [[row0, row1],
              [row2, row3, row4, row5]
              ]
    window = sg.Window("대장간", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

    window.close()

def fence():
    pass

def main():
    # 캐릭터(스프라이트) 불러오기
    character = py.image.load("_character.png")
    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    print(character_size)
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

    # 상점 세팅
    store_setting = py.image.load("_store.png")
    store_setting_size = store_setting.get_rect().size  # 이미지의 크기를 구해옴

    store_x_pos = int(40)
    store_y_pos = int(200)

    # 대장간 세팅
    forge_setting = py.image.load("_forge.png")
    forge_setting_size = forge_setting.get_rect().size

    forge_x_pos = 170
    forge_y_pos = 200

    # 가방 세팅
    bag_setting = py.image.load("_bag.png")
    bag_setting_size = bag_setting.get_rect().size

    bag_x_pos = screen_width - bag_setting_size[0]
    bag_y_pos = screen_height - bag_setting_size[1]

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

            if event.type == py.KEYDOWN: # 키가 눌러졌는지 확인
                if event.key == py.K_LEFT:
                    to_x -= character_speed
                elif event.key == py.K_RIGHT:
                    to_x += character_speed
                elif event.key == py.K_UP:
                    to_y -= character_speed
                elif event.key == py.K_DOWN:
                    to_y += character_speed


            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    to_x = 0
                elif event.key == py.K_UP or event.key == py.K_DOWN:
                    to_y = 0

        character_x_pos += to_x
        character_y_pos += to_y

        # print(character_x_pos, character_y_pos)

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

        screen.blit(background, (0,0)) # 배경 그리기 -> (0,0) 창에 완벽하게 맞게 설정
        screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 위치 설정
        field_set() # 밭 15개 기본 위치 설정
        screen.blit(store_setting, (store_x_pos, store_y_pos))  # 상점 위치 설정
        screen.blit(forge_setting, (forge_x_pos, forge_y_pos))  # 대장간 위치 설정
        screen.blit(bag_setting, (bag_x_pos, bag_y_pos)) # 가방 위치 설정

        # 상점 접근시 gui창 띄우기ㅁ
        if store_x_pos < character_x_pos < store_x_pos + store_setting_size[0] and store_y_pos < character_y_pos < store_y_pos + store_setting_size[1]:
            store_gui()
            character_y_pos += 2

        # 대장간 접근시 gui창 띄우기
        if forge_x_pos < character_x_pos < forge_x_pos + forge_setting_size[0] and forge_y_pos < character_y_pos < forge_y_pos + forge_setting_size[1]:
            forge_gui()
            character_y_pos += 2

        py.display.update() # 게임화면을 다시 그리기

    py.quit() # pygame 종료

if __name__=="__main__":
    main()