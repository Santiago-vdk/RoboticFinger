import sys, os
import ctypes
import re

root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))
language_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'language'))
sys.path.insert(0, language_path)

from antlr4 import *
from RoboticFingerLexer import RoboticFingerLexer
from RoboticFingerParser import RoboticFingerParser
from RoboticFingerListener import RoboticFingerListener
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
       	print(msg + " line: " + str(line) + " column: " + str(column))
        print("SYNTAX ERROR, exiting...")
        sys.exit()



def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):

    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')

    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')

    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)

        #print('shortest path: '+str(path)+" cost="+str(distances[dest]))
        return path

    else :
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        #dijkstra(graph,x,dest,visited,distances,predecessors)
        return dijkstra(graph, x, dest, visited, distances, predecessors)





teclado =  [[7,8,9],    # Se utiliza para manejar el posicionamiento global del dedo
            [4,5,6],
            [1,2,3],
            [0,-1,-1]]

graph = {'7': {'8': 1, '4': 1},
         '8': {'7': 1, '5': 1, '9':1},
         '9': {'8': 1, '6':1,},
         '4': {'7': 1, '5': 1, '1': 1},
         '5': {'8': 1, '4': 1, '6': 1, '2':1},
         '6': {'9': 1, '5': 1, '3': 1},
         '1': {'4': 1, '2': 1, '0': 1},
         '2': {'5': 1, '1': 1, '3': 1},
         '3': {'2': 1, '6': 1},
         '0': {'1': 1}}

dijkstra(graph,'7','8')
dijkstra(graph,'4','8')

#print("----------------------------------------")

def calcular_trayectoria(path):
    i = 0
    j = 0
    k = 1
    camino = []
    while(teclado[i][j] != int(path[-1])):                  # Arreglo de tuplas, cada tupla tiene (X|Y,IZQ|DER,STEPS)
        moved = False                                       # X->M0 = 0. Y->M1 = 1, IZQ = 0, DER = 1, STEPS(calculados)
        if(not moved and j+1<len(teclado[i])):
            if(teclado[i][j+1] == int(path[k])):
                #print("Derecha")
                instruccion = (1,1,3200)
                camino.append(instruccion)
                k += 1
                j += 1
                moved = True
        if(not moved and j-1 >= 0):
            if(teclado[i][j-1] == int(path[k])):
                #print("Izquierda")
                instruccion = (1,1,3200)
                camino.append(instruccion)
                k += 1
                j -= 1
                moved = True
        if(not moved and i+1<len(teclado)):
            if(teclado[i+1][j] == int(path[k])):
                #print("Abajo")
                instruccion = (1,1,3200)
                camino.append(instruccion)
                k += 1
                i += 1
                moved = True
        if(not moved and i-1 >= 0):
            if(teclado[i-1][j] == int(path[k])):
                #print("Arriba")
                instruccion = (1,1,3200)
                camino.append(instruccion)
                k += 1
                i -= 1
                moved = True

        if(not moved):
            print("Camino no encontrado")
    return camino   # Devuelvo la equivalencia en instrucciones de la Biblioteca

tamanio = -1            # Tamaño del teclado a manejar
pos_actual = (0,0)

def seleccionar_teclado(tamanio):
    if(tamanio == "SMALL"):
        tamanio = 2
        print("Teclado definido: SMALL")
    elif(tamanio == "MEDIUM"):
        tamanio = 3
        print("Teclado definido: MEDIUM")
    elif(tamanio == "LARGE"):
        tamanio = 5
        print("Teclado definido: LARGE")
    else:
        print("Error inesperado seleccionando teclado!")
        sys.exit()



def main(argv):

    if len(argv) < 3:
        print("Favor especificar archivo de configuracion y un tamaño SMALL | MEDIUM | LARGE")
        sys.exit()

    input = FileStream(argv[1])
    lexer = RoboticFingerLexer(input)

    lexer.removeErrorListeners()
    lexer._listeners = [ MyErrorListener() ]

    stream = CommonTokenStream(lexer)
    parser = RoboticFingerParser(stream)
    parser._listeners = [ MyErrorListener() ]

    tree = parser.roboticfinger()

    listen = RoboticFingerListener()
    walker = ParseTreeWalker()
    walker.walk(listen, tree)

    tam_teclado = argv[2]
    if(tam_teclado == "small" or tam_teclado == "SMALL"):
        seleccionar_teclado("SMALL")
    elif(tam_teclado == "medium" or tam_teclado == "MEDIUM"):
        seleccionar_teclado("MEDIUM")
    elif(tam_teclado == "large" or tam_teclado == "LARGE"):
        seleccionar_teclado("LARGE")
    else:
        print("Tamaño de teclado indefinido (SMALL | MEDIUM | LARGE)")
        sys.exit()

    print("Ejecutando secuencia...\n")
    with open(root_path + "/configuration") as fp:
        for line in fp:

            command = line.split(' ')

            if(command[0] == "DRAG"):
                print("Ejecutando DRAG")

                desde = teclado[ pos_actual[0] ][ pos_actual[1] ]
                hasta = teclado[ int(command[1]) ][ int(command[2]) ]
                print("Desde " + str(desde) + ", Hasta " + str(hasta))
                if(desde != hasta):

                    path = dijkstra(graph,str(desde),str(hasta))
                    path = path[::-1]

                    print("Camino a seguir: " + str(path))
                    instrucciones = calcular_trayectoria(path)

                    for instruccion in instrucciones:                   # Arreglo de tuplas, cada tupla tiene (X|Y,IZQ|DER,STEPS)

                        if(ctypes.CDLL(root_path + '/library/lib.so').drag(instruccion[0],instruccion[1],instruccion[2]) < 0):
                            print("Error ejecutando instruccion DRAG")
                            #sys.exit()
                else:
                    print("DRAG IGNORADO")

            elif(command[0] == "PUSH"):
                print("Ejecutando PUSH")
                if(ctypes.CDLL(root_path + '/library/lib.so').push(command[1]) < 0):
                    print("Error ejecutando instruccion PUSH")
                    #sys.exit()

            elif(command[0] == "TOUCH"):
                print("Ejecutando TOUCH")
                if(ctypes.CDLL(root_path + '/library/lib.so').touch() < 0):
                    print("Error ejecutando instruccion TOUCH")
                    #sys.exit()
            else:
                print("Error inesperado detectando instrucciones!")
                sys.exit()



if __name__ == '__main__':
    main(sys.argv)
