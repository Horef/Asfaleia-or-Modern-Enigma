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

current_machine = Asfaleia_Machine()
encoded_sentence = current_machine.encode('Hi!')

current_machine.reset()
decoded_sentence = current_machine.decode(encoded_sentence)
print(decoded_sentence)
