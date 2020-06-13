# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:12:05 2020

@author: User
"""
sum=0
scores=[]
names=[]

highest=0
lowest=100
n =input("people?")
n=int(n)

for i in range(n):
    score= input("input score")
    score=int(score)
    scores.append(score)
    
    name= input("input name")
    names.append(name)
    
    
for i in range(n):  
     if scores[i]>highest:
        highest = scores[i]
        highestname = names[i]
        
     if scores[i] <lowest:
        lowest = scores[i]
        lowestname = names[i]


#print("平均分",average)             
print(highestname, 'highest:',highest)
print(lowestname, "Lowest:",lowest)




























































