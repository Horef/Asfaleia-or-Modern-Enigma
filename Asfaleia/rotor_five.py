#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:57:50 2019

@author: Sergiy Horef
"""
from rotor import Rotor

class Rotor_Five(Rotor):
    
    def __init__(self, nr):
        super().__init__(nr)
        self.val_one_shuffler = [('v','d'), ('a','x'), ('i','y'), 
                                 ('c','k'), ('w','z'), ('n','f'), 
                                 ('l','r'), ('u','q'), ('j','e'), 
                                 ('b','m'), ('s','t'), ('p','o'), 
                                 ('g','h')]
        
        self.val_two_shuffler = [('z','c'), ('d','j'), ('b','h'), 
                                 ('g','y'), ('x','f'), ('i','l'), 
                                 ('r','t'), ('s','o'), ('w','v'), 
                                 ('u','k'), ('a','p'), ('q','n'), 
                                 ('e','m')]
        
        self.val_three_shuffler = [('d','j'), ('i','y'), ('t','k'), 
                                   ('x','r'), ('m','h'), ('w','p'), 
                                   ('a','u'), ('q','c'), ('n','b'), 
                                   ('e','z'), ('f','o'), ('g','s'), 
                                   ('l','v')]
        
        self.val_four_shuffler = [('p','u'), ('t','c'), ('m','v'), 
                                  ('a','n'), ('b','f'), ('s','l'), 
                                  ('e','i'), ('q','h'), ('o','g'), 
                                  ('j','z'), ('x','w'), ('r','d'), 
                                  ('k','y')]
        
        self.val_five_shuffler = [('u','x'), ('h','a'), ('e','v'), 
                                  ('w','y'), ('z','g'), ('r','j'), 
                                  ('q','l'), ('m','c'), ('f','n'), 
                                  ('k','p'), ('o','b'), ('t','d'), 
                                  ('s','i')]
        
        self.val_six_shuffler = [('l','w'), ('p','b'), ('j','t'), 
                                 ('m','h'), ('z','v'), ('o','c'), 
                                 ('y','e'), ('q','k'), ('f','d'), 
                                 ('n','g'), ('i','x'), ('a','s'), 
                                 ('u','r')]
        
        self.val_seven_shuffler = [('w','u'), ('x','k'), ('y','f'), 
                                   ('z','d'), ('h','p'), ('r','o'), 
                                   ('q','v'), ('i','t'), ('s','a'), 
                                   ('m','g'), ('l','e'), ('n','j'), 
                                   ('c','b')]
        
        self.val_eight_shuffler = [('r','s'), ('b','k'), ('a','w'), 
                                   ('u','o'), ('q','c'), ('f','p'), 
                                   ('i','h'), ('m','j'), ('x','v'), 
                                   ('n','d'), ('z','e'), ('l','y'), 
                                   ('g','t')]
        
        self.val_nine_shuffler = [('j','l'), ('p','w'), ('n','m'), 
                                  ('v','s'), ('e','b'), ('c','k'), 
                                  ('z','q'), ('u','o'), ('d','x'), 
                                  ('f','y'), ('i','a'), ('t','r'), 
                                  ('g','h')]
        
        self.val_ten_shuffler = [('z','j'), ('m','r'), ('h','x'), 
                                 ('o','f'), ('t','k'), ('a','v'), 
                                 ('e','y'), ('p','b'), ('d','n'), 
                                 ('l','g'), ('i','u'), ('q','s'), 
                                 ('c','w')]
        
        self.val_eleven_shuffler = [('s','d'), ('g','a'), ('k','c'), 
                                    ('r','j'), ('e','y'), ('z','p'), 
                                    ('u','v'), ('m','f'), ('t','i'), 
                                    ('q','x'), ('w','b'), ('h','o'), 
                                    ('l','n')]
        
        self.val_twelve_shuffler = [('o','n'), ('g','z'), ('f','i'), 
                                    ('p','x'), ('b','c'), ('s','j'), 
                                    ('w','q'), ('m','y'), ('r','k'), 
                                    ('h','u'), ('e','v'), ('a','l'), 
                                    ('d','t')]
        
        self.val_thirteen_shuffler = [('y','j'), ('t','k'), ('z','b'), 
                                      ('q','w'), ('u','d'), ('m','l'), 
                                      ('f','r'), ('x','s'), ('n','o'), 
                                      ('h','e'), ('p','v'), ('i','c'), 
                                      ('g','a')]
        
        self.val_fourteen_shuffler = [('y','u'), ('t','x'), ('s','v'), 
                                      ('g','d'), ('q','p'), ('n','b'), 
                                      ('z','r'), ('j','i'), ('o','c'), 
                                      ('e','l'), ('h','a'), ('k','m'), 
                                      ('w','f')]
        
        self.val_fifteen_shuffler = [('j','o'), ('y','t'), ('n','m'), 
                                     ('b','x'), ('r','k'), ('s','z'), 
                                     ('g','l'), ('u','v'), ('p','d'), 
                                     ('q','w'), ('f','c'), ('a','e'), 
                                     ('i','h')]
        
        self.val_sixteen_shuffler = [('m','q'), ('c','z'), ('p','o'), 
                                     ('v','s'), ('k','g'), ('u','w'), 
                                     ('d','r'), ('y','n'), ('i','e'), 
                                     ('a','f'), ('j','b'), ('h','x'), 
                                     ('t','l')]
        
        self.val_seventeen_shuffler = [('w','x'), ('o','m'), ('h','a'), 
                                       ('z','p'), ('s','f'), ('r','y'), 
                                       ('j','v'), ('t','l'), ('d','b'), 
                                       ('k','c'), ('e','g'), ('u','i'), 
                                       ('n','q')]
        
        self.val_eighteen_shuffler = [('t','n'), ('e','s'), ('b','v'), 
                                      ('g','x'), ('d','j'), ('l','m'), 
                                      ('h','p'), ('r','k'), ('q','z'), 
                                      ('f','y'), ('w','c'), ('i','a'), 
                                      ('u','o')]
        
        self.val_nineteen_shuffler = [('p','c'), ('e','i'), ('k','l'), 
                                      ('a','z'), ('y','t'), ('m','g'), 
                                      ('s','n'), ('o','w'), ('x','v'), 
                                      ('f','b'), ('d','q'), ('r','u'), 
                                      ('h','j')]
        
        self.val_twenty_shuffler = [('b','m'), ('r','y'), ('p','h'), 
                                    ('c','k'), ('f','z'), ('v','x'), 
                                    ('s','n'), ('e','l'), ('a','t'), 
                                    ('q','o'), ('i','w'), ('d','u'), 
                                    ('j','g')]
        
        self.val_twenty_one_shuffler = [('w','p'), ('m','i'), ('k','v'), 
                                        ('r','b'), ('s','o'), ('z','u'), 
                                        ('f','g'), ('d','y'), ('a','n'), 
                                        ('h','c'), ('t','e'), ('l','x'), 
                                        ('j','q')]
        
        self.val_twenty_two_shuffler = [('v','f'), ('w','r'), ('s','q'), 
                                        ('g','o'), ('y','x'), ('k','p'), 
                                        ('h','d'), ('n','b'), ('a','m'), 
                                        ('u','z'), ('i','l'), ('t','c'), 
                                        ('e','j')]
        
        self.val_twenty_three_shuffler = [('k','a'), ('v','g'), ('t','w'), 
                                          ('z','d'), ('q','e'), ('x','j'), 
                                          ('o','s'), ('c','b'), ('f','y'), 
                                          ('i','p'), ('n','l'), ('h','u'), 
                                          ('m','r')]
        
        self.val_twenty_four_shuffler = [('w','d'), ('f','s'), ('v','q'), 
                                         ('g','o'), ('h','y'), ('m','b'), 
                                         ('l','k'), ('i','u'), ('j','z'), 
                                         ('a','n'), ('r','p'), ('e','c'), 
                                         ('x','t')]
        
        self.val_twenty_five_shuffler = [('w','x'), ('i','q'), ('f','z'), 
                                         ('y','j'), ('r','p'), ('n','h'), 
                                         ('e','l'), ('o','g'), ('b','c'), 
                                         ('u','s'), ('k','t'), ('m','d'), 
                                         ('v','a')]
        
        self.val_twenty_six_shuffler = [('z','c'), ('x','u'), ('b','h'), 
                                        ('m','y'), ('k','j'), ('w','s'), 
                                        ('o','v'), ('r','l'), ('i','d'), 
                                        ('g','a'), ('n','p'), ('t','f'), 
                                        ('e','q')]
    
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



