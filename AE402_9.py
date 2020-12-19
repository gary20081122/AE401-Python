# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 09:58:28 2020

@author: User
"""

import pygame , random, math

class Ball(pygame.sprite.Sprite):
    dx=0
    dy=0
    x=0
    y=0
    
    def __init__(self,speed,srx,sry,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.x=srx
        self.y=sry
        self.image= pygame.Surface([radium*2,radium*2])
        self.image.fill((255,255,25))
        pygame.draw.circle(self.image,color,(radium,radium),radium,0)
        self.rect=self.image.get_rect() #取得球體
        self.rect.center=(srx,sry)
        move=random.randint(78,87)
        radian=math.radians(move)
        self.dx=speed *math.cos(radian)
        self.dy=speed *math.cos(radian)

    def update(self):
        self.x+=self.dx #x=x+dx
        self.y+=self.dy
        self.rect.x=self.x
        self.rect.y=self.y
        if(self.rect.left<=0 or self.rect.right >=500):
            self.dx*=-1
        elif(self.rect.top<=3 or self.rect.bottom >=500):
            self.dy*=-1
            
            
    def collidebounce(self):
        self.dx*=-1
            
pygame.init()
size=(500,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Gary")

color1=(23,76,151)
color2=(35,62,187)

background= pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))

allsprite =pygame.sprite.Group()
ball_1=Ball(3, 100,100,70,color1)
allsprite.add(ball_1)

ball_2=Ball(3, 100,100,7,color2)
allsprite.add(ball_2)

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


    screen.blit(background,(0,0))
    ball_1.update()
    ball_2.update()

    allsprite.draw(screen)
    result = pygame.sprite.collide_rect(ball_1,ball_2)
    if result ==True:
        ball_1.collidebounce()
        ball_2.collidebounce()
    pygame.display.update()

pygame.quit






























