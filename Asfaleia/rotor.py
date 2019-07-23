#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:18:02 2019

@author: Sergiy Horef
"""
#This is a rotor class which is a base for all of the created rotors
#, so you can use it as a template if you need more
class Rotor:
    #Every rotor has a base of 26 different shuffle possibilities
    #, and have a base shuffle value of 1, it also have a next rotor
    #parameter which is a rotor which value would increase by one,
    #if the current rotor reaches its 26 value
    def __init__(self, nr, val):
        self.num_of_values = 26
        self.current_value = val
        self.next_rotor = nr
        
    #Function is used to increase a value of the rotor
    def increase_current_value(self):
        if self.current_value == 26:
            if self.next_rotor != None:
                self.next_rotor.increase_current_value
            
            self.current_value = 1
        else: 
            self.current_value += 1
        
    #Function is used to manually set a value to the rotor
    def set_current_value(self, num):
        self.current_value = num
        
    #Function is used to manually get a value from the rotor(usless)
    def get_current_value(self):
        return self.current_value
    
    def __str__(self):
        return 'This is a default parent class of a rotor'
    
    def __repr__(self):
        return '{self.__class__.__name__}({self.next_rotor})'.format(self=self)