"""
Created on Tue Aug 25 21:13:09 2026
----------------3-----------------------------------------------------------
    assignment_Q 2 , lesson 4
    --------------------------
    az user gheymate kala ro begire
    agar gheymat >= 1 million --> %20 takhfif
    agar 500,000 >= gheymar > 1 --> 15
    agar < 500 10 
@author: lotfi
"""
print ('=' * 70)
price = input(' Enter your price : ')
if price.isdigit():
   price = float(price) 
   
   if price > 1000000 :
    print ( price - (price * 0.2))
   elif price > 500000 :
    print (price - (price * 0.15))
   elif price <= 500000 :
    print (price - (price * 0.1))
else :
    print (' Invalid price! ')
 