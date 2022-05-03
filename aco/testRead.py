import pandas, numpy

def readBoard(path, sheetName):
    try:
        archive = pandas.read_excel(path, sheet_name = sheetName, header = None)
    except Exception:
        print('No such file or directory')
        exit()
    else:
        return validateBoard(archive)

def validateBoard(board):
    tamBoard = numpy.shape(board)
    #tamBoard[0] corresponde a las filas y tamBoard[1] a las columnas
    if(tamBoard[0] == tamBoard[1]):
        cantQueens = 0
        for i in range(tamBoard[0]):
            for j in range(tamBoard[1]):
                if(board[i][j] == 'x' or board[i][j] == 'X'):
                    cantQueens += 1
                    if(cantQueens > tamBoard[0]):
                        print('number of queens exceeds the limit')
                        exit()
                else:
                    try:
                        not numpy.isnan(board[i][j])
                    except Exception:
                        print('board with wrong characters')
                        exit()
                        #si entra aquì hay un string diferente a la representacion de una reina
                    else:
                        if(not numpy.isnan(board[i][j])):
                            print('board with wrong characters')
                            exit()
                            #si entra aqui hay numeros
                    #si no entra a ningun lado la celda està vacia en el excel
        if(cantQueens < tamBoard[0]):
            print('number of queens is insufficient')
            exit()
        return board    
    else:
        print('wrong board size, enter NxN board')
        exit()