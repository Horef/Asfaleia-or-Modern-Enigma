#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:40:05 2019

@author: Sergiy Horef
"""
"""
All you normally would use is this file.
The machine is already imported and created.
There are different function you can use:
    encode() - if you want to encode a sentence
    decode() - if you want to decode a sentence
    reset() - if you want to reset a machine to its starting positions
    config() - if you want to manually set a values to rotors
"""
from asfaleia_machine import Asfaleia_Machine

c_m = Asfaleia_Machine()
encoded_sentence = c_m.encode('Hi!')

c_m.reset()
decoded_sentence = c_m.decode(encoded_sentence)
print(decoded_sentence)
