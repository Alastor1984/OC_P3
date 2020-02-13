#! /usr/bin/env python3.6
# coding: utf-8

import random

class Gameboard(object):
    """ Gameboard initialisation and modification """
    SPRITES = 15
    
    def __init__(self):
        self.board = [[0]*self.SPRITES for c in range(self.SPRITES)]
    
    def put_agent(self, pos, agent):
        self.board[agent.pos.x][agent.pos.y] = agent.name

    def _main_path(self):
        pass

    def __str__(self):
        for c in range(self.SPRITES):
            for l in range(self.SPRITES):
                print(self.board[l][c], end = " ")
            print()
        return "Here is the actually board"

class Agent(object):
    """docstring for Agent"""
    def __init__(self,  name, pos):
        self.name = name
        self.pos = pos

class Position(object):
    """ Define position in cartesian coordinates """
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "la position est (x,y)"

def main():
    board = Gameboard()
    pos_mcg = Position(random.randint(0,board.SPRITES-1), 0)
    pos_guard = Position(random.randint(0,board.SPRITES-1), board.SPRITES-1)
    mcg = Agent("M", pos_mcg)
    guard = Agent("G", pos_guard)

    board.put_agent(mcg)
    board.put_agent(guard)
    print(board)

main()