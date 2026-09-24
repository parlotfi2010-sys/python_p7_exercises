# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:22:39 2026
    assignment 5 , lesson 3
@author: Parnian lotfi
"""

print ("=" * 40)
print (" Hello to the python shop user! ")
print ("=" * 40)

product = input (' Enter your product name here : ')
price = input (' Enter your price here : ')
if price.isdigit() :
    price = (float (price))
else :
    price = input (' Try again : ')
    if price.isdigit() :
        price = (float(price))
    else :
        print (' Invalid price! ')
        
print ("=" * 40)

DiscountCode = input(' Enter your discount code here : ')

if DiscountCode.lower().strip()=='z14' :
    print ( 'Fainal price :' , price - (price * 0.2 ))
    
else :
    print (' Your discount code is false! ')
    print (' You have ONLY ONE MORE chance! ')
    
    DiscountCode2 = input (' Enter your discount code again here : ') 
    
    if DiscountCode2.lower().strip() =='z14' :
        print ( 'Fainal price :' , price - (price * 0.2 ))
        
    else :
        print ( ' Blocked ' )