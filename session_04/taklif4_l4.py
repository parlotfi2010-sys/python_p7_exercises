# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:22:01 2026
---------------------------------------------------------------------------
    assignment_Q 4 , lesson 4
    --------------------------
    az karbar sorate mashin migire (speed)
    agar speed > 120 ---> dangerous
    agar 120 >= speed > 80 ---> high speed  
    agar 80 >= speed > 0 ---> Normal speed
    agar speed <= 0 ---> The car is stopped
@author: Parnian lotfi
"""

speed = input(" Enter your car's speed : ").strip()

if speed.isdigit() :
    speed = float(speed)
    if speed > 120 :
        print (' Dangerous!! ')   
    elif 120 >= speed > 80 :
        print (' High speed! ')
    elif 80 >= speed > 0 :
        print (' Normal speed. ')
    elif speed <= 0 :
        print (' The car is stopped. ')
else :
    print (' Invalid speed. ')