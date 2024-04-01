#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
#When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. 
#The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
import pygame as pg 

clock = pg.time.Clock()

pg.init()

screen = pg.display.set_mode((700,700))

done  = False
x = 25
y = 25
while not done:
    screen.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True 

    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT] :
        if x+20 > 675:continue
        else:x += 20
    if keys[pg.K_LEFT]:
        if x-20 < 25:continue
        else:x -= 20
    if keys[pg.K_UP]:
        if y-20 < 25:continue
        else:y -= 20
    if keys[pg.K_DOWN]:
        if y+20 > 675:continue
        else:y += 20
    
    pg.draw.circle(screen,'Red', (x,y), 25)
    
    clock.tick(60)
    pg.display.flip()