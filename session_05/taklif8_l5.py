# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:54:50 2026
-------------------------------------
 assignment8 , lesson 5
@author: Parnian lotfi
"""
print (' Hello! ')

while True :
    message = input ('You : ').lower().strip() 
    
    if message == 'bye' :
        print ('Good Bye.')
        break
    else :
        print ('[Chatbot answer]')

