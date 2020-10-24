# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:06:21 2020

@author: User
"""


import pygame
orange =(0,0,0)
white=(255,255,255)
yellow=(255,255,102)

size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("宗麟")

done=False
clock=pygame.time.Clock()
screen.fill(orange)

size=(150,150)
r=pygame.Surface(size)
pygame.draw.rect(screen,yellow,r.get_rect(),50)
pygame.display.flip()
clock.tick(60)





















