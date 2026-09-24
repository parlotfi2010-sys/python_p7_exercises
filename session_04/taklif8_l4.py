# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:40:47 2026
---------------------------------------------------------------------------
    assignment_Q 8 , lesson 4
    --------------------------
    ye list az user ha darim va bayad tedad afradi ke dar in list andazeye
    esmhashon kamtar az 5 hast ro beshmarim
    users = ['ali' , 'vahid' , 'mohammadreza' , 'hamidreza' ,
             'gholamreza' , 'amir' , 'sara' , 'maryam']
@author: Parnian lotfi
"""

users = ['ali' , 'vahid' , 'mohammadreza' , 'hamidreza' ,
         'gholamreza' , 'amir' , 'sara' , 'maryam']
for user in users :
    if len(user) < 5 :
        print (user)