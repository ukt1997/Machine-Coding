# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 01:44:55 2022

@author: Ujjwal Kumar

This is Utility File
"""

class Board:
    
    def __init__(self,size=4):
        self.board = [['_']*size]*size
    
    def print_board(self):
        for i in self.board:
            print(i)
            
B = Board(5)
B.print_board()

