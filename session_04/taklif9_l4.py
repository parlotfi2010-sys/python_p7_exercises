# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:59:33 2026
---------------------------------------------------------------------------
    assignment_Q 9 , lesson 4
    --------------------------
    ye list darim az gheymate mahsol haye yek froshgah
    ye list jadid besazid ke tamam gheymate mahsoolat ro 10% afzayesh dehad
@author: Parnian lotfi
"""

prices = [100, 150, 200, 380, 456, 500, 1000]
new_prices = []

for price in prices :
    new_price = price + (price*0.1)
    new_prices.append(new_price)
print (new_prices)