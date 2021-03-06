import sys, os
import ctypes
import re
import time

root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))
language_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'language'))
sys.path.insert(0, language_path)

from antlr4 import *
from RoboticFingerLexer import RoboticFingerLexer
from RoboticFingerParser import RoboticFingerParser
from RoboticFingerListener import RoboticFingerListener
from antlr4.error.ErrorListener import ErrorListener

distancia = 0

# Listener para errores de sintaxis
# Referencia [30]
class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
       	print(msg + " line: " + str(line) + " column: " + str(column))
        print("SYNTAX ERROR, exiting...")
        sys.exit()


# Metodo para calculo de dijkstra
# Referencias [35] y [36] en documentacion
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
        #print(unvisited)
        #print("min " + str(x))
        #dijkstra(graph,x,dest,visited,distances,predecessors)
        return dijkstra(graph, x, dest, visited, distances, predecessors)


# Matriz encargada de resolver las direcciones que debe tomar el dedo
teclado =  [[7,8,9],
            [4,5,6],
            [1,2,3],
            [0,-1,10]]

# Grafo para calculo del recorrido
graph = {'7': {'8': 1, '4': 1},
         '8': {'7': 1, '5': 1, '9':1},
         '9': {'8': 1, '6':1,},
         '4': {'7': 1, '5': 1, '1': 1},
         '5': {'8': 1, '4': 1, '6': 1, '2':1},
         '6': {'9': 1, '5': 1, '3': 1},
         '1': {'4': 1, '2': 1, '0': 1},
         '2': {'5': 1, '1': 1, '3': 1},
         '3': {'2': 1, '6': 1, '10': 10},
         '0': {'1': 1},
         '10': {'3': 3},
         }


global tamanio
tamanio = -1            # Tamaño del teclado a manejar
#print("----------------------------------------")

# Funcion encargada de traducir el camino mas corto en direcciones/instrucciones
def calcular_trayectoria(path):
    global tamanio
    i = pos_actual[0]
    j = pos_actual[1]
    k = 1
    camino = []
    while(teclado[i][j] != int(path[-1])):                  # Arreglo de tuplas, cada tupla tiene (X|Y,IZQ|DER,STEPS)
        moved = False                                       # X->M0 = 0. Y->M1 = 1, IZQ = 0, DER = 1, STEPS(calculados)
        if(not moved and j+1<len(teclado[i])):
            if(teclado[i][j+1] == int(path[k])):
                #print("ARRIBA")
                #print("I: " + str(i) + " J: " + str(j))                       #    drag(0,1,1000);// Servo flotante derecha
                if(tamanio == 0):
                    instruccion = (1,1,230)
                elif(tamanio == 1):
                    instruccion = (1,1,280)
                else:
                    instruccion = (1,1,320)
                camino.append(instruccion)
                k += 1
                j += 1
                moved = True
        if(not moved and j-1 >= 0):
            if(teclado[i][j-1] == int(path[k])):
                #print("ABAJO")                     #    drag(0,0,1000);	// Servo flotante izquierda
                #print("I: " + str(i) + " J: " + str(j))
                if(tamanio == 0):
                    instruccion = (1,0,230)
                elif(tamanio == 1):
                    instruccion = (1,0,280)
                else:
                    instruccion = (1,0,320)
                camino.append(instruccion)
                k += 1
                j -= 1
                moved = True
        if(not moved and i+1<len(teclado)):
            if(teclado[i+1][j] == int(path[k])):
                #print("DERECHA")                           #   drag(1,0,1000);	// Servo principal hacia atras
                #print("I: " + str(i) + " J: " + str(j))
                if(tamanio == 0):
                    instruccion = (0,1,230)
                elif(tamanio == 1):
                    instruccion = (0,1,280)
                else:
                    instruccion = (0,1,270)
                camino.append(instruccion)
                k += 1
                i += 1
                moved = True
        if(not moved and i-1 >= 0):
            if(teclado[i-1][j] == int(path[k])):
                #print("IZQUIERDA")                            # drag(1,1,1000);	// Servo principal hacia adelante
                #print("I: " + str(i) + " J: " + str(j))
                if(tamanio == 0):
                    instruccion = (0,0,230)
                elif(tamanio == 1):
                    instruccion = (0,0,280)
                else:
                    instruccion = (0,0,270)

                camino.append(instruccion)
                k += 1
                i -= 1
                moved = True

        if(not moved):
            print("Camino no encontrado")
    return camino   # Devuelvo la equivalencia en instrucciones de la Biblioteca


pos_actual = [0,0]

# Validacion para la seleccion d un teclado
def seleccionar_teclado(pTamanio):
    global tamanio
    if(pTamanio == "SMALL"):
        tamanio = 0
        print(bcolors.HEADER + "Teclado definido: SMALL" + bcolors.ENDC)
    elif(pTamanio == "MEDIUM"):
        tamanio = 1
        print(bcolors.HEADER + "Teclado definido: MEDIUM"+ bcolors.ENDC)
    elif(pTamanio == "LARGE"):
        tamanio = 2
        print(bcolors.HEADER + "Teclado definido: LARGE"+ bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Error inesperado seleccionando teclado!" + bcolors.ENDC)
        sys.exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(argv):

    # Llamado para el ajuste de la maquina
    if(argv[1] == "calibrar"):
        print("Iniciando calibrado, verifique el estado inicial de la maquina...")

        if(ctypes.CDLL(root_path + '/library/lib.so').drag(0,0,3400) < 0):
             print("Error ejecutando instruccion DRAG")
             sys.exit()
        if(ctypes.CDLL(root_path + '/library/lib.so').drag(0,1,3400) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()
        if(ctypes.CDLL(root_path + '/library/lib.so').drag(1,1,900) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()
        if(ctypes.CDLL(root_path + '/library/lib.so').touch() < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()

        if(ctypes.CDLL(root_path + '/library/lib.so').drag(1,1,900) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()

        if(ctypes.CDLL(root_path + '/library/lib.so').drag(1,0,900) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()

        if(ctypes.CDLL(root_path + '/library/lib.so').push(2) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()

        if(ctypes.CDLL(root_path + '/library/lib.so').drag(1,0,900) < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()
    # Llamado para el ajuste de la posicion inicial
    elif(argv[1] == "touch"):
        print("Bajando dedo...")

        if(ctypes.CDLL(root_path + '/library/lib.so').touch() < 0):
            print("Error ejecutando instruccion DRAG")
            sys.exit()
    else:
        if len(argv) < 3:
            print(bcolors.FAIL + "Favor especificar archivo de configuracion y un tamaño SMALL | MEDIUM | LARGE" + bcolors.ENDC)
            sys.exit()

        # Etapa de parseo y revision de sintaxis
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


        # Etapa para obtener el tamaño del teclado
        tam_teclado = argv[2]
        if(tam_teclado == "small" or tam_teclado == "SMALL"):
            seleccionar_teclado("SMALL")
        elif(tam_teclado == "medium" or tam_teclado == "MEDIUM"):
            seleccionar_teclado("MEDIUM")
        elif(tam_teclado == "large" or tam_teclado == "LARGE"):
            seleccionar_teclado("LARGE")
        else:
            print(bcolors.FAIL + "Tamaño de teclado indefinido (SMALL | MEDIUM | LARGE)"  + bcolors.ENDC)
            sys.exit()

        # Inicio de la secuencia
        print(bcolors.OKGREEN + "Ejecutando secuencia...\n" + bcolors.ENDC)
        with open(root_path + "/configuration") as fp:  # Se lee la configuracion previamente validada sintacticamente
            for line in fp:
                line = line.rstrip()        # Removemos el \n del archivo
                command = line.split(' ')       # Se separa cada instruccion para procesarse
                #print(len(command[0]))
                if(command[0] == "DRAG"):       # Instruccion DRAG
                    print("Ejecutando DRAG")

                    try:
                        desde = teclado[ pos_actual[0] ][ pos_actual[1] ]   # Direccion desde la que estamos partiendo
                        hasta = teclado[ int(command[1]) ][ int(command[2]) ]   # Direccion a la que deseamos llegar
                    except:
                        print("Error, los rangos de movimiento son invalidos!")
                        sys.exit()
                    print("Desde " + str(desde) + ", Hasta " + str(hasta))
                    if(desde != hasta):                                        # En caso de ya estar en la direccion desda IGNORAR

                        path = dijkstra(graph,str(desde),str(hasta),[],{},{})   # Calculo de dijkstra para obtener el camino mas corto en el grafo
                        path = path[::-1]   # Inversion de la lista obtenida

                        print("Camino a seguir: " + str(path))
                        instrucciones = calcular_trayectoria(path)  # Se traducen el camino que nos retorna dijkstra a su equivalencia en intrucciones de la biblioteca

                        pos_actual[0] = int(command[1])
                        pos_actual[1] = int(command[2])
                        for instruccion in instrucciones:                   # Arreglo de tuplas, cada tupla tiene (X|Y,IZQ|DER,STEPS)
                            #print(instruccion)
                            if(ctypes.CDLL(root_path + '/library/lib.so').drag(instruccion[0],instruccion[1],instruccion[2]) < 0):
                                print("Error ejecutando instruccion DRAG")
                                sys.exit()
                                #pass
                            time.sleep(1)
                        print("")

                    else:
                        print("DRAG IGNORADO")

                elif(command[0] == "PUSH"):
                    print("Ejecutando PUSH " + str(command[1]))
                    if(ctypes.CDLL(root_path + '/library/lib.so').push(int(command[1])) < 0):
                        print("Error ejecutando instruccion DRAG")
                        sys.exit()
                    print("")
                    time.sleep(int(command[1]))
                elif(command[0] == "TOUCH"):
                    print("Ejecutando TOUCH")
                    if(ctypes.CDLL(root_path + '/library/lib.so').touch() < 0):
                        print("Error ejecutando instruccion DRAG")
                        sys.exit()
                    print("")
                    time.sleep(1)
                elif(len(command[0]) == 0 ):
                    # Espacio en blanco
                    print("Ignorando espacio en blanco")
                    print("")
                    pass
                else:
                    print("Error inesperado detectando instrucciones!")
                    sys.exit()
                    pass



if __name__ == '__main__':
    main(sys.argv)
