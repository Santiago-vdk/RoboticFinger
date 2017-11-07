import sys, os

# Manejan la importacion del lenguaje
language_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'language'))
sys.path.insert(0, language_path)

from antlr4 import *
from RoboticFingerLexer import RoboticFingerLexer
from RoboticFingerParser import RoboticFingerParser

from RoboticFingerListener import RoboticFingerListener
 
def main(argv):
    input = FileStream(argv[1])
    lexer = RoboticFingerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RoboticFingerParser(stream)
    tree = parser.chat()
 
    #output = open("output.html","w")
    
    #htmlChat = HtmlChatListener(output)
    #walker = ParseTreeWalker()
    #walker.walk(htmlChat, tree)

    htmlChat = RoboticFingerListener()
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)
        
    #output.close()      
 
if __name__ == '__main__':
    main(sys.argv)
