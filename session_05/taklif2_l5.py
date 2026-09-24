# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:55:39 2026
-------------------------------------
 assignment2 , lesson 5
@author: Parnian lotfi
"""
students = ['ali', 'vahid', 'sara', 'hamid', 'reza',
            'elham','mohsen', 'zahra', 'paniz', 'parmida']

scores = [20, 17, 9, 13, 7, 20, 18, 3, 1, 14]

passed = []

for i in range (len(students)) :
    if scores[i] >= 10 :
        passed.append([scores[i] , students[i]])

passed.sort(reverse=True)
for student in passed :
    print (student[1] , ':' , student[0])