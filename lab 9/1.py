'''
Racer
Extend example project from Lab 8 and add following tasks: Extra tasks to the given tutorial:

Randomly generating coins with different weights on the road
Increase the speed of Enemy when the player earns N coins
Comment your code
'''
import site
import pygame
import random
import time
from itertools import chain

pygame.init()

#Colors
black = pygame.Color((0,0,0))
white = pygame.Color((255,255,255))
red = pygame.Color((255,0,0))
blue = pygame.Color((0,0,255))
green = pygame.Color((0,255,0))

#Some game variables
screen_width = 400
screen_height = 600
speed = 5
#scores
score = 0
coin_score = 0
coin_scores ={
        "small":1,
        "medium":3,
        "large":5
    }

#fonts and game over text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)


#bg image
background = pygame.image.load("lab 9/images/AnimatedStreet.png")


#screen and frame counter
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
loop = True

#Enemy and Player classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab 9/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), -20)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > screen_height):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), -20)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab 9/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < screen_width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)

#coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy,size):
        super().__init__()
        if size == "small":
            self.image = pygame.image.load("lab 9/images/small_coin.png")
        elif size == "medium":
            self.image = pygame.image.load("images/med_coin.png")
        elif size == "large":
            self.image = pygame.image.load("images/big_coin.png")
        self.rect = self.image.get_rect()
        coord_range = list(chain(range(22, enemy.rect.center[0] - 24 - 22), range(enemy.rect.center[0] + 24 + 22, screen_width - 22)))
        #here we create create a range of integer values so that the coin and the enemy's rect's never overlap
        self.rect.center = (random.choice(coord_range), 0)
        self.size=size
    def move(self, enemy):
     self.rect.move_ip(0, speed)
     if self.rect.top > screen_height:
         self.rect.top = 0

#instances of player and enemy
P1 = Player()
E1 = Enemy()
coin = Coin(E1, "small")
#Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(coin)
car_sprites = pygame.sprite.Group()
car_sprites.add(P1, E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, coin)
#New User event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

coin_limit=10
while loop:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.2

        if event.type == pygame.QUIT:
            loop = False
    
    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, black)
    screen.blit(font_small.render(f"Coins: {coin_score}", True, black), (300, 10))
    screen.blit(scores, (10,10))

    

    #blits and moves all sprites
    for entity in car_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #moving the coin for every frame
    screen.blit(coin.image, coin.rect)
    coin.move(E1)

    if coin_score>=coin_limit:
        speed+=1
        coin_limit+=10
    
    #game over screen
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("lab 9/images/crash.wav").play()
        time.sleep(5)

        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
    if pygame.sprite.spritecollide(P1, coins_group, dokill=True):
        pygame.mixer.Sound("lab 9/images/getcoin.mp3").play()
        coin_score += coin_scores[coin.size]
     
    if len(coins_group) == 0:
        coin_size=random.choice(["small", "medium", "large"])
        coin = Coin(E1, coin_size)
        coins_group.add(coin)
        all_sprites.add(coin)

    
    try:
        pygame.display.flip()
    except:
        print("Game Over!")
        loop = False
    clock.tick(60)