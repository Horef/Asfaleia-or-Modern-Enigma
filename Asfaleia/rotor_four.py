#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:49:41 2019

@author: Sergiy Horef
"""
from rotor import Rotor

class Rotor_Four(Rotor):
    
    def __init__(self, nr):
        super().__init__(nr)
        self.val_one_shuffler = [('l','n'), ('x','a'), ('p','d'), 
                                 ('e','s'), ('t','q'), ('z','u'), 
                                 ('i','k'), ('g','w'), ('h','c'), 
                                 ('b','r'), ('f','o'), ('v','m'), 
                                 ('y','j')]
        
        self.val_two_shuffler = [('l','y'), ('s','j'), ('p','i'), 
                                 ('c','t'), ('h','x'), ('v','k'), 
                                 ('r','z'), ('u','d'), ('q','f'), 
                                 ('n','m'), ('o','w'), ('b','a'), 
                                 ('e','g')]
        
        self.val_three_shuffler = [('p','a'), ('e','h'), ('w','g'), 
                                   ('b','z'), ('m','k'), ('l','i'), 
                                   ('x','u'), ('s','t'), ('n','c'), 
                                   ('f','j'), ('y','v'), ('o','d'), 
                                   ('r','q')]
        
        self.val_four_shuffler = [('p','m'), ('l','d'), ('a','c'), 
                                  ('k','w'), ('f','g'), ('h','t'), 
                                  ('x','b'), ('u','j'), ('n','y'), 
                                  ('r','s'), ('z','e'), ('v','o'), 
                                  ('i','q')]
        
        self.val_five_shuffler = [('g','p'), ('i','e'), ('w','q'), 
                                  ('d','y'), ('m','h'), ('v','j'), 
                                  ('l','n'), ('s','k'), ('b','u'), 
                                  ('o','t'), ('r','f'), ('z','a'), 
                                  ('c','x')]
        
        self.val_six_shuffler = [('y','p'), ('z','v'), ('e','i'), 
                                 ('h','l'), ('k','d'), ('q','j'), 
                                 ('s','o'), ('a','u'), ('b','g'), 
                                 ('c','n'), ('f','m'), ('t','r'), 
                                 ('x','w')]
        
        self.val_seven_shuffler = [('j','c'), ('a','b'), ('f','x'), 
                                   ('m','i'), ('y','z'), ('v','r'), 
                                   ('u','t'), ('o','q'), ('d','h'), 
                                   ('g','w'), ('s','n'), ('l','k'), 
                                   ('p','e')]
        
        self.val_eight_shuffler = [('v','g'), ('t','k'), ('w','i'), 
                                   ('e','c'), ('p','h'), ('l','r'), 
                                   ('n','f'), ('b','y'), ('a','q'), 
                                   ('x','o'), ('m','d'), ('s','j'), 
                                   ('z','u')]
        
        self.val_nine_shuffler = [('c','s'), ('x','u'), ('v','y'), 
                                  ('f','b'), ('o','z'), ('m','q'), 
                                  ('e','p'), ('i','t'), ('l','n'), 
                                  ('r','h'), ('w','d'), ('a','g'), 
                                  ('j','k')]
        
        self.val_ten_shuffler = [('o','v'), ('z','j'), ('m','w'), 
                                 ('d','s'), ('l','q'), ('e','c'), 
                                 ('p','r'), ('n','x'), ('h','i'), 
                                 ('g','u'), ('k','t'), ('f','y'), 
                                 ('a','b')]
        
        self.val_eleven_shuffler = [('q','o'), ('z','w'), ('d','u'), 
                                    ('i','h'), ('j','c'), ('a','y'), 
                                    ('p','e'), ('x','r'), ('n','m'), 
                                    ('s','g'), ('v','f'), ('t','l'), 
                                    ('b','k')]
        
        self.val_twelve_shuffler = [('f','a'), ('b','u'), ('z','g'), 
                                    ('c','m'), ('d','p'), ('l','h'), 
                                    ('q','t'), ('v','r'), ('j','o'), 
                                    ('i','e'), ('y','s'), ('k','x'), 
                                    ('n','w')]
        
        self.val_thirteen_shuffler = [('e','z'), ('m','l'), ('p','o'), 
                                      ('u','d'), ('c','x'), ('h','w'), 
                                      ('g','r'), ('f','k'), ('v','q'), 
                                      ('y','j'), ('s','a'), ('n','i'),
                                      ('t','b')]
        
        self.val_fourteen_shuffler = [('p','t'), ('o','d'), ('m','f'), 
                                      ('b','i'), ('r','v'), ('k','e'), 
                                      ('n','a'), ('g','w'), ('x','y'), 
                                      ('j','c'), ('z','q'), ('u','h'), 
                                      ('l','s')]
        
        self.val_fifteen_shuffler = [('d','s'), ('g','o'), ('i','j'), 
                                     ('h','p'), ('c','x'), ('b','a'), 
                                     ('e','l'), ('q','m'), ('n','y'), 
                                     ('z','r'), ('k','t'), ('w','f'), 
                                     ('v','u')]
        
        self.val_sixteen_shuffler = [('n','x'), ('q','i'), ('f','e'), 
                                     ('o','y'), ('m','l'), ('z','s'), 
                                     ('a','u'), ('t','k'), ('w','g'), 
                                     ('v','j'), ('h','c'), ('r','p'), 
                                     ('d','b')]
        
        self.val_seventeen_shuffler = [('p','x'), ('u','o'), ('v','n'), 
                                       ('z','i'), ('b','f'), ('g','d'), 
                                       ('a','c'), ('j','r'), ('s','t'), 
                                       ('k','l'), ('y','h'), ('e','q'), 
                                       ('m','w')]
        
        self.val_eighteen_shuffler = [('t','g'), ('z','r'), ('u','d'), 
                                      ('n','b'), ('j','x'), ('o','a'), 
                                      ('e','s'), ('h','k'), ('i','p'), 
                                      ('c','w'), ('m','v'), ('l','f'), 
                                      ('q','y')]
        
        self.val_nineteen_shuffler = [('t','w'), ('x','k'), ('d','n'), 
                                      ('g','v'), ('p','r'), ('q','o'), 
                                      ('e','z'), ('y','l'), ('s','j'), 
                                      ('f','m'), ('h','i'), ('b','c'), 
                                      ('u','a')]
        
        self.val_twenty_shuffler = [('f','p'), ('o','q'), ('c','d'), 
                                    ('t','y'), ('i','x'), ('w','r'), 
                                    ('a','h'), ('m','b'), ('u','e'), 
                                    ('n','z'), ('v','l'), ('j','g'), 
                                    ('k','s')]
        
        self.val_twenty_one_shuffler = [('z','x'), ('t','d'), ('o','u'), 
                                        ('r','s'), ('q','y'), ('w','e'), 
                                        ('n','h'), ('b','j'), ('p','c'), 
                                        ('g','m'), ('a','l'), ('i','f'), 
                                        ('k','v')]
        
        self.val_twenty_two_shuffler = [('u','g'), ('c','w'), ('j','k'), 
                                        ('b','l'), ('q','d'), ('y','o'), 
                                        ('n','r'), ('t','m'), ('v','f'), 
                                        ('p','s'), ('e','x'), ('h','z'), 
                                        ('a','i')]
        
        self.val_twenty_three_shuffler = [('k','m'), ('l','a'), ('w','q'), 
                                          ('h','s'), ('t','v'), ('b','f'), 
                                          ('n','o'), ('d','c'), ('x','i'), 
                                          ('r','u'), ('z','e'), ('j','p'), 
                                          ('g','y')]
        
        self.val_twenty_four_shuffler = [('y','x'), ('z','s'), ('f','k'), 
                                         ('g','b'), ('u','a'), ('h','c'), 
                                         ('v','o'), ('e','q'), ('j','d'), 
                                         ('r','t'), ('i','m'), ('p','l'), 
                                         ('w','n')]
        
        self.val_twenty_five_shuffler = [('i','b'), ('d','c'), ('f','u'), 
                                         ('k','x'), ('l','g'), ('w','n'), 
                                         ('e','v'), ('r','y'), ('j','t'), 
                                         ('q','a'), ('z','o'), ('p','s'), 
                                         ('h','m')]
        
        self.val_twenty_six_shuffler = [('g','a'), ('v','y'), ('h','j'), 
                                        ('b','o'), ('p','e'), ('l','n'), 
                                        ('x','u'), ('c','t'), ('z','w'), 
                                        ('k','f'), ('i','s'), ('d','r'), 
                                        ('q','m')]
    
        self.shuffler_dict = {
                1: self.val_one_shuffler,
                2: self.val_two_shuffler,
                3: self.val_three_shuffler,
                4: self.val_four_shuffler,
                5: self.val_five_shuffler,
                6: self.val_six_shuffler,
                7: self.val_seven_shuffler,
                8: self.val_eight_shuffler,
                9: self.val_nine_shuffler,
                10: self.val_ten_shuffler,
                11: self.val_eleven_shuffler,
                12: self.val_twelve_shuffler,
                13: self.val_thirteen_shuffler,
                14: self.val_fourteen_shuffler,
                15: self.val_fifteen_shuffler,
                16: self.val_sixteen_shuffler,
                17: self.val_seventeen_shuffler,
                18: self.val_eighteen_shuffler,
                19: self.val_nineteen_shuffler,
                20: self.val_twenty_shuffler,
                21: self.val_twenty_one_shuffler,
                22: self.val_twenty_two_shuffler,
                23: self.val_twenty_three_shuffler,
                24: self.val_twenty_four_shuffler,
                25: self.val_twenty_five_shuffler,
                26: self.val_twenty_six_shuffler
        }
    
    def shuffle_letters(self, letters):
        for pair in self.shuffler_dict[self.current_value]:
                letters[pair[0]], letters[pair[1]] = letters[pair[1]], letters[pair[0]]

    
    def __str__(self):
        return 'This is a {self.__class__.__name__} with a value of {self.current_value}'.format(self=self)
    
    def __repr__(self):
        return '{self.__class__.__name__}({self.next_rotor})'.format(self=self)
