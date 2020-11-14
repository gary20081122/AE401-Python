# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:13:03 2020

@author: User
"""

import pygame,random
pygame.init()
black=(0,0,0)
white=(255,255,255)

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
play_pos=(0,0)
music=pygame.mixer.Sound("laser5.ogg")
background_image=pygame.image.load("saturn_family1.jpg")
play_image=pygame.image.load("playerShip1_orange.png")
play_image.set_colorkey(black)

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            music.play()
    screen.blit(background_image,play_pos)
    position=pygame.mouse.get_pos()
    x =position[0]
    y =position[1]
    #screen.fill(colors())
    screen.blit(play_image, (x,y))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()       


























