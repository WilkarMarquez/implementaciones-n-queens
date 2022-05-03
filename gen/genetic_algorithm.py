import random, time
from showSolution import *
from testRead import readBoard

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

def genIndividual(n):
    return [random.randint(0,n-1) for _ in range(0,n)]

def mutation(individual):
    n = len(individual)-1
    position = random.randint(0,n)
    gen = random.randint(0,n)
    individual[position] = gen
    
    return individual

def crossover(father1,father2):
    n = len(father1)-1
    pointCrossover = random.randint(1,n)
    child = father1[:pointCrossover] + father2[pointCrossover:]
    return child

def matingPool(population, mut):
    newGeneration = []
    for i in range(0,int(len(population)*4)):
        father1 = random.randint(0,len(population)-1)
        father2 = random.randint(0,len(population)-1)
        child = crossover(population[father1],population[father2])
        if random.random() < mut:
            child = mutation(child)
        newGeneration.append(child)
    return newGeneration

def fittestSelection(generation,sizePopulation):
    tmp = sorted(generation, key=heuristica)
    metade = int(sizePopulation/2)
    newPopulation = tmp[:metade]
    ini = random.randint(0,sizePopulation) + metade
    fin = ini + metade 
    newPopulation += tmp[ini:fin]
    return newPopulation

def foundSolution(population):
    menor = heuristica(population[0])
    bestIndividual = population[0]
    for individual in population:
        if heuristica(individual) <= menor:
            bestIndividual = individual
            menor = heuristica(individual)
        if heuristica(individual) == 0:
            return (True, individual)

    return (False,bestIndividual)


sol, ite, value = [], [], []

def AG(boardInitial, populationSize, eliteSize, mutationRate, generations):
    population = []
    i = 0
    while i < populationSize:
        population.append(genIndividual(len(boardInitial)))
        i+=1
    current = foundSolution(population)
    bestCurrent = heuristica(current[1])
    repetido = 0
    global sol
    sol = current[1]
    global ite
    global value
    i=0
    while i < generations:
        ite.append(i)
        newGeneration = matingPool(population,mutationRate)
        population = fittestSelection(newGeneration,populationSize)
        current = foundSolution(population)
        if heuristica(current[1]) == bestCurrent:
            repetido += 1
        else:
            bestCurrent = heuristica(current[1])
            repetido = 0
            mutationRate = 0.03
        if repetido > 10:
            mutationRate += 0.005
        value.append(bestCurrent)
        i += 1
        sol = current[1]

boardInitial = readBoard('Tableros1.xlsx', 'N=12')
print(boardInitial)
starTime = time.time()
AG(boardInitial, populationSize = 100, eliteSize = 20, mutationRate = 0.03, generations = 500)
show('Solution with AG', sol, time.time() - starTime)
plotConver(ite, value)

