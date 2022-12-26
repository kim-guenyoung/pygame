
import pygame
import sys
import time
import random


jump = True
clock = pygame.time.Clock()
obstacles = pygame.sprite.Group()

# pygame.mixer.init()
# pygame.mixer.music.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/둘리.wav")
# pygame.mixer.music.play()

# 초기화
pygame.init()

screen_width = 640
screen_height = 400 

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("냥떠러지")
my_color = (153, 217, 234)
pygame.key.set.repeat(15, 15)

big_font = pygame.font.SysFont(None, 80)
small_font = pygame.font.SysFont(None, 40)

character = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/cat1-1.png")
#character2 = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/cat2-1.png")

character_size = character.get_rect().size #rectangle의 약자/ 이미지의 크기
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기



black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
brown = (185, 122, 87)

#수정
green = (0, 200, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)




pygame.display.update()   
pygame.display.flip()


def introbackground():
    screen.blit(pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/intro.jpg"), (0, 0))

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def button(txt, x, y, w, h, ic, ac, action = None): #버튼 함수 정의
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ic, (x, y, w, h))
        
        
        if click == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click == 1 and action != None:
            
            action()
        
    smallText = pygame.font.SysFont("malgungothic", 20)
    textSurf, textRect = text_objects(txt, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def restart_game():
    global game_over, score
    game_over = False
    obstacles.empty()
    score = 0
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/둘리.wav")
    pygame.mixer.music.play()
    pygame.display.flip()

def quitgame():
    pygame.quit()
    sys.exit()

def introScreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()


        screen.fill(white)
        introbackground()

        largeText = pygame.font.SysFont("malgungothic", 50)
        TextSurf, TextRect = text_objects("냥떠러지", largeText)

        TextRect.center = ((screen_width/2), (screen_height/4))
        screen.blit(TextSurf, TextRect)

        # button("시작", 150, 300, 80, 30, green, orange, restart_game)
        # button("종료", 400, 300, 80, 30, red, orange, quitgame)

        button("시작", 150, 300, 80, 30, green, orange, restart_game)
        button("종료", 400, 300, 80, 30, red, orange, quitgame)

        pygame.display.update()
        clock.tick(15)
    

introScreen()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width,height), pygame.SRCALPHA).convert_alpha()
       
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.vel = 5
        self.rect.x = screen_width #오른쪽에서 플레이어쪽으로 이동합니다.
        self.rect.y = screen_height - self.rect.height

    def update(self):
        self.rect.x -= int(self.vel)

    def check_screen_out(self): #화면 밖으로 나가면 점수 획득.. 및.... 객체를 삭제 해야 합니다.
        result = False
        if self.rect.x < 0:
            result = True
        return result

all_sprites = pygame.sprite.Group()


#충돌 처리 쉽게 구현하기 위해 Sprite를 상속받기
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        #color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/cat1-2.png")
        
        
        self.rect = self.image.get_rect()
        self.vel = 0
        self.clicked = False  #마우스로 점프
        self.jump_cnt = 0 #3단 점프까지 적용 해 볼게요.

    def update(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            

            if self.jump_cnt < 3: #3회까지만..
                self.vel = -15
                self.jump_cnt += 1
                
            else:
                screen.blit(character, (360, self.vel))
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.vel += 1     #1씩 아래로 떨어지게 만듭니다.
        if self.vel > 10: # 10 이상 안넘어가도록.. 막습니다.
            self.vel = 10

        #바닥 = 화면 제일 밑
        if self.rect.bottom <= screen_height:
            self.rect.y += int(self.vel) #일단 떨어지게 하고.
            if self.rect.y >= screen_height - 39 - self.rect.height: #땅 부분을 처리한 것임.
                # 땅의 크기는 40으로 지정했고, 캐릭터의 위치는 39로 하여 낭떠러지에 부딪히면 GAME OVER 창이 나오게 구현함.
                self.rect.y = screen_height - 39 - self.rect.height
                self.jump_cnt = 0 #바닥에 착지했으니까... 점프횟수 초기화
  
def show_gameover():
    global game_over
    game_over = True
    screen.fill(red)

    font = pygame.font.SysFont("헤드라인", 60)
    over_text = font.render(f"GAME OVER!", True, (50,50,255))
    screen.blit(over_text, (int(screen_width/2 -  over_text.get_width()/2), int(screen_height/3)))

    font = pygame.font.SysFont("헤드라인", 30)
    over_text = font.render(f"press SPACE to RESTART..", True, (200,200,255))
    screen.blit(over_text, (int(screen_width/2 -  over_text.get_width()/2), int(screen_height/4*2)))

    pygame.mixer.quit()



def show_score():
    font = pygame.font.SysFont("헤드라인", 30)
    score_text = font.render(f"Score : {score}", True, (black))
    screen.blit(score_text, (530,0))

player = pygame.sprite.Group()

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
color != my_color and brown
player.add(Player(30,30, color))

game_over = False
score = 0
clock = pygame.time.Clock()
fps = 60
t_tick = -1

while True:
    clock.tick(fps)
    t_tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
  
    if pressed_keys[pygame.K_SPACE] and game_over:
        restart_game()
    


    #장애물 생성
    if game_over == True:
        show_gameover()
    else:
        if t_tick % random.randint(20,50) == 0:
            t_tick = 0
            obstacles.add(Obstacle(40, 40, my_color))

        #충돌 처리
        if pygame.sprite.groupcollide(player, obstacles, False, False) :
            show_gameover()

        
        #장애물이 왼쪽 밖으로 넘어간 것 체크
        del_obstacle = []
        for o in obstacles:
            if o.check_screen_out():
                score += 1
                del_obstacle.append(o)



        #장애물 삭제
        for d in del_obstacle:
            obstacles.remove(d)
        
        #screen.fill(my_color)

        background = pygame.image.load("C:/Users/김근영/Desktop/1학년 2학기/알고리즘과 게임콘텐츠/1주차/pygame/pygame_basic/background.png")
        screen.blit(background, (0, 0))
        show_score()
                
        player.update()
        player.draw(screen)

        obstacles.update()
        obstacles.draw(screen)

    pygame.display.update()