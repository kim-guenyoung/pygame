import pygame

pygame.init() #초기화 작업(필수)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정(게임 화면) 어떻게 글자를 표시할 지
pygame.display.set_caption("STACK") #게임 이름 : STACK

#FPS
clock = pygame.time.Clock()



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


#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 1

#이벤트 루프
running = True #게임이 진행되는지 확인
while running:
    dt = clock.tick(60) #게임화면 초당 프레임횟수 (클수록 빠름)

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): #계속 돌면서 
        if event.type == pygame.QUIT: #창을 닫을 때
            running = False #false가 되니까 while문 탈출해서 파이게임 종료
    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: #손에서 방향키를 뗐을 때
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0

            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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


    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() #while문 계속 돌면서 화면 계속해서 업데이트


#pygame 종료
pygame.quit()