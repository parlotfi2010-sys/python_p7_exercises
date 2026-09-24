# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:54:45 2026
-------------------------------------
 assignment6 , lesson 5
@author: Parnian lotfi
"""
a = 0
while a < 3 :
    username = input (' Enter your username : ').lower().strip()
    password = input (' Enter your password : ')
    
    if username == 'admin' and password == '1234' :
        print (' Successfully. ')
        break
    else :
        a = a + 1
        print (' Incorrect username or password. ')
if a == 3 :
    print (' Account locked. ')
