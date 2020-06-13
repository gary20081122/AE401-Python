# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:56:07 2020

@author: User
"""

math = list()
total=0
avg=0

highest=0
lowest=100
n =input("people?")
n=int(n)

for i in range(n):
    score= input("input score")
    score=int(score)
    name= input("input name")
    
    oneperson = list()
    oneperson.append(name)
    oneperson.append(score)
    math.append(oneperson)
    
print(math)
# average score
for i in math:
    total = total+i[1]
average = total / n
 #highest score
high=0
person=''
for i in math:
    if i[1]>high:
        high=i[1]
        person=i[0]
print(person, "got the highest score",high)

# lowest score
low=100
person=''
for i in math:
    if i [1]<low:
        low=i[1]
        person=i[0]
print(person, "got the lowest score", low)
















































        
        
