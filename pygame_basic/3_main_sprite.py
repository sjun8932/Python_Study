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

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("C:/Programming/Python/PythonWospace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width /2 - character_width/2 # 화면 가로의 절반 크기 (가로 위치)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로위치)




#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0,0,255)) # 이렇게 해도 되고 아래 주석대로 해도 된다.
    screen.blit(background, (0, 0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기





    pygame.display.update() # 게임 화면을 다시 그리기!!!
    # 파이게임에서는 매 프레임마다 화면을 새로 그려주는 동작을 해야한다.

# pygmae 종료
pygame.quit()