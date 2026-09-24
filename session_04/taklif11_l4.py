# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:21:06 2026
---------------------------------------------------------------------------
    assignment_Q 11 , lesson 4
    --------------------------
    ye list darim az gheymate mahsoolat
    va ye list darim az gheymate froshe mahsoolat
    bayad soode har kodom az mahsolat ro dar yek list joda hesab
    soode ---> sell_prices - buy_prices
    buy_prices = [100, 200, 150, 400]
    sell_prices = [130, 250, 190, 500]
@author: Parnian lotfi
"""

buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]
profits = []

for i in range (len (buy_prices)) :
     profit = sell_prices[i] - buy_prices[i] 
     profits.append(profit)
print(profits)