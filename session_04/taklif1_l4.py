# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:20:39 2026
---------------------------------------------------------------------------
    assignment_Q 1 , lesson 4
    --------------------------
    as user usernamesh ro begire va passwordwsh ro ham begire ,
    agar usarname barabar ba"admin" va password "1234" benevisid 
    login ba movafaghiat anjam shod,
    agar na  benevisid passworl ya username ghalat hasr.
    
@author: Parnian lotfi
"""

print ( '=' * 100 )
print ( '         Hello user         ' )
print ( '=' * 100 )

username = input(' Enter your username : ')
password = input(' Enter your password : ')

if username.lower().strip() == 'admin' and password == '1234' :
    print (' Login successful. ')
else :
    print (' Incorrect username or password. ')