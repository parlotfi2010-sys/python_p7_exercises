# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:16:08 2026
---------------------------------------------------------------------------
    assignment_Q 3.edit , lesson 4
    --------------------------
    user mitone chandta vorodi bede
@author: Parnian lotfi
"""

print ('=' * 70)

product = ['Laptop' , 'Mouse' , 'Keyboard' , 'Monitor']

name = input(' Enter the product name : ').title().split(',')
if all(item.strip() in product for item in name) :
    print (' product is available. ')
else :
    print (' One or more products are not available. ')
#all---> baresi mikone ke hame mahsolate vared shode toye list bashan
#split()--->check mikone ke agar vorodi ha ba virgol az ham joda shode bodan be list tabdileshon kone