# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:02:11 2026
-------------------------------------
 assignment1 , lesson 5
@author: Parnian lotfi
"""
scores = [20, 17, 9, 13, 7, 20, 18, 3, 1, 14]

passed = []
failed = []

for score in scores :
    if score >= 10 :
        passed.append(score)
    else :
        failed.append(score)

print (' Passed students : ' , passed)
print (' Failed students : ' , failed)
