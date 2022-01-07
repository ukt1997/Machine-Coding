# -*- coding: utf-8 -*-
"""
Spyder Editor

This is Main script file.
"""
import utility as utl



def print_board():
    for i in board:
        print(i)


print("This is Inner Board")
board = [['_']*4]*4
print_board()



print("This is created Using Calss ")
B = utl.Board(5)
B.print_board()
