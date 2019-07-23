#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:12:41 2019

@author: Sergiy Horef
"""
#This is a file for a asfaleia machine which is already built from all the needed parts
from rotor_one import Rotor_One
from rotor_two import Rotor_Two
from rotor_three import Rotor_Three
from rotor_four import Rotor_Four
from rotor_five import Rotor_Five

from switcher import Switcher

class Asfaleia_Machine():
    def __init__(self, r_one=1, r_two=1, r_three=1, r_four=1, r_five=1):
        
        #This is a part of code used to check for values entered to be 
        #compatible with the program
        if not isinstance(r_one, int):
            raise TypeError('Rotor values should be entered as integers')
            
        if not isinstance(r_two, int):
            raise TypeError('Rotor values should be entered as integers')
            
        if not isinstance(r_three, int):
            raise TypeError('Rotor values should be entered as integers')
            
        if not isinstance(r_four, int):
            raise TypeError('Rotor values should be entered as integers')
            
        if not isinstance(r_five, int):
            raise TypeError('Rotor values should be entered as integers')
        
        #Dictionary of all the letters and coresponding to them
        self.letters = {'a':'a','b':'b','c':'c',
               'd':'d','e':'e','f':'f',
               'g':'g','h':'h','i':'i', 
               'j':'j','k':'k','l':'l',
               'm':'m','n':'n','o':'o',
               'p':'p','q':'q','r':'r',
               's':'s','t':'t','u':'u',
               'v':'v','w':'w','x':'x',
               'y':'y','z':'z'}
        
        #All the rotors are created from the least to first, it is important
        self.rotor_three = Rotor_One(None, r_three)
        self.rotor_two = Rotor_Five(self.rotor_three, r_two)
        self.rotor_one = Rotor_Three(self.rotor_two, r_one)
        
        #Swithers are created here
        self.switcher_one = Switcher()
        self.switcher_two = Switcher()
        self.switcher_three = Switcher()
        self.switcher_four = Switcher()
        self.switcher_five = Switcher()
        self.switcher_six = Switcher()
        self.switcher_seven = Switcher()
        self.switcher_eight = Switcher()
        self.switcher_nine = Switcher()
        self.switcher_ten = Switcher()
        
        #Switchers are used
        self.use_switchers()
        
    #Function used to use switchers
    def use_switchers(self):        
        self.switcher_one.switch(self.letters, 'a', 'r')
        self.switcher_two.switch(self.letters, 'k', 'l')
        self.switcher_three.switch(self.letters, 't', 'v')
        self.switcher_four.switch(self.letters, 'm', 'j')
        self.switcher_five.switch(self.letters, 'g', 'z')
        self.switcher_six.switch(self.letters, 'b', 'c')
        self.switcher_seven.switch(self.letters, 'e', 'y')        
        self.switcher_eight.switch(self.letters, 'o', 'n')
        self.switcher_nine.switch(self.letters, 's', 'k')
        self.switcher_ten.switch(self.letters, 'w', 'q')
        
    #Function used to uncode a sentence 
    def encode(self, sentence):
        if not isinstance(sentence, str):
                raise TypeError('You shoud use strings to encode')
        
        encoded_message = []
        
        for letter in sentence.lower():
            if letter not in self.letters:
                encoded_message.append(letter)
                continue
            
            # Values of rotors are increased only on one direction
            # so the values are not increased when the letters are
            # going all the way back
            self.rotor_one.shuffle_letters(self.letters)
            self.rotor_one.increase_current_value()
            self.rotor_two.shuffle_letters(self.letters)
            self.rotor_three.shuffle_letters(self.letters)
            
            self.rotor_three.shuffle_letters(self.letters)
            self.rotor_two.shuffle_letters(self.letters)
            self.rotor_one.shuffle_letters(self.letters)
            
            encoded_message.append(self.letters[letter.lower()])
        
        return ''.join(encoded_message)
    
    #Function used to decode a sentence 
    def decode(self, sentence):
        if not isinstance(sentence, str):
                raise TypeError('You shoud use strings to encode')
        
        decoded_message = []
        
        for letter in sentence.lower():
            if letter not in self.letters:
                decoded_message.append(letter)
                continue
            
            # Values of rotors are increased only on one direction
            # so the values are not increased when the letters are
            # going all the way back
            self.rotor_one.shuffle_letters(self.letters)
            self.rotor_one.increase_current_value()
            self.rotor_two.shuffle_letters(self.letters)
            self.rotor_three.shuffle_letters(self.letters)
            
            self.rotor_three.shuffle_letters(self.letters)
            self.rotor_two.shuffle_letters(self.letters)
            self.rotor_one.shuffle_letters(self.letters)
            
            for x, y in self.letters.items():
                if y == letter:
                    decoded_message.append(x)
        
        return ''.join(decoded_message)
        
    #Function used reset the machine to its starting form(init)
    def _set(self, r_one=1, r_two=1, r_three=1, r_four=1, r_five=1):
        self.reset_letters()
        self.use_switchers()
        
        if (1 <= r_one <= 26):
            self.rotor_one.set_current_value(r_one)
        else:
            raise ValueError('The value should be in appropriate range')
            
        if (1 <= r_two <= 26):
            self.rotor_two.set_current_value(r_two)
        else:
            raise ValueError('The value should be in appropriate range')
        
        if (1 <= r_three <= 26):
            self.rotor_three.set_current_value(r_three)
        else:
            raise ValueError('The value should be in appropriate range')
        
    #Function used to reset letters
    def reset_letters(self):
        self.letters = {'a':'a','b':'b','c':'c',
               'd':'d','e':'e','f':'f',
               'g':'g','h':'h','i':'i', 
               'j':'j','k':'k','l':'l',
               'm':'m','n':'n','o':'o',
               'p':'p','q':'q','r':'r',
               's':'s','t':'t','u':'u',
               'v':'v','w':'w','x':'x',
               'y':'y','z':'z'}
        
    def __str__(self):
        return 'This is an {self.__class__.__name__} class with properties of {self.rotor_one.__class__.__name__} - {self.rotor_one.current_value}, {self.rotor_two.__class__.__name__} - {self.rotor_two.current_value}, {self.rotor_three.__class__.__name__} - {self.rotor_three.current_value}'.format(self=self)
    
    def __repr__(self):
        return '{self.__class__.__name__}()'.format(self=self)