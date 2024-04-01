import pygame 
import datetime 
 
pygame.init() 
screen = pygame.display.set_mode((500, 400)) 
running = True 
 
clock = pygame.time.Clock() 
main_clock = pygame.image.load("lab 7/images/mainclock.png") 
minute_hand = pygame.image.load(("lab 7/images/rightarm.png")) 
second_hand = pygame.image.load(("lab 7/images/leftarm.png")) 
main_clock = pygame.transform.scale(main_clock, (500, 400)) 
minute_hand = pygame.transform.scale(minute_hand, (500, 450)) 
second_hand = pygame.transform.scale(second_hand, (30, 500)) 
 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    screen.fill((255, 255, 255)) 
    current_time = datetime.datetime.now() 
 
    minute_angle = current_time.minute * -6 - current_time.second/10 - 45
    second_angle = current_time.second * -6  
 
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle) 
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle) 
 
    screen.blit(main_clock, main_clock.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=screen.get_rect().center)) 
    pygame.display.flip() 
    clock.tick(60) 
 
pygame.quit()