# Generated from RoboticFinger.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\6\2+\n\2\r\2\16\2,\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\5\24\\\n\24\3\24\3\24\6\24`")
        buf.write("\n\24\r\24\16\24a\2\2\25\3\3\5\2\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\2\33\2\35\4\37\5!\6#\7%\b\'\t")
        buf.write("\3\2\2\2Z\2\3\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3*\3\2\2\2\5.\3")
        buf.write("\2\2\2\7\60\3\2\2\2\t\62\3\2\2\2\13\64\3\2\2\2\r\66\3")
        buf.write("\2\2\2\178\3\2\2\2\21:\3\2\2\2\23<\3\2\2\2\25>\3\2\2\2")
        buf.write("\27@\3\2\2\2\31B\3\2\2\2\33D\3\2\2\2\35F\3\2\2\2\37H\3")
        buf.write("\2\2\2!N\3\2\2\2#S\3\2\2\2%X\3\2\2\2\'_\3\2\2\2)+\5\35")
        buf.write("\17\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\4\3\2\2")
        buf.write("\2./\7C\2\2/\6\3\2\2\2\60\61\7E\2\2\61\b\3\2\2\2\62\63")
        buf.write("\7F\2\2\63\n\3\2\2\2\64\65\7R\2\2\65\f\3\2\2\2\66\67\7")
        buf.write("I\2\2\67\16\3\2\2\289\7T\2\29\20\3\2\2\2:;\7U\2\2;\22")
        buf.write("\3\2\2\2<=\7[\2\2=\24\3\2\2\2>?\7J\2\2?\26\3\2\2\2@A\7")
        buf.write("Q\2\2A\30\3\2\2\2BC\7W\2\2C\32\3\2\2\2DE\7V\2\2E\34\3")
        buf.write("\2\2\2FG\4\62;\2G\36\3\2\2\2HI\5\33\16\2IJ\5\27\f\2JK")
        buf.write("\5\31\r\2KL\5\7\4\2LM\5\25\13\2M \3\2\2\2NO\5\13\6\2O")
        buf.write("P\5\31\r\2PQ\5\21\t\2QR\5\25\13\2R\"\3\2\2\2ST\5\t\5\2")
        buf.write("TU\5\17\b\2UV\5\5\3\2VW\5\r\7\2W$\3\2\2\2XY\7\"\2\2Y&")
        buf.write("\3\2\2\2Z\\\7\17\2\2[Z\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]")
        buf.write("`\7\f\2\2^`\7\17\2\2_[\3\2\2\2_^\3\2\2\2`a\3\2\2\2a_\3")
        buf.write("\2\2\2ab\3\2\2\2b(\3\2\2\2\7\2,[_a\2")
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
                  "H", "O", "U", "T", "DIGIT", "TOUCH", "PUSH", "DRAG", 
                  "WHITESPACE", "NEWLINE" ]

    grammarFileName = "RoboticFinger.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


