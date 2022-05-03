import numpy

class Board(object):
    def __init__(self, board):
        self.position = board #vector inicial
        self.tamBoard = len(board)