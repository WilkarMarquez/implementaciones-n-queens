from board import Board
from testRead import readBoard
import numpy, time, pandas
from showSolution import show

def repetead(adjacent, path):
    for i in adjacent:
        for j in path:
            if(numpy.array_equal(i,j)):
                adjacent.remove(i)
                break
    return adjacent

def isSolution(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if(j > i):
                if(abs(state[i] - state[j]) == abs(i-j) or state[i] == state[j]):
                    return False
    return True

def nextState(state):
    totalState = list()
    nextState = state.copy()
    for i in range(len(state)):
        #arriba
        if(limitBoard(state[i]-1, len(state)) and state.count(state[i]-1) <= 1):
            nextState[i] = state[i] - 1
            #print(nextState, 'arriba')
            totalState.append(nextState)
            nextState = state.copy()
        #abajo
        if(limitBoard(state[i]+1, len(state)) and state.count(state[i]+1) <= 1):
            nextState[i] = state[i] + 1
            #print(nextState, 'abajo')
            totalState.append(nextState)
            nextState = state.copy()
    #print('adj',totalState)
    return totalState

def limitBoard(num, tam):
    return (num <tam) and (num >= 0)

def nearState(state):
        near_states = []
        tam = len(state)-1
        for col1 in range(len(state)):
            for row in range(len(state)):
                if row != state[col1]:
                    aux = list(state)
                    aux[col1] = row
                     
                    #if((aux[0] != 0 or aux[0] != tam) and (aux[-1] != 0 or aux[-1] != tam)):
                    if(countDia(aux, tam) <= 1):
                        if(aux.count(aux[col1]) <= 2):
                            near_states.append(list(aux))
        #print(near_states)
        return near_states

def countDia(aux, tam):
    count = 0
    if(aux[0] == 0 or aux[0] == tam):
        count += 1
    if(aux[-1] == 0 or aux[-1] == tam):
        count += 1
    return count

#print(nearState([0,1,2,2]))

nodes, st, end = 0, 0, 0

def bfs_paths(start):
    queue = [(start, [start])]
    global st, end
    st = time.time()
    visited = []
    while queue:
        (vertex, path) = queue.pop(0)     
        if(vertex not in visited):
            global nodes  
            nodes += 1
            visited.append(vertex)
            #print(vertex)
            #print('visitados', visited)
            adjacent = nearState(vertex)
            #print('adj',adjacent)
            lis = repetead(adjacent, visited)
            #print('sin repe', lis)
            #print(len(visited),(len(lis)+len(adjacent)))
            print(vertex, nodes)
            for next in lis:
                if isSolution(next):
                    end = time.time()
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

# aqui se lee el archivo para ellos especifique la hoja que se quiere 
# leer en el segundo parametro de la función ej: N=4,N=8

start = Board(readBoard('Tableros1.xlsx', 'N=4'))
solution = next(bfs_paths(start.position))
print('solución',solution)
print('Nodos expandidos BFS:', nodes)
print('Tiempo,', end - st, 'segundos')
show('Solucion BFS',solution[-1], nodes, end - st)
