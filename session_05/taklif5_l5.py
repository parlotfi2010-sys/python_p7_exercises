# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:54:44 2026
-------------------------------------
 assignment5 , lesson 5
@author: Parnian lotfi
"""
while True :
    username = input (' Enter your username : ').lower().strip()
    password = input (' Enter your password : ')
    
    if username == 'admin' and password == '1234' :
        print (' Successfully. ')
        break
    else :
        print (' Incorrect username or password. ')
        print ('=' * 70)