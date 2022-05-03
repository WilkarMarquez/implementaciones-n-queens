import numpy

class Board(object):
    def __init__(self, board):
        self.position = board #vector inicial
        self.tamBoard = len(board)
        self.parent = None
        self.heu = 0
        self.cost = 0
        self.func = 0