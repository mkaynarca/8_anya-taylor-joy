#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:49:36 2021

@author: mkaynarca
"""

n = 8
x=2
y=3


def createBoard(n:int) -> list:
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[-1].append(["O"])
    return board

def createAvailable(n:int) -> list:
    availableBoard = []
    for i in range(n):
        availableBoard.append([])
        for j in range(n):
            availableBoard[-1].append([True])
    return availableBoard

def placeQueen(board:list, x:int, y:int) -> list:
    board[y][x] = ["X"]
    return board
    
def checkAvailable(board:list, availableBoard:list) -> list:
    temp = availableBoard
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ['X']:
                for k in range(len(board)):
                    temp[i][k] = False
                for l in range(len(board)):
                    temp[l][j] = False
                for m in range(len(board)):
                    for n in range(len(board)):
                        if (m-n==i-j):
                            temp[m][n] = False
                        if (m+n==i+j):
                            temp[m][n] = False
    return temp
                        
                    

# board = createBoard(n)

# available = createAvailable(n)

# placeQueen(board, x, y)

# check = checkAvailable(board, available)