import pygame

pygame.init() #초기화 작업(필수)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정(게임 화면) 어떻게 글자를 표시할 지
pygame.display.set_caption("STACK") #게임 이름 : STACK


#배경이미지 불러오기
background = pygame.image.load("C:/Users/김근영/Desktop/pygame/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/김근영/Desktop/pygame/pygame_basic/character.png")
character_size = character.get_rect().size #rectangle의 약자/ 이미지의 크기
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치하게 함
character_y_pos = screen_height - character_height #화면 세로크기의 가장 위쪽 부분에 위치하게 함
#빼주는 게 640의 픽셀에서 그 캐릭터의 키(좌표)를 빼주어야 하니까(그래야 정중앙에 위치함)



#이벤트 루프
running = True #게임이 진행되는지 확인
while running:
    for event in pygame.event.get(): #계속 돌면서 
        if event.type == pygame.QUIT: #창을 닫을 때
            running = False #false가 되니까 while문 탈출해서 파이게임 종료
    
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() #while문 계속 돌면서 화면 계속해서 업데이트


#pygame 종료
pygame.quit()