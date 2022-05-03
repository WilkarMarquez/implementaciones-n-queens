import matplotlib.pyplot
import matplotlib.ticker as ticker

def show(algoritmo, solution, nodes, time):
    x = []
    y = []
    auxX = []
    auxY = []
    for i in range(len(solution)):
        auxX.append(i)
        auxY.append(i)
        x.append(i+0.5)
        y.append(solution[i]+0.5 )
    matplotlib.pyplot.title(algoritmo+' en '+str(time)[0:7] +' segundos expandiendo '+str(nodes) + ' nodos' )   
    matplotlib.pyplot.axis([0,len(solution),len(solution),0])     
    matplotlib.pyplot.grid()
    matplotlib.pyplot.xticks(auxX)
    matplotlib.pyplot.yticks(auxY)
    matplotlib.pyplot.plot(x, y,'X')
    matplotlib.pyplot.show()
    print