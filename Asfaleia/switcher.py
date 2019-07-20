#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:06:05 2019

@author: Sergiy Horef
"""
#This is a swithcher class all it is doin is permanently changing
#places of a keys in the letters dictionary
class Switcher():
    def __init__(self):
        self = self
        
    def switch(self, letters, letter_one, letter_two):
        letters[letter_one], letters[letter_two] = letters.pop(letter_two), letters.pop(letter_one)
        
    def __str__(self):
        return 'This is a switcher, which switches {self.letter_one} with {self.letter_two}'.format(self=self)
    
    def __repr__(self):
        return '{self.__class__.__name__}({self.letters}, \'{self.letter_one}\', \'{self.letter_two}\')'.format(self=self)