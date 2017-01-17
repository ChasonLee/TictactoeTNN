# -*- coding: utf-8 -*-
__author__ = 'Chason'
import random

class GameBoard:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM
        self.PLAYER1_NUM = 1
        self.PLAYER2_NUM = 2
        self.PLAYER1_CHAR = '#'
        self.PLAYER2_CHAR = '*'
        self.MAPS = '.'
        self.turns = 0
        self.board = [0 for i in range(ROW * COL)]

    def PrintPiece(self, inx):
        if inx == self.PLAYER1_NUM:
            print self.PLAYER1_CHAR,
        elif inx == self.PLAYER2_NUM:
            print self.PLAYER2_CHAR,
        else:
            print self.MAPS,

    def ShowBoard(self):
        for i, p in enumerate(self.board):
            self.PrintPiece(p)
            if (i + 1) % self.COL == 0:
                print
        print

    def Move(self, loc, player):
        if 0 <= loc < self.ROW * self.COL:
            if self.board[loc] == 0:
                self.board[loc] = player
                return True
            else:
                print "Occupy error: location %d is not empty."
                return False
        else:
            print "Location error: can not move to %d."%loc
            return False

    def RndMove(self, player):
        rnd = int(self.ROW * self.COL * random.random())
