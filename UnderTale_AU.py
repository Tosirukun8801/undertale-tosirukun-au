import pygame
from pygame.locals import*
import sys
import time
import math
import asyncio

pygame.init()
pos = [360, 300]
papyrus_pos_body = [360,120]

flame_x1 = 100
flame_y1 = 260
flame_x2 = 520
flame_y2 = 160

heart_type = "red"

papyrus_pos_x_true = 0

heart_red = pygame.image.load("./images/heart_red.png")
papyrus_body = pygame.image.load("./images/papyrus/body1.png")
papyrus_head = pygame.image.load("./images/papyrus/head1.png")
papyrus_leg = pygame.image.load("./images/papyrus/leg1.png")
blastershot = pygame.image.load("./images/blaster/blaster1.png")
blasterfire = pygame.image.load("./images/blaster/blaster2.png")

heart_start = pygame.mixer.Sound("./sounds/start1.wav")
heart_start2 = pygame.mixer.Sound("./sounds/start2.wav")
heart_start3 = pygame.mixer.Sound("./sounds/start3.wav")
blaster_shot = pygame.mixer.Sound("./sounds/blastershot.wav")
blaster_fire = pygame.mixer.Sound("./sounds/gasterfire.wav")



screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("UnderTale AU BETA")
pygame.key.set_repeat(5,5)

loop = asyncio.get_event_loop()

pygame.draw.rect(screen, (255,255,255), Rect(100,260,520,160), 8)
pygame.display.update()

heart_start2.play()
time.sleep(0.2)
heart_start2.play()
time.sleep(0.8)
heart_start3.play()
time.sleep(0.5)

pygame.mixer.music.load("./sounds/bgm1.mp3")
pygame.mixer.music.play(-1)


papyrus_body = pygame.transform.scale(papyrus_body, (98, 100))
papyrus_head = pygame.transform.scale(papyrus_head, (75, 70))
papyrus_leg = pygame.transform.scale(papyrus_leg, (86, 76))

while(1):
    async def blaster(x, y, z):
        blastershot = pygame.image.load("./images/blaster/blaster1.png")
        blasterfire = pygame.image.load("./images/blaster/blaster2.png")
        blaster_shot.play()
        blastershot = pygame.transform.rotate(blastershot, z)
        screen.blit(blastershot, (x, y))
        await asyncio.sleep(2)
        blaster_fire.play()
        blasterfire = pygame.transform.rotate(blasterfire, z)
        screen.blit(blasterfire, (x, y))
        

        
    screen.fill((0,0,0))
    press = pygame.key.get_pressed()
                
    if press[K_0]:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(blaster(100,100,270))
    if heart_type == "red":
        rect = heart_red.get_rect()
        rect.center = pos
        screen.blit(heart_red, rect)
    screen.blit(papyrus_leg, (311,150))
    screen.blit(papyrus_body, (311, 70))
    screen.blit(papyrus_head, (311, 25))
    pygame.draw.rect(screen, (255,255,0), Rect(300,450,120,20))
    pygame.draw.rect(screen, (255,255,255), Rect(flame_x1,flame_y1,flame_x2,flame_y2), 8) #枠を描画
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    #if papyrus_pos_x_true == 0:
        #papyrus_pos_body[0] += 0.005
        #if papyrus_pos_body[0] > 362:
            #papyrus_pos_x_true = 1
            #papyrus_pos_body[0] += 0.005

    #if papyrus_pos_x_true == 1:
        #papyrus_pos_body[0] -= 0.005
        #if papyrus_pos_body[0] < 358:
            #papyrus_pos_x_true = 0
            #papyrus_pos_body[0] -= 0.005

    press = pygame.key.get_pressed()
                
    if press[K_LEFT]:
        if not pos[0] < flame_x1 + 15:
            pos[0] -= 0.1
    if press[K_RIGHT]:
        if not pos[0] > flame_x1 + flame_x2 - 15:
            pos[0] += 0.1
    if press[K_UP]:
        if not pos[1] < flame_y1 + 15:
            pos[1] -= 0.1
    if press[K_DOWN]:
        if not pos[1] > flame_y1 + flame_y2 -15:
            pos[1] += 0.1
