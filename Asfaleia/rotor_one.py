#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:25:11 2019

@author: Sergiy Horef
"""
from rotor import Rotor
#Class for a first rotor
class Rotor_One(Rotor):
    
    def __init__(self, nr):
        #It starts its life from calling a parent func of init
        super().__init__(nr)
        #From here are going lists of all the tuples that used to shuffle the letters
        self.val_one_shuffler = [('u','d'), ('e','a'), ('s','g'), 
                                 ('r','p'), ('h','v'), ('b','l'), 
                                 ('k','x'), ('n','q'), ('m','c'), 
                                 ('z','o'), ('t','w'), ('i','f'), 
                                 ('j','y')]
        
        self.val_two_shuffler = [('u','q'), ('a','h'), 
                                 ('l','x'), ('j','s'), 
                                 ('k','f'), ('i','o'), 
                                 ('d','e'), ('c','v'), 
                                 ('p','g'), ('n','b'), 
                                 ('m','t'), ('z','r'), 
                                 ('y','w')]
        
        self.val_three_shuffler = [('e','g'), ('n','l'), 
                                  ('y','w'), ('p','t'), 
                                  ('h','c'), ('m','q'), 
                                  ('d','j'), ('u','x'), 
                                  ('s','v'), ('i','f'), 
                                  ('a','b'), ('o','z'), 
                                  ('r','k')]
        
        self.val_four_shuffler = [('x','c'), ('d','m'), 
                                  ('u','r'), ('t','j'), 
                                  ('h','s'), ('f','e'), 
                                  ('q','n'), ('w','y'), 
                                  ('a','p'), ('g','i'), 
                                  ('z','l'), ('k','b'), 
                                  ('o','v')]
        
        self.val_five_shuffler = [('x','q'), ('w','g'), 
                                  ('n','a'), ('p','v'), 
                                  ('d','j'), ('s','k'), 
                                  ('l','i'), ('y','m'), 
                                  ('t','r'), ('h','z'), 
                                  ('c','o'), ('f','u'), 
                                  ('b','e')]
        
        self.val_six_shuffler = [('n','w'), ('h','z'), 
                                 ('f','e'), ('l','t'), 
                                 ('p','x'), ('v','o'), 
                                 ('q','m'), ('r','g'), 
                                 ('d','y'), ('u','c'), 
                                 ('s','k'), ('a','i'), 
                                 ('j','b')]
        
        self.val_seven_shuffler = [('t','c'), ('y','l'), 
                                   ('f','z'), ('w','k'), 
                                   ('p','g'), ('s','o'), 
                                   ('m','x'), ('h','u'), 
                                   ('d','n'), ('r','b'), 
                                   ('a','i'), ('q','e'), 
                                   ('v','j')]
        
        self.val_eight_shuffler = [('j','c'), ('m','t'), 
                                   ('g','s'), ('d','o'), 
                                   ('a','i'), ('l','v'), 
                                   ('y','n'), ('r','q'), 
                                   ('z','p'), ('h','k'), 
                                   ('x','w'), ('b','u'), 
                                   ('f','e')]
        
        self.val_nine_shuffler = [('m','p'), ('w','a'), 
                                  ('u','q'), ('r','e'), 
                                  ('t','v'), ('f','b'), 
                                  ('o','z'), ('s','n'), 
                                  ('h','x'), ('c','k'), 
                                  ('y','l'), ('i','g'), 
                                  ('d','j')]
        
        self.val_ten_shuffler = [('e','k'), ('t','f'), 
                                 ('s','p'), ('r','l'), 
                                 ('v','m'), ('o','y'), 
                                 ('n','h'), ('c','q'), 
                                 ('a','z'), ('b','d'), 
                                 ('w','g'), ('i','u'), 
                                 ('j','x')]
        
        self.val_eleven_shuffler = [('f','e'), ('k','s'), 
                                    ('q','w'), ('i','j'), 
                                    ('l','n'), ('u','g'), 
                                    ('v','d'), ('x','t'), 
                                    ('r','o'), ('y','m'), 
                                    ('z','a'), ('h','c'), 
                                    ('p','b')]
        
        self.val_twelve_shuffler = [('f','n'), ('g','b'), 
                                    ('d','k'), ('t','m'), 
                                    ('s','c'), ('e','p'), 
                                    ('q','u'), ('i','h'), 
                                    ('l','o'), ('r','z'), 
                                    ('y','v'), ('x','j'), 
                                    ('w','a')]
        
        self.val_thirteen_shuffler = [('a','w'), ('c','o'), 
                                      ('f','j'), ('n','x'), 
                                      ('g','s'), ('v','y'), 
                                      ('l','u'), ('m','r'), 
                                      ('p','z'), ('b','i'), 
                                      ('d','k'), ('h','q'), 
                                      ('e','t')]
        
        self.val_fourteen_shuffler = [('u','i'), ('x','r'), 
                                      ('v','f'), ('t','p'), 
                                      ('c','g'), ('y','w'), 
                                      ('h','m'), ('b','s'), 
                                      ('z','o'), ('n','k'), 
                                      ('d','l'), ('q','j'), 
                                      ('a','e')]
        
        self.val_fifteen_shuffler = [('a','v'), ('j','m'), 
                                     ('k','u'), ('b','e'), 
                                     ('w','y'), ('i','p'), 
                                     ('x','q'), ('s','n'), 
                                     ('h','c'), ('t','f'), 
                                     ('z','l'), ('g','r'), 
                                     ('d','o')]
        
        self.val_sixteen_shuffler = [('e','m'), ('u','a'), 
                                     ('p','z'), ('r','h'), 
                                     ('x','w'), ('f','y'), 
                                     ('l','s'), ('k','d'), 
                                     ('v','g'), ('t','c'), 
                                     ('i','o'), ('n','j'), 
                                     ('b','q')]
        
        self.val_seventeen_shuffler = [('x','f'), ('g','i'), 
                                       ('t','h'), ('p','m'), 
                                       ('r','o'), ('e','y'), 
                                       ('q','u'), ('n','c'), 
                                       ('d','v'), ('j','b'), 
                                       ('l','s'), ('a','k'), 
                                       ('w','z')]
        
        self.val_eighteen_shuffler = [('y','t'), ('f','v'), 
                                      ('g','i'), ('z','b'), 
                                      ('u','e'), ('r','a'), 
                                      ('l','d'), ('j','o'), 
                                      ('s','p'), ('m','k'), 
                                      ('x','w'), ('q','c'), 
                                      ('n','h')]
        
        self.val_nineteen_shuffler = [('d','t'), ('b','a'), 
                                      ('i','l'), ('e','m'), 
                                      ('s','r'), ('j','x'), 
                                      ('z','y'), ('o','h'), 
                                      ('v','w'), ('u','q'), 
                                      ('p','g'), ('f','c'), 
                                      ('k','n')]
        
        self.val_twenty_shuffler = [('s','x'), ('b','t'), 
                                    ('v','d'), ('f','h'), 
                                    ('q','o'), ('p','m'), 
                                    ('e','i'), ('l','k'), 
                                    ('y','z'), ('g','n'), 
                                    ('r','a'), ('u','w'), 
                                    ('c','j')]
        
        self.val_twenty_one_shuffler = [('e','x'), ('b','y'), 
                                        ('z','j'), ('a','v'), 
                                        ('l','r'), ('t','n'), 
                                        ('d','i'), ('h','u'), 
                                        ('q','p'), ('m','w'), 
                                        ('g','s'), ('c','k'), 
                                        ('f','o')]
        
        self.val_twenty_two_shuffler = [('q','o'), ('i','b'), 
                                        ('w','f'), ('x','u'), 
                                        ('e','j'), ('m','y'), 
                                        ('t','z'), ('r','k'), 
                                        ('a','d'), ('v','l'), 
                                        ('s','c'), ('g','p'), 
                                        ('n','h')]
        
        self.val_twenty_three_shuffler = [('a','x'), ('s','n'), 
                                          ('d','l'), ('g','z'), 
                                          ('m','h'), ('t','r'), 
                                          ('k','o'), ('w','c'), 
                                          ('y','f'), ('p','e'), 
                                          ('v','u'), ('j','i'), 
                                          ('q','b')]
        
        self.val_twenty_four_shuffler = [('b','v'), ('k','x'), 
                                         ('p','l'), ('z','m'), 
                                         ('t','j'), ('g','n'), 
                                         ('d','e'), ('o','i'), 
                                         ('a','w'), ('y','c'), 
                                         ('s','h'), ('f','q'), 
                                         ('u','r')]
        
        self.val_twenty_five_shuffler = [('w','f'), ('q','u'), 
                                         ('c','v'), ('s','i'), 
                                         ('p','j'), ('d','b'), 
                                         ('t','l'), ('r','g'), 
                                         ('z','m'), ('y','x'), 
                                         ('h','e'), ('n','k'), 
                                         ('o','a')]
        
        self.val_twenty_six_shuffler = [('y','h'), ('p','l'), 
                                        ('n','z'), ('j','o'), 
                                        ('x','i'), ('d','t'), 
                                        ('f','m'), ('r','e'), 
                                        ('k','v'), ('q','a'), 
                                        ('b','u'), ('s','w'), 
                                        ('c','g')]
    
    #This function is used to shuffle the letters
    def shuffle_letters(self, letters):
        if self.current_value == 1:
            for pair in self.val_one_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 2:
            for pair in self.val_two_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 3:
            for pair in self.val_three_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 4:
            for pair in self.val_four_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 5:
            for pair in self.val_five_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 6:
            for pair in self.val_six_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 7:
            for pair in self.val_seven_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 8:
            for pair in self.val_eight_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 9:
            for pair in self.val_nine_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 10:
            for pair in self.val_ten_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 11:
            for pair in self.val_eleven_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 12:
            for pair in self.val_twelve_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 13:
            for pair in self.val_thirteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 14:
            for pair in self.val_fourteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 15:
            for pair in self.val_fifteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 16:
            for pair in self.val_sixteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 17:
            for pair in self.val_seventeen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 18:
            for pair in self.val_eighteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 19:
            for pair in self.val_nineteen_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 20:
            for pair in self.val_twenty_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 21:
            for pair in self.val_twenty_one_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 22:
            for pair in self.val_twenty_two_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 23:
            for pair in self.val_twenty_three_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 24:
            for pair in self.val_twenty_four_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 25:
            for pair in self.val_twenty_five_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
                
        elif self.current_value == 26:
            for pair in self.val_twenty_six_shuffler:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]
        
        
    def __str__(self):
        return 'This is a {self.__class__.__name__} with a value of {self.current_value}'.format(self=self)
    
    def __repr__(self):
        return '{self.__class__.__name__}({self.next_rotor})'.format(self=self)