# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:40:39 2026
---------------------------------------------------
    assignment 1 , lesson 3
 **nomre(grade) begire bebine toye che rengi hast.**
@author: Parnian lotfi
"""
grade = float(input(' Type your grade here : '))

if 18 <= grade <= 20 :
    print ('A')
elif 16 <= grade < 18 :
    print ('B')
elif 14 <= grade < 16 :
    print ('C')
elif 10 <= grade < 14 :
    print ('D')
elif 0 <= grade < 10 :
    print ('F')
else :
    print (' your grade is not valid! ')

