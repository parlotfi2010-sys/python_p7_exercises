# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:36:24 2026
-------------------------------------
 assignment3 , lesson 5
@author: Parnian lotfi
"""
products = []

while True :
    product = input(' Enter product name : ')
    
    if product.lower().strip() == 'exit' :
        break
    products.append(product)
print (products)
