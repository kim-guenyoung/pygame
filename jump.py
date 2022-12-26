import pygame
import random

pygame.init() #초기화 작업(필수)

#화면 크기 설정
screen_width = 800 #가로 크기
screen_height = 600 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정(게임 화면) 어떻게 글자를 표시할 지
pygame.display.set_caption("STACK") #게임 이름 : STACK

add_hole = pygame.USEREVENT + 1
pygame.time.set_timer(add_hole, 250)

add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)



holes = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player_lives = 1

while(player_lives > 0):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player_lives = player_lives - 1
#배경이미지 불러오기
background = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/blue_block.png")
character_size = character.get_rect().size #rectangle의 약자/ 이미지의 크기
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_y_pos = screen_height - character_height #화면 세로크기의 가장 위쪽 부분에 위치하게 함
#빼주는 게 640의 픽셀에서 그 캐릭터의 키(좌표)를 빼주어야 하니까(그래야 정중앙에 위치함)

#이동할 좌표
to_x = 0
to_y = 0

#위에서 떨어질 블록 코드
block = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/green_block.png")
block_size = block.get_rect().size
block_width = block_size[0]
block_height = block_size[1]
block_x_pos = 0
block_y_pos = 0
block_speed = 20

#이벤트 루프
running = True #게임이 진행되는지 확인
while running:
    for event in pygame.event.get(): #계속 돌면서 
        if event.type == pygame.QUIT: #창을 닫을 때
            running = False #false가 되니까 while문 탈출해서 파이게임 종료
   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 0.1
            elif event.key == pygame.K_RIGHT:
                to_x += 0.1
            elif event.key == pygame.K_SPACE:
                to_y == 400
            # elif event.key == pygame.K_UP:
            #     to_y -= 0.1
            # elif event.key == pygame.K_DOWN:
            #     to_y += 0.1
        
        if event.type == pygame.KEYUP: #손에서 방향키를 뗐을 때
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0

            
    block_x_pos += to_x
    block_y_pos += to_y

#가로 화면 안에만 있게
    if character_x_pos < 0: #화면 밖으로 나가면 벽에서 멈추게
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


#세로 화면 안에만 있게
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

   
    #화면에 그리기
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(block, (block_x_pos, block_y_pos))
    pygame.display.update() #while문 계속 돌면서 화면 계속해서 업데이트


#pygame 종료
pygame.quit()