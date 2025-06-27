from pygame import *

mw = display.set_mode ((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (700, 500))

x1, y1 = 100, 300 
x2, y2 = 300, 300

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
speed = 2

run = True
clock = time.Clock()
FPS = 500
while run:
    mw.blit(background, (0,0))
    mw.blit(sprite1, (x1, y1))
    mw.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1>5:
        x1-=speed
    if keys_pressed[K_a] and x2>5:
        x2-=speed
    if keys_pressed[K_w] and y2>5:
        y2 -= speed
    if keys_pressed[K_UP] and y1>5:
        y1 -= speed
    if keys_pressed[K_RIGHT] and x1<595:
        x1 += speed
    if keys_pressed[K_d] and x2<595:
        x2 += speed
    if keys_pressed[K_s] and y2<395:
        y2 += speed
    if keys_pressed[K_DOWN] and y1<395:
        y1 += speed


    display.update()
    clock.tick(FPS)