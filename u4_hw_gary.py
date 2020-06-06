# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:15:39 2020

@author: User
"""

import turtle

turtle.shape("circle")
turtle.penup()
size =20
for i in range(30):
    turtle.stamp()
    size = size+3
    turtle.forward(size)
    turtle.right(24)
turtle.done()















