# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:03:17 2020

@author: User
"""

import pygame,random

black=(0,0,0)
white=(255,255,255)
pygame.init()
def move (image1,image2):
    global count
    if count<5:
        image=image1
    elif count<5:
        image=image2
       
    if count>10:
        count=0
    else:
        count+=1
        return image
    
 

def colors():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return(r,g,b)

size =(600,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Gary")

clock=pygame.time.Clock()

down1=pygame.image.load("down1.png")
down2=pygame.image.load("down2.png")
side1=pygame.image.load("side1.png")
side2=pygame.image.load("side2.png")
standing=pygame.image.load("standing.png")
teleport1=pygame.image.load("teleport1.png")
teleport2=pygame.image.load("teleport2.png")
teleport3=pygame.image.load("teleport3.png")
up1=pygame.image.load("up1.png")
up2=pygame.image.load("up2.png")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

k=pygame.mixer.Sound("teleport.wav")

x=0
y=0

lock=False
done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    key=pygame.key.get_pressed()
    
    if not lock:
        if key[pygame.K_LEFT]:
            x-=1
        elif key[pygame.K_RIGHT]:
            x+=1
        elif key[pygame.K_UP]:
            y-=1        
        elif key[pygame.K_DOWN]:
            y+=1
        elif key[pygame.K_SPACE]:
            lock = True # 進入穿越模式
        else:
            image=standing
            count=0
    
    else:
        if count==0:
            k.play()
            #image=teleport1
        elif count<5:
            image=teleport1
        elif count<10:
            image=teleport2
        elif count<15:
            image=teleport3
        else:    
            x = random.randrange(0, size[0])
            y = random.randrange(0, size[1])
            locked = False
            count = 0
        count+=1    
        
    screen.fill(colors())
    screen.blit(image, (x,y))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()       






















































