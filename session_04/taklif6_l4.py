# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:05:14 2026
---------------------------------------------------------------------------
    assignment_Q 6 , lesson 4
    --------------------------
    ye list az esm ha darim , ba estefade az halgheye for,
    majmooe toole tamame esm haro hesab kone.
@author: Parnian lotfi
"""
#--------------------------------------------------------    
names = ['Ali' , 'Sara' , 'Reza' , 'Mina']
for t in names:
    a = len (names[0])
    b = len (names[1])
    c = len (names[2])
    d = len (names[3])
total = a + b + c + d
print (total)
#--------------------------------------------------------    
names = ['Ali' , 'Sara' , 'Reza' , 'Mina']
for t in names:
    total = len(names[0] + names[1] + names[2] + names[3]) 
print (total)
#-------------------------------------------------------- 
total = 0
names = ['Ali' , 'Sara' , 'Reza' , 'Mina']
for t in names:
    total = (total + len(t))
print (total)



