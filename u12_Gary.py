# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:38:06 2020

@author: User
"""


import time

run = input("Start? > ")
# Only run if user types in "start"
startTime = time.time()
try:
    if run == "start":
    #Loop until we reach 20 minutes running
        while True:
            totalTime = round(time.time() - startTime, 1)
            print(">>>>>>", totalTime)

except KeyboardInterrupt:
    print(totalTime,'seconds')


















































































