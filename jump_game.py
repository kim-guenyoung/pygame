import pygame
import sys
import random

pygame.init()

screen_width = 640
screen_height = 200


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("jump")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vel = 0
        self.clicked = False
        self.jump_cnt = 0

    def update(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            if self.jump_cnt < 3:
                self.vel = -15
                self.jump_cnt += 1
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.vel +=1
        if self.vel > 10:
            self.vel = 10

        if self.rect.bottom <= screen_height:
            self.rect.y +=int(self.vel)
            if self.rect.y >= screen_height - self.rect.height:
                self.rect.y = screen_height - self.rect.height
                self.jump_cnt = 0

class water(pygame.sprite.Sprite):
    def __init__(self, width, height, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        
        pt = [(width / 2, 0), (0, height), (width, height)]
        pygame.draw.polygon(self.image, color, pt)
        self.rect = self.image.get_rect()
        self.vel = 5
        self.rect.x = screen_width
        self.rect.y = screen_height - self.rect.height

    def update(self):
        self.rect.x -= int(self.vel)

    def check_screen_out(self):
        result = False
        if self.rect.x < 0:
            result = True
        return result

def show_gameover():
    global game_over
    game_over = True

    font = pygame.font.SysFont("헤드라인", 60)
    over_text = font.render(f"Game Over", True, (50, 50, 255))
    screen.blit(over_text, (int(screen_width / 2 - over_text.get_width() / 2), int(screen_height /3)))

    font = pygame.font.SysFont("헤드라인", 60)
    over_text = font.render(f"please, space key...", True, (200, 200, 255))
    screen.blit(over_text, (int(screen_width / 2 - over_text.get_width() / 2), int(screen_height /4 *2)))



player = pygame.sprite.Group()
player.add(Player(30, 30, white))
waters = pygame.sprite.Group()
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

    if game_over == True:
        pass

    if t_tick % random.randint(20, 50) == 0:
        t_tick = 0
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        waters.add(water(30, 30, color))

    if pygame.sprite.groupcollide(player, waters, False, False):
        game_over = True    

    del_water = []
    for w in waters:
        if w.check_screen_out():
            score += 1
            del_water.append(w)

    for d in del_water:
        waters.remove(w)

    print(f"점수 : {score}, 장애물 개수 : {len(waters)}")

    screen.fill(black)

    player.update()
    player.draw(screen)

    waters.update()
    waters.draw(screen)

    pygame.display.update()