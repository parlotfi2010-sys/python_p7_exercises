# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:46:39 2026
-----------------------------------------------------------------------
    assignment 3 , lesson 3
    **ye mashin hesab ke dota adad migire va operation va print kone**
@author: Parnian lotfi
"""

b = float(input(' Enter your number one here :'))
c = float(input(' Enter your number two here :'))
d = input('Enter your operation.')
if d == '+' :
     print ( b+c )
elif d == '-' :
    print ( b-c )
elif d == '*' :
     print ( b*c )
elif d == '/' :
    print (b/c)
elif d == '**' :
    print ( b ** c)
else:
    print (' !Error! ')