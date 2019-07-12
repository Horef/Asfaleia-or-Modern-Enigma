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
    encode_letter() - if you want to encode a single letter
    encode_sentence() - if you want to encode a sentence
    reset() - if you want to reset a machine to its starting positions
    set_rotors() - if you want to manually set a values to rotors
"""
from asfaleia_machine import Asfaleia_Machine

current_machine = Asfaleia_Machine()
current_machine.encode_sentence('Hi!')

current_machine.reset()
current_machine.decode_sentence('dzhew!')