#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:22:17 2019

@author: Sergiy Horef
"""
from rotor import Rotor

class Rotor_Two(Rotor):
    
    def __init__(self, nr):
        super().__init__(nr)
        self.val_one_shuffler = [('f','i'), ('z','p'), ('m','b'), 
                                 ('u','v'), ('c','h'), ('g','e'), 
                                 ('l','t'), ('a','j'), ('n','q'), 
                                 ('y','o'), ('x','k'), ('s','d'), 
                                 ('r','w')]
        
        self.val_two_shuffler = [('q','z'), ('r','s'), ('a','v'), 
                                 ('o','d'), ('e','p'), ('i','j'), 
                                 ('b','f'), ('m','x'), ('g','t'), 
                                 ('l','y'), ('k','c'), ('n','h'), 
                                 ('w','u')]
        
        self.val_three_shuffler = [('v','m'), ('t','r'), ('a','x'), 
                                   ('l','s'), ('b','p'), ('z','q'), 
                                   ('u','i'), ('d','g'), ('h','c'), 
                                   ('n','e'), ('y','f'), ('k','j'), 
                                   ('o','w')]
        
        self.val_four_shuffler = [('a','k'), ('z','w'), ('o','l'), 
                                  ('h','f'), ('x','q'), ('e','s'), 
                                  ('c','t'), ('d','p'), ('v','g'), 
                                  ('b','i'), ('n','m'), ('u','y'), 
                                  ('r','j')]
        
        self.val_five_shuffler = [('a','k'), ('z','w'), ('o','l'), 
                                  ('h','f'), ('x','q'), ('e','s'), 
                                  ('c','t'), ('d','p'), ('v','g'), 
                                  ('b','i'), ('n','m'), ('u','y'), 
                                  ('r','j')]
        
        self.val_six_shuffler = [('y','a'), ('e','d'), ('i','k'), 
                                 ('m','s'), ('w','q'), ('r','l'), 
                                 ('z','x'), ('v','t'), ('f','b'), 
                                 ('p','o'), ('n','g'), ('c','j'), 
                                 ('h','u')]
        
        self.val_seven_shuffler = [('b','r'), ('j','e'), ('k','c'), 
                                   ('a','h'), ('l','o'), ('x','d'), 
                                   ('q','g'), ('f','p'), ('t','m'), 
                                   ('v','n'), ('u','y'), ('w','s'), 
                                   ('z','i')]
        
        self.val_eight_shuffler = [('y','s'), ('n','v'), ('w','f'), 
                                   ('e','a'), ('b','i'), ('g','z'), 
                                   ('u','j'), ('o','m'), ('x','h'), 
                                   ('q','r'), ('k','l'), ('p','d'), 
                                   ('c','t')]
        
        self.val_nine_shuffler = [('o','f'), ('z','p'), ('e','n'), 
                                  ('q','j'), ('l','y'), ('k','r'), 
                                  ('u','g'), ('h','v'), ('t','i'), 
                                  ('m','x'), ('s','b'), ('a','w'), 
                                  ('c','d')]
        
        self.val_ten_shuffler = [('k','p'), ('j','o'), ('l','w'), 
                                 ('r','i'), ('e','s'), ('f','h'), 
                                 ('a','q'), ('b','t'), ('c','m'), 
                                 ('d','x'), ('y','g'), ('v','n'), 
                                 ('z','u')]
        
        self.val_eleven_shuffler = [('d','q'), ('e','l'), ('u','x'), 
                                    ('v','j'), ('a','m'), ('s','g'), 
                                    ('w','f'), ('k','b'), ('i','t'), 
                                    ('r','c'), ('o','p'), ('n','z'), 
                                    ('y','h')]
        
        self.val_twelve_shuffler = [('m','n'), ('a','h'), ('e','l'), 
                                    ('k','t'), ('z','i'), ('b','g'), 
                                    ('j','r'), ('o','f'), ('w','y'), 
                                    ('d','p'), ('v','u'), ('c','s'), 
                                    ('q','x')]
        
        self.val_thirteen_shuffler = [('p','n'), ('k','f'), ('l','d'), 
                                      ('e','j'), ('w','r'), ('c','q'), 
                                      ('a','v'), ('x','s'), ('o','h'), 
                                      ('y','t'), ('i','u'), ('b','m'), 
                                      ('z','g')]
        
        self.val_fourteen_shuffler = [('k','g'), ('q','h'), ('s','m'), 
                                      ('p','b'), ('j','x'), ('t','d'), 
                                      ('y','a'), ('e','i'), ('f','c'), 
                                      ('n','v'), ('o','w'), ('r','l'), 
                                      ('u','z')]
        
        self.val_fifteen_shuffler = [('r','n'), ('c','j'), ('z','u'), 
                                     ('o','m'), ('f','v'), ('w','a'), 
                                     ('e','t'), ('h','l'), ('x','y'), 
                                     ('p','b'), ('s','i'), ('k','d'), 
                                     ('g','q')]
        
        self.val_sixteen_shuffler = [('w','h'), ('p','x'), ('f','d'), 
                                     ('k','r'), ('m','i'), ('l','s'), 
                                     ('g','q'), ('v','a'), ('u','y'), 
                                     ('o','z'), ('c','t'), ('e','j'), 
                                     ('b','n')]
        
        self.val_seventeen_shuffler = [('t','h'), ('s','r'), ('k','z'), 
                                       ('x','c'), ('d','l'), ('f','n'), 
                                       ('e','v'), ('i','u'), ('b','j'), 
                                       ('a','g'), ('w','p'), ('o','y'), 
                                       ('m','q')]
        
        self.val_eighteen_shuffler = [('s','i'), ('f','v'), ('y','g'), 
                                      ('u','n'), ('e','p'), ('x','c'), 
                                      ('j','o'), ('b','h'), ('l','w'), 
                                      ('t','d'), ('m','a'), ('q','z'), 
                                      ('r','k')]
        
        self.val_nineteen_shuffler = [('v','j'), ('u','s'), ('c','t'), 
                                      ('a','x'), ('f','z'), ('r','l'), 
                                      ('h','g'), ('y','w'), ('q','b'), 
                                      ('k','i'), ('e','m'), ('o','d'), 
                                      ('p','n')]
        
        self.val_twenty_shuffler = [('u','n'), ('v','z'), ('c','o'), 
                                    ('q','a'), ('w','l'), ('y','h'), 
                                    ('p','t'), ('f','m'), ('e','k'), 
                                    ('d','s'), ('b','g'), ('x','i'), 
                                    ('j','r')]
        
        self.val_twenty_one_shuffler = [('h','x'), ('j','g'), ('n','m'), 
                                        ('p','y'), ('f','w'), ('r','c'), 
                                        ('i','e'), ('d','k'), ('q','z'), 
                                        ('s','a'), ('t','l'), ('v','o'), 
                                        ('b','u')]
        
        self.val_twenty_two_shuffler = [('k','x'), ('c','n'), ('w','v'), 
                                        ('m','g'), ('d','z'), ('t','u'), 
                                        ('l','f'), ('p','o'), ('r','e'), 
                                        ('q','a'), ('b','s'), ('h','i'), 
                                        ('j','y')]
        
        self.val_twenty_three_shuffler = [('q','h'), ('s','k'), ('m','d'), 
                                          ('a','b'), ('w','x'), ('p','n'), 
                                          ('f','u'), ('l','y'), ('g','e'), 
                                          ('j','c'), ('o','r'), ('i','v'), 
                                          ('t','z')]
        
        self.val_twenty_four_shuffler = [('e','h'), ('o','z'), 
                                         ('y','v'), ('f','c'), 
                                         ('s','n'), ('l','k'), 
                                         ('m','x'), ('a','q'), 
                                         ('t','r'), ('i','j'), 
                                         ('u','w'), ('g','d'), 
                                         ('b','p')]
        
        self.val_twenty_five_shuffler = [('z','v'), ('o','b'), 
                                         ('g','f'), ('k','p'), 
                                         ('h','y'), ('q','e'), 
                                         ('l','j'), ('t','u'), 
                                         ('m','c'), ('r','s'), 
                                         ('w','x'), ('i','n'), 
                                         ('d','a')]
        
        self.val_twenty_six_shuffler = [('x','t'), ('z','p'), 
                                        ('o','r'), ('q','b'), 
                                        ('s','n'), ('l','j'), 
                                        ('h','u'), ('i','f'), 
                                        ('w','e'), ('v','y'), 
                                        ('k','a'), ('c','m'), 
                                        ('g','d')]
    
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
        
        self.increase_current_value()
