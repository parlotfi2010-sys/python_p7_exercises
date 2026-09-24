# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:45:42 2026
---------------------------------------------------------------------------
    assignment_Q 12 , lesson 4
    --------------------------
    ba estefade az halgheye for
    ye systemi benevisid ke 5 bar az karbar esm yek mahsool begire(zara, nike,...)
    agar toole oon mahsool ka,tar az 6 ---> dakhele ye list be nam sabade_kharid berize
@author: Parnian lotfi
"""

sabade_kharid = []

for i in range (5) :
    product = input ('Enter product name : ').strip()
    if len(product) < 6 :
        sabade_kharid.append(product)
print (sabade_kharid)