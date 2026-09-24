# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:54:49 2026
-------------------------------------
 assignment7 , lesson 5
@author: Parnian lotfi
"""
foods = ['pizza', 'burger', 'pasta', 'salad' , 'fries']
orders = []

print('Restaurant Menu :')
print(foods)

while True :
    user_orders = input (' Enter your food name : ').lower().strip()
    if user_orders == 'order' :
        break
    elif user_orders in foods :
        orders.append(user_orders)
    else :
        print (' Your food is not on the menu. ')
    
print ('Your Factore : ')
for food in orders :
    print (food)
