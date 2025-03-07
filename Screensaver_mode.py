import pygame
import random

pygame.init()

width = 500
height = 500
window = pygame.display.set_mode((width,height))

pygame.display.set_caption("screensaver_python")

x = width / 2
y = height / 2
vel = 5
l = 80
w= 40

colours = ((160,82,45), (255,192,203),(255,255,255),(66,133,244) ,(244,160,0),(219,68,55),(15,157,88))
shape_colour = random.choice(colours)
shape_size = (l,w)

run = True

while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x = x + vel
    if x + w > width:
        vel = vel * -1
        shape_colour = random.choice(colours)

    if  x < 0 :
        vel += 5
        shape_colour = random.choice(colours)

    y = y + vel
    if y + l > height:
        vel = -5
        shape_colour = random.choice(colours)

    if y < 0 :
        vel += 5
        shape_colour = random.choice(colours)

 

    window.fill((92,64,51))
    pygame.draw.rect(window,shape_colour,(x,y,w,l))
    pygame.display.update()

pygame.quit()
