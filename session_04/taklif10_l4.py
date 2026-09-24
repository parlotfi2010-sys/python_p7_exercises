# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:11:19 2026
---------------------------------------------------------------------------
    assignment_Q 10 , lesson 4
    --------------------------
    ma ye dade darim az sensore yek karkhane ke dama ro be Celsius neveshte
    ye list jadid besazid va in list adad ro be farenheite tabdil kone
    F = C * 1.8 + 32
@author: Parnian lotfi
"""

Celsius = [10, 17, 14, 20, 30, 40, 38]
Farenheite = []

for C in Celsius :
    F = C * 1.8 + 32
    Farenheite.append(F)
print (Farenheite)