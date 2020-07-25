# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:16:00 2020

@author: User
"""
"""

fo = open('myfile.txt', 'w')
fo.write('This is a test')
"""


fo = open('myfile.txt','a')
fo.write('and I')
fo.close()

fo  = open('myfile.txt','r')
myletter = fo.read()
print(myletter)
fo.close()


import os.path

if os.path.isfile('myfile.txt'):
        print('檔案存在')
else:
        print('不存在')



































































