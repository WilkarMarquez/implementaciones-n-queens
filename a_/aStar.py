import numpy, time, heapq, sys
from testRead import readBoard
from board import Board
from showSolution import show

class AStar(object,):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.initial = None
        self.solution = None

    def nearState(self, state):
        near_states = []
        tam = len(state)-1
        for col1 in range(len(state)):
            for row in range(len(state)):
                if row != state[col1]:
                    aux = list(state)
                    aux[col1] = row
                     
                    #if((aux[0] != 0 or aux[0] != tam) and (aux[-1] != 0 or aux[-1] != tam)):
                    if(self.countDia(aux, tam) <= 1):
                        if(aux.count(aux[col1]) <= 2):
                            near_states.append(Board(aux))
        #print(near_states)
        return near_states

    def countDia(self,aux, tam):
        count = 0
        if(aux[0] == 0 or aux[0] == tam):
            count += 1
        if(aux[-1] == 0 or aux[-1] == tam):
            count += 1
        return count

    def limitBoard(self, num, tam):
        return (num < tam) and (num >= 0)

    def getHeuristic(self, state):
        attacks = 0
        auxUp, auxDown, auxRow = False, False, False
        for i in range(len(state)):
            for j in range(len(state)):
                if(j > i):
                    #arriba
                    if(abs(state[i] - state[j]) == abs(i-j) and state[i] < state[j] and not auxUp):
                        attacks += 1
                        auxUp = True
                    #abajo
                    if(abs(state[i] - state[j]) == abs(i-j) and state[i] > state[j] and not auxDown):
                        attacks += 1
                        auxDown = True
                    #fila
                    if(state[i] == state[j] and not auxRow):
                        attacks += 1
                        auxRow = True
            auxUp, auxDown, auxRow = False, False, False
        return attacks

    def getCost(self, adj, board):
        for i in range(len(board.position)):
                if(board.position[i] != adj.position[i]):
                    return abs(board.position[i] - adj.position[i])*.1

    def isSolution(self, state):
        for i in range(len(state)):
            for j in range(len(state)):
                if(j > i):
                    if(abs(state[i] - state[j]) == abs(i-j) or state[i] == state[j]):
                        return False
        return True

    def updateBoard(self, adj, board):
        adj.cost = board.cost + self.getCost(adj, board)
        adj.heu = self.getHeuristic(adj.position)
        adj.parent = board
        adj.func = adj.heu + adj.cost

    def printPath(self):
        board = self.solution
        while board.parent:
            board = board.parent
            print('solution:', board.position, board.func, board.heu, board.cost)

    def process(self, stateInit):

        count = 0
        global st, end
        st = time.time()
        heapq.heappush(self.opened, (stateInit.func, count, stateInit))
        self.initial = stateInit.position
        while len(self.opened):
            f, c, board = heapq.heappop(self.opened)
            self.closed.add(board)
            if (self.isSolution(list(board.position))):
                end = time.time()
                self.solution = board
                print('Estado inicial:',stateInit.position) 
                print('Solución',board.position)
                print('nodos expandidos A*:',count)
                print('Tiempo,', end - st, 'segundos')
                show('Solución A*', self.solution.position, count, end - st)
                break
            adjBoards = self.nearState(list(board.position))
            for adjBoard in adjBoards:        
                if adjBoard not in self.closed:
                    if (adjBoard.func, adjBoard) in self.opened:
                        if adjBoard.cost > board.cost:
                            self.updateBoard(adjBoard, board)
                    else:
                        self.updateBoard(adjBoard, board)
                        #print(adjBoard.position, adjBoard.heu, adjBoard.cost)
                        count = count + 1
                        heapq.heappush(self.opened, (adjBoard.func, count, adjBoard))
#><
st, end = 0, 0
# aqui se lee el archivo para ellos especifique la hoja que se quiere 
# leer en el segundo parametro de la función ej: N=4,N=8
boardInitial = Board(readBoard('Tableros1.xlsx', 'N=8'))
a = AStar()
a.process(boardInitial)