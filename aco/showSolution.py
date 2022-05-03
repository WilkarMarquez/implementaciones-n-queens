import matplotlib.pyplot as plt

def show(algoritmo, solution, time):
    x = []
    y = []
    auxX = []
    auxY = []
    for i in range(len(solution)):
        auxX.append(i)
        auxY.append(i)
        x.append(i+0.5)
        y.append(solution[i]+0.5 )
    plt.title(algoritmo+' in '+str(time)[0:7] +' seconds')   
    plt.axis([0,len(solution),len(solution),0])     
    plt.grid()
    plt.xticks(auxX)
    plt.yticks(auxY)
    plt.plot(x, y,'X')
    plt.show()
    print

def plotConver(ite, value):
    plt.title('AG: convergence graph')
    plt.plot(ite, value)
    plt.ylabel('Number of attacks')
    plt.xlabel('Iteration')
    plt.show()