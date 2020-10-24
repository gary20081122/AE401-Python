# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:29:25 2020

@author: User
"""
import random
count=0
a=random.randint(1,10)

while count<5:
    count+=1
    x=input("請輸入一到十")
    x=int(x)
    if a>x:
        if count==5:
            print("5")
        else:
            print("big")
    elif x>a:
        if count==5:
            print("5")
        else:
            print("small")
    else:
        print("bingo")
        break





























