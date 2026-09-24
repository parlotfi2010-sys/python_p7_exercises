# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:05:33 2026
---------------------------------------------------------------------------
    assignment_Q 3 , lesson 4
    --------------------------
    products = ['Laptop' , 'Mouse' , 'Keyboard' , 'Monitor']
    ye list darim , ye vorodi az karbar migigre
    va az karbar mikhad esm ye mahsol ro bege
    agar dakhle list bashe --> mahsol dar dastres hast.
    agar nabood --> dar dastres nist
@author: Parnian lotfi
"""
print ('=' * 70)

product = ['Laptop' , 'Mouse' , 'Keyboard' , 'Monitor']

name = input(' Enter the product name : ').title().strip()
if name in product :
    print (' product is available. ')
else :
    print (' product is not available. ')