# -*- coding: utf-8 -*-

#%%
from random import randint,uniform
import math
import numpy, time
from testRead import readBoard as b
from showSolution import *
"""def randomAnts(size):
    return [randint(1,nVezir) for _ in range(nVezir)]
"""

def fitness(ant):
    horizontalCollisions=sum([ant.count(queen)-1 for queen in ant])/2
    diagonalCollisions=0
    n=len(ant)
    leftDiagonal=[0]*2*n
    rightDiagonal=[0]*2*n
    for i in range(n):
        leftDiagonal[i+ant[i]-1]+=1
        rightDiagonal[len(ant)-i+ant[i]-2]+=1
    diagonalCollisions=0
    for i in range(2*n-1):
        counter=0
        if leftDiagonal[i]>1:
            counter+=leftDiagonal[i]-1
        if rightDiagonal[i]>1:
            counter+=rightDiagonal[i]-1
        diagonalCollisions+=counter/(n-abs(i-n+1))
    return int(maxFitness-(horizontalCollisions+diagonalCollisions))


def printAnts(ants):
    print("Ants = {},fitness = {}".format(ants,fitness(ants)))
    

def changed(x):
    n=len(x)
    c=randint(0,n-1)
    m=randint(1,n)
    x[c]=m
    return x

def globalPhremone(ants):
    changed(ants)
    changed(ants)
    return ants

def localPhremone(ants):
    changed(ants)
    return ants

if __name__ == "__main__":

    tablero=b('Tableros1.xlsx','N=12')
    start=time.time()
    nVezir = len(tablero)
    iteration=100
    maxFitness=(nVezir*(nVezir-1))/2
    worstAnts=int(0.2*nVezir)
    bestAnts=int(0.6*nVezir)
    print(maxFitness)
    print(worstAnts)
    print(bestAnts)
    print(bestAnts)
    exit()
    alfa=2
    beta=2
    passMax=10
    generation=1
    passMin=0
    transitionProbability=0.9 # geçiş olasılığı
    passMethod=int(alfa*1/nVezir*beta*(passMax-passMin))
    temp=[]
    for x in range(nVezir):
        for y in range(nVezir):
            if(tablero[y][x]=='x' or tablero[y][x]=='X'):
                temp.append(y+1)
    print(temp)
    ants = [temp for _ in range(iteration)]
    ants.sort(key=lambda x : x[1])
    while not maxFitness in [fitness(ant) for ant in ants]:
        print("==Generation == ".format(generation))
        print("Maximum fitness = {}".format(max([fitness(n) for n in ants])))
        generation+=1
        goAnts = ants[randint(0,bestAnts)]
        randomAntsIndex = randint(0,passMethod)
        if (numpy.random.random() < transitionProbability):
            morePowerfulAnts = localPhremone(goAnts)
            if (ants[randomAntsIndex][1] > morePowerfulAnts[1]):
                ants[randomAntsIndex] = morePowerfulAnts
        else:
            for i in range(nVezir-worstAnts,nVezir):
                ants[i] = localPhremone(ants[i])
            ants.sort(key=lambda x : x[1])
        lowCostAnts = ants[0]
        effectlyGlobalAnts = globalPhremone(lowCostAnts)
        if (ants[0][1] > effectlyGlobalAnts[1]):
            ants[0] = effectlyGlobalAnts
        ants.sort(key=lambda x : x[1])
    
    antsOut = []
    for ant in ants:
        if fitness(ant) == maxFitness:
            antsOut = ant
            printAnts(ant)
    board = []
    for x in range(nVezir):
        board.append([" X "]*nVezir)
    
    for i in range(nVezir):
        board[nVezir-antsOut[i]][i] = " V "
    
    def printBoard(board):
        for row in board:
            print("".join(row))
    
    end=time.time()
    show('Solution with AG', [0,1,2,3], end - start)
    printBoard(board)
        

