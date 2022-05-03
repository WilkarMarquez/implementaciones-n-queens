import random as r, numpy as np, time, math
from testRead import readBoard
from showSolution import *

class Board:
 
    def __init__(self, board):
        self.quenns = board

    def stateActual(self):
        return self.quenns
    
    def mostrar(self):
        for i in range(len(self.quenns)):
            for j in range(len(self.quenns)):
                if self.quenns[j] == i:
                    print('Q',end=" ")
                else:
                    print('-', end=" ")
            print()
 
    def generateNeighbor(self, move):
        i = r.randint(0,len(self.quenns)-1)
        neighbor = self.quenns[:]
        while True:
            newLocal = r.randint(0,len(self.quenns)-1)
            if neighbor[i] != newLocal:
                neighbor[i] = newLocal
                break
        return neighbor

    def atribui(self,newState):
        self.quenns = newState

def heuristica(board):
    row = 0
    dia = 0
    for i in range(0,len(board)):
        for j in range(i+1,len(board)):
            if i != j:
                x = abs(i-j)
                y = abs(board[i]-board[j])
                if x == y:
                    dia += 1
            if board[i]==board[j]:
                row += 1

    return row + dia

def simulatedAnnealing(board, numIteration):
    actual = board.stateActual()
    heuActual = heuristica(actual)
    listIteration = []
    listValue = []
    for t in range(1,numIteration):
        temp = 0.75/math.sqrt(t)
        neighbor = board.generateNeighbor(actual)
        heuNeighbor = heuristica(neighbor)
        heuActual = heuristica(actual)
        listIteration.append(t)
        listValue.append(heuActual)
        if temp == 0:
            return actual
        if heuActual == 0:
            global ite
            global val
            val, ite = listValue, listIteration
        elif heuNeighbor <= heuActual:
            board.atribui(neighbor)
            actual = board.stateActual()
        else:
            prob = math.exp((heuActual - heuNeighbor)/temp)
            choices = np.random.choice(['neighbor','actual'],p=[prob,1-prob])
            if choices == 'neighbor':
                board.atribui(neighbor)
            actual = board.stateActual()
    return actual

ite = []
val = []

boardInit = readBoard('Tableros1.xlsx', 'N=12')
sa = Board(boardInit)
startTime =time.time()
result = simulatedAnnealing(sa, numIteration = 5000)
print('state initial:',boardInit)
print('solution found:', result)
print('time of solution found:', time.time() - startTime)
show('Solution with SA', result, time.time() - startTime)
plotConver(ite, val)