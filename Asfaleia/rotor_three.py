#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:40:57 2019

@author: Sergiy Horef
"""
from rotor import Rotor

class Rotor_Three(Rotor):
    
    def __init__(self, nr):
        super().__init__(nr)
        
        self.val_one_shuffler = [('z','s'), ('k','x'), ('t','w'), 
                                 ('u','y'), ('h','v'), ('f','a'), 
                                 ('d','m'), ('q','l'), ('o','g'), 
                                 ('j','c'), ('p','r'), ('b','i'), 
                                 ('e','n')]
        
        self.val_two_shuffler = [('c','z'), ('j','h'), ('m','y'), 
                                 ('t','b'), ('i','f'), ('v','s'), 
                                 ('p','q'), ('u','r'), ('o','l'), 
                                 ('g','e'), ('x','n'), ('k','w'), 
                                 ('a','d')]
        
        self.val_three_shuffler = [('h','v'), ('d','a'), ('k','q'), 
                                   ('n','s'), ('m','b'), ('u','r'), 
                                   ('g','e'), ('l','j'), ('w','o'), 
                                   ('c','f'), ('t','z'), ('x','i'), 
                                   ('y','p')]
        
        self.val_four_shuffler = [('n','a'), ('c','h'), ('z','t'), 
                                  ('j','s'), ('u','v'), ('q','f'), 
                                  ('y','d'), ('k','m'), ('w','i'), 
                                  ('r','p'), ('x','o'), ('g','l'), 
                                  ('e','b')]
        
        self.val_five_shuffler = [('n','a'), ('c','h'), ('z','t'), 
                                  ('j','s'), ('u','v'), ('q','f'), 
                                  ('y','d'), ('k','m'), ('w','i'), 
                                  ('r','p'), ('x','o'), ('g','l'), 
                                  ('e','b')]
        
        self.val_six_shuffler = [('h','s'), ('l','n'), ('j','c'), 
                                 ('t','u'), ('p','q'), ('y','v'), 
                                 ('a','g'), ('w','o'), ('e','x'), 
                                 ('i','d'), ('m','f'), ('z','k'), 
                                 ('r','b')]
        
        self.val_seven_shuffler = [('p','c'), ('x','i'), ('k','b'), 
                                   ('y','g'), ('f','j'), ('t','u'), 
                                   ('a','z'), ('l','o'), ('n','v'), 
                                   ('h','q'), ('s','d'), ('e','w'), 
                                   ('r','m')]
        
        self.val_eight_shuffler = [('u','o'), ('d','z'), ('j','s'), 
                                   ('v','b'), ('m','i'), ('w','p'), 
                                   ('g','r'), ('a','h'), ('k','t'), 
                                   ('f','e'), ('c','q'), ('l','n'), 
                                   ('x','y')]
        
        self.val_nine_shuffler = [('u','q'), ('n','t'), ('y','k'), 
                                  ('d','s'), ('l','i'), ('b','m'), 
                                  ('z','h'), ('c','j'), ('p','r'), 
                                  ('a','e'), ('x','w'), ('f','g'), 
                                  ('v','o')]
        
        self.val_ten_shuffler = [('s','e'), ('y','o'), ('h','q'), 
                                 ('j','d'), ('k','r'), ('v','z'), 
                                 ('c','w'), ('l','p'), ('n','m'), 
                                 ('a','t'), ('b','i'), ('x','f'), 
                                 ('u','g')]
        
        self.val_eleven_shuffler = [('g','h'), ('z','m'), ('k','a'), 
                                    ('l','n'), ('o','p'), ('d','s'), 
                                    ('w','j'), ('i','x'), ('r','v'), 
                                    ('c','t'), ('b','u'), ('e','q'), 
                                    ('y','f')]
        
        self.val_twelve_shuffler = [('y','x'), ('u','w'), ('o','v'), 
                                    ('h','m'), ('e','c'), ('q','b'), 
                                    ('t','p'), ('s','f'), ('d','z'), 
                                    ('i','l'), ('j','a'), ('g','n'), 
                                    ('r','k')]
        
        self.val_thirteen_shuffler = [('p','r'), ('m','e'), ('j','x'), 
                                      ('o','b'), ('i','s'), ('c','a'), 
                                      ('v','z'), ('y','n'), ('t','q'), 
                                      ('k','h'), ('l','w'), ('f','d'), 
                                      ('u','g')]
        
        self.val_fourteen_shuffler = [('x','b'), ('t','w'), ('i','o'), 
                                      ('m','e'), ('g','a'), ('z','p'), 
                                      ('r','k'), ('j','n'), ('u','h'), 
                                      ('l','y'), ('q','c'), ('v','f'), 
                                      ('s','d')]
        
        self.val_fifteen_shuffler = [('j','k'), ('b','e'), ('a','g'), 
                                     ('z','q'), ('h','w'), ('y','t'), 
                                     ('i','o'), ('m','n'), ('s','v'), 
                                     ('f','d'), ('l','c'), ('p','x'), 
                                     ('r','u')]
        
        self.val_sixteen_shuffler = [('x','w'), ('m','q'), ('b','r'), 
                                     ('p','c'), ('a','h'), ('l','z'), 
                                     ('g','s'), ('e','v'), ('t','y'), 
                                     ('o','d'), ('f','u'), ('j','i'), 
                                     ('k','n')]
        
        self.val_seventeen_shuffler = [('f','t'), ('u','q'), ('m','x'), 
                                       ('z','h'), ('k','d'), ('g','r'), 
                                       ('e','j'), ('a','y'), ('i','w'), 
                                       ('o','c'), ('l','b'), ('p','v'), 
                                       ('n','s')]
        
        self.val_eighteen_shuffler = [('j','i'), ('q','g'), ('r','v'), 
                                      ('b','e'), ('t','m'), ('n','p'), 
                                      ('k','l'), ('h','y'), ('s','c'), 
                                      ('u','a'), ('x','o'), ('z','f'), 
                                      ('d','w')]
        
        self.val_nineteen_shuffler = [('b','u'), ('y','g'), ('h','r'), 
                                      ('a','d'), ('v','s'), ('j','p'), 
                                      ('o','k'), ('e','q'), ('w','c'), 
                                      ('l','x'), ('z','n'), ('f','t'), 
                                      ('i','m')]
        
        self.val_twenty_shuffler = [('b','k'), ('q','d'), ('i','s'), 
                                    ('x','a'), ('n','l'), ('h','o'), 
                                    ('u','p'), ('z','e'), ('y','m'), 
                                    ('t','j'), ('v','g'), ('w','r'), 
                                    ('c','f')]
        
        self.val_twenty_one_shuffler = [('f','t'), ('m','h'), ('z','a'), 
                                        ('x','j'), ('i','c'), ('v','s'), 
                                        ('l','o'), ('n','q'), ('p','g'), 
                                        ('w','b'), ('u','r'), ('y','e'), 
                                        ('d','k')]
        
        self.val_twenty_two_shuffler = [('p','r'), ('d','z'), ('a','w'), 
                                        ('x','h'), ('u','s'), ('l','y'), 
                                        ('m','b'), ('v','e'), ('o','g'), 
                                        ('t','q'), ('i','n'), ('f','k'), 
                                        ('c','j')]
        
        self.val_twenty_three_shuffler = [('g','k'), ('t','v'), ('e','f'), 
                                          ('b','c'), ('z','y'), ('x','d'), 
                                          ('l','j'), ('a','s'), ('i','w'), 
                                          ('h','o'), ('n','r'), ('p','q'), 
                                          ('u','m')]
        
        self.val_twenty_four_shuffler = [('v','l'), ('p','b'), ('j','a'), 
                                         ('k','h'), ('z','m'), ('y','c'), 
                                         ('r','e'), ('x','f'), ('w','u'), 
                                         ('i','g'), ('o','d'), ('t','s'), 
                                         ('n','q')]
        
        self.val_twenty_five_shuffler = [('p','b'), ('v','n'), ('s','a'), 
                                         ('z','x'), ('f','l'), ('d','e'), 
                                         ('t','g'), ('m','j'), ('u','h'), 
                                         ('q','o'), ('k','y'), ('w','r'), 
                                         ('i','c')]
        
        self.val_twenty_six_shuffler = [('s','b'), ('x','g'), ('p','t'), 
                                        ('u','i'), ('h','v'), ('y','k'), 
                                        ('l','a'), ('o','w'), ('n','e'), 
                                        ('d','r'), ('f','j'), ('m','c'), 
                                        ('q','z')]
    
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

