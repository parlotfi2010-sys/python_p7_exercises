# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:54:43 2026
-------------------------------------
 assignment4 , lesson 5
@author: Parnian lotfi
"""

while True :
    print ('1 : mojodi')
    print ('2 : variz')
    print ('3 : bardasht')

    choice = input(' Yek gozine vared konid : ').strip()
    if choice == '1' :
        print (' Amaliate mojodi entekhab shod. ')
    elif choice == '2' :
        print (' Amaliate variz entekhab shod. ')
    elif choice == '3' :
        print (' Amaliate bardasht entekhab shod. ')
    else :
        print (' Gozine eshtebah ast. ')
        continue
    
    choice2 = input (' Amaliate digar ya Khoroj? ').lower().strip()
    if choice2 == 'khoroj':
        print (' Mamnoon, Khoroje shoma ba movafaghiat anjam shod. ')
        break