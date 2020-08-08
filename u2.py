# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:02:27 2020

@author: User
"""


from datetime import date
weekdays = {0:'一',
            1:'二',
            2:'三',
            3:'四',
            4:'五',
            5:'六',
            6:'日'}

birth = input('20081122')
birth_year=int(birth[0:4])
birth_month = int(birth[4:6])
birth_day = int(birth[6:8])
birthday = date(birth_year,birth_month,birth_day)
age_days = date.today()-birthday

print('到今天共活了{}天'.format(age_days))
for keys in weekdays.keys():
    if birthday.weekday() == keys:
        print('生日那天是星期'+weekdays[keys])















































































