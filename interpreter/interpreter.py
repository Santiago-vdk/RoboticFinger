import sys, os
import ctypes
import re


root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))
language_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'language'))
sys.path.insert(0, language_path)


def main():
        TestLib = ctypes.cdll.LoadLibrary(root_path + '/library/lib.o')
        print(TestLib.hello())





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


def main(argv):
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

    print("Ejecutando secuencia...\n")

    with open(root_path + "/configuration") as fp:
        for line in fp:
            
            
           
            command = line.split(' ')

            if(command[0] == "TOUCH"):
                print("Ejecutando TOUCH")
                if(ctypes.CDLL(root_path + '/library/lib.so').mov(0,0,int(command[2])) < 0):
                    print("Error ejecutando comando TOUCH")

            elif(command[0] == "PUSH"):
                print("Ejecutando PUSH")
                if(ctypes.CDLL(root_path + '/library/lib.so').mov(0,1,int(command[2])) < 0):
                    print("Error ejecutando comando PUSH")

            elif(command[0] == "DRAG"):
                print("Ejecutando DRAG")
                if(ctypes.CDLL(root_path + '/library/lib.so').mov(0,1,int(command[2])) < 0):
                    print("Error ejecutando comando PUSH")
            
        
    
 
if __name__ == '__main__':
    main(sys.argv)
