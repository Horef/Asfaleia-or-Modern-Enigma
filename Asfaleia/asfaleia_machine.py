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
    def __init__(self):
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
        self.rotor_three = Rotor_Three(None)
        self.rotor_two = Rotor_Two(self.rotor_three)
        self.rotor_one = Rotor_One(self.rotor_two)
        
        #Swithers are created and used here
        self.switcher_one = Switcher()
        self.switcher_one.switch(self.letters, 'a', 'r')
        
        self.switcher_two = Switcher()
        self.switcher_two.switch(self.letters, 'k', 'l')
         
        self.switcher_three = Switcher()
        self.switcher_three.switch(self.letters, 't', 'v')
         
        self.switcher_four = Switcher()
        self.switcher_four.switch(self.letters, 'm', 'j')
        
        self.switcher_five = Switcher()
        self.switcher_five.switch(self.letters, 'g', 'z')
        
        self.switcher_six = Switcher()
        self.switcher_six.switch(self.letters, 'b', 'c')
        
        self.switcher_seven = Switcher()
        self.switcher_seven.switch(self.letters, 'e', 'y')
        
        self.switcher_eight = Switcher()
        self.switcher_eight.switch(self.letters, 'o', 'n')
        
        self.switcher_nine = Switcher()
        self.switcher_nine.switch(self.letters, 's', 'k')
        
    #Function used to uncode a sentence 
    def encode(self, sentence):
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
            
    #Function used to manually change the values of rotors
    def config(self, val_one, val_two, val_three):
        self.rotor_one.set_current_value(val_one)
        self.rotor_two.set_current_value(val_two)
        self.rotor_three.set_current_value(val_three)
        
        self.reset_letters()
        
    #Function used reset the machine to its starting form(init)
    def reset(self):
        self.__init__()
        
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