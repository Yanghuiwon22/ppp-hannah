import pygame
import time

# Pygame 초기화
pygame.init()

# 게임 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이미지 변경 게임")

# 이미지 로드
image1 = pygame.image.load("_store.png")
image2 = pygame.image.load("_forge.png")

# 이미지 초기 위치 설정
image_x = 0
image_y = 0

# 이전 이미지 변경 시간
last_image_change_time = time.time()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 로직
    current_time = time.time()
    if current_time - last_image_change_time >= 5:
        # 이미지 변경
        if image_x == 0:
            image_x = screen_width - image1.get_width()
            image = image2
        else:
            image_x = 0
            image = image1

        last_image_change_time = current_time

    # 화면 그리기
    screen.fill((0, 0, 0))  # 검은색 배경
    screen.blit(image, (image_x, image_y))

    # 화면 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()