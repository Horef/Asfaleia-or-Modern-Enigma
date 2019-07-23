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

print('[(', end = '')

for x in range(26):
    while True:
        num = r.randint(0, 25)
        
        if num not in in_use:
            in_use.add(num)
            
            if in_use.__len__() % 2 == 0:
                print('\'' + letters[num] + '\'', end = '')
                if (x != 25):
                    print('), ', end = '(')
                else:
                    print(')]')
            else:
                print('\'' + letters[num] + '\'', end = ',')
                
            break
        