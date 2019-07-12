#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:46:59 2019

@author: sergiyzymogliad
"""

import random as r

letters = ['a','b','c','d','e','f','g','h','i',
           'j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']

in_use = set()

i = 0
print('(', end = '')

for x in range(26):
    while True:
        num = r.randint(0,25)
        
        if num not in in_use:
            in_use.add(num)
            i += 1
            
            if i == 2:
                print('\'' + letters[num] + '\'', end = '),')
                i = 0
                print(' ', end = '(')
            else:
                print('\'' + letters[num] + '\'', end = ',')
                
            break
        