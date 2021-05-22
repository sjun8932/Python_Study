import pygame

pygame.init() #초기화 (파이게임 임포트 하자마자 해야합니다. 필수 작업 *^^*)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Programming/Python/PythonWospace/pygame_basic/background.png")



#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0,0,255)) # 이렇게 해도 되고 아래 주석대로 해도 된다.
    screen.blit(background, (0, 0)) # 배경 그기기

    pygame.display.update() # 게임 화면을 다시 그리기!!!
    # 파이게임에서는 매 프레임마다 화면을 새로 그려주는 동작을 해야한다.

# pygmae 종료
pygame.quit()