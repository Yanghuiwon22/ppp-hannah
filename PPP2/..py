import pygame

# pygame 초기화
pygame.init()

# 창의 너비와 높이 설정
width, height = 800, 600

# 창 생성
window = pygame.display.set_mode((width, height))
sub_window = pygame.Surface((width // 2, height // 2))  # 부분 창 생성

# 창의 제목 설정
pygame.display.set_caption("Pygame 창")

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 부분 창 그리기
    sub_window.fill((255, 255, 255))  # 부분 창 배경을 흰색으로 설정
    pygame.draw.rect(sub_window, (0, 0, 255), (50, 50, 200, 100))  # 사각형 그리기

    # 부분 창을 메인 창에 그리기
    window.blit(sub_window, (width // 4, height // 4))

    # 화면 업데이트
    pygame.display.flip()

# pygame 종료
pygame.quit()