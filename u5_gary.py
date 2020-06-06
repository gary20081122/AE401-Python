# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:12:05 2020

@author: User
"""
sum=0
list=[]
highest=0
lowest=100
n =input("people?")
n=int(n)

for i in range(n):
    score= input("input score")
    score=int(score)
    list.append(score)

for i in range(n):  
    
     if list[i]>highest:
        highest = list[i]
     if list[i] <lowest:
        lowest = list[i]
     sum = list[i]+sum
average = sum/n

print("平均分",average)          
print("最高分",highest)
print("最低分",lowest)










































































