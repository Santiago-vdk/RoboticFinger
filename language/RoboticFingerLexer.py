# Generated from RoboticFinger.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\6\2/\n\2\r\2\16\2\60")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\5\26d\n\26\3\26\3\26\6\26h\n\26\r\26\16\26")
        buf.write("i\2\2\27\3\3\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2")
        buf.write("\27\2\31\2\33\2\35\2\37\2!\4#\5%\6\'\7)\b+\t\3\2\20\4")
        buf.write("\2CCcc\4\2EEee\4\2FFff\4\2RRrr\4\2IIii\4\2TTtt\4\2UUu")
        buf.write("u\4\2[[{{\4\2JJjj\4\2QQqq\4\2WWww\4\2VVvv\3\2c|\3\2C\\")
        buf.write("\2`\2\3\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3.\3\2\2\2\5\62\3\2\2\2\7")
        buf.write("\64\3\2\2\2\t\66\3\2\2\2\138\3\2\2\2\r:\3\2\2\2\17<\3")
        buf.write("\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25B\3\2\2\2\27D\3\2\2\2")
        buf.write("\31F\3\2\2\2\33H\3\2\2\2\35J\3\2\2\2\37L\3\2\2\2!N\3\2")
        buf.write("\2\2#P\3\2\2\2%V\3\2\2\2\'[\3\2\2\2)`\3\2\2\2+g\3\2\2")
        buf.write("\2-/\5!\21\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3")
        buf.write("\2\2\2\61\4\3\2\2\2\62\63\t\2\2\2\63\6\3\2\2\2\64\65\t")
        buf.write("\3\2\2\65\b\3\2\2\2\66\67\t\4\2\2\67\n\3\2\2\289\t\5\2")
        buf.write("\29\f\3\2\2\2:;\t\6\2\2;\16\3\2\2\2<=\t\7\2\2=\20\3\2")
        buf.write("\2\2>?\t\b\2\2?\22\3\2\2\2@A\t\t\2\2A\24\3\2\2\2BC\t\n")
        buf.write("\2\2C\26\3\2\2\2DE\t\13\2\2E\30\3\2\2\2FG\t\f\2\2G\32")
        buf.write("\3\2\2\2HI\t\r\2\2I\34\3\2\2\2JK\t\16\2\2K\36\3\2\2\2")
        buf.write("LM\t\17\2\2M \3\2\2\2NO\4\62;\2O\"\3\2\2\2PQ\5\33\16\2")
        buf.write("QR\5\27\f\2RS\5\31\r\2ST\5\7\4\2TU\5\25\13\2U$\3\2\2\2")
        buf.write("VW\5\13\6\2WX\5\31\r\2XY\5\21\t\2YZ\5\25\13\2Z&\3\2\2")
        buf.write("\2[\\\5\t\5\2\\]\5\17\b\2]^\5\5\3\2^_\5\r\7\2_(\3\2\2")
        buf.write("\2`a\7\"\2\2a*\3\2\2\2bd\7\17\2\2cb\3\2\2\2cd\3\2\2\2")
        buf.write("de\3\2\2\2eh\7\f\2\2fh\7\17\2\2gc\3\2\2\2gf\3\2\2\2hi")
        buf.write("\3\2\2\2ig\3\2\2\2ij\3\2\2\2j,\3\2\2\2\7\2\60cgi\2")
        return buf.getvalue()


class RoboticFingerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_NUMBER = 1
    DIGIT = 2
    TOUCH = 3
    PUSH = 4
    DRAG = 5
    WHITESPACE = 6
    NEWLINE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT_NUMBER", "DIGIT", "TOUCH", "PUSH", "DRAG", "WHITESPACE", 
            "NEWLINE" ]

    ruleNames = [ "INT_NUMBER", "A", "C", "D", "P", "G", "R", "S", "Y", 
                  "H", "O", "U", "T", "LOWERCASE", "UPPERCASE", "DIGIT", 
                  "TOUCH", "PUSH", "DRAG", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "RoboticFinger.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


