# Generated from RoboticFinger.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\6\5\35\n\5\r\5\16\5\36\3\5\3\5\3\6\6\6$\n\6\r\6\16")
        buf.write("\6%\3\6\2\2\7\2\4\6\b\n\2\3\3\2\5\7\2%\2\r\3\2\2\2\4\23")
        buf.write("\3\2\2\2\6\30\3\2\2\2\b\34\3\2\2\2\n#\3\2\2\2\f\16\5\4")
        buf.write("\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\21\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\5")
        buf.write("\6\4\2\24\25\5\b\5\2\25\26\5\n\6\2\26\27\7\t\2\2\27\5")
        buf.write("\3\2\2\2\30\31\t\2\2\2\31\32\7\b\2\2\32\7\3\2\2\2\33\35")
        buf.write("\7\3\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37 \3\2\2\2 !\7\b\2\2!\t\3\2\2\2\"$\7\3\2")
        buf.write("\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\13\3\2\2")
        buf.write("\2\5\17\36%")
        return buf.getvalue()


class RoboticFingerParser ( Parser ):

    grammarFileName = "RoboticFinger.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INT_NUMBER", "DIGIT", "TOUCH", "PUSH", 
                      "DRAG", "WHITESPACE", "NEWLINE" ]

    RULE_roboticfinger = 0
    RULE_line = 1
    RULE_command = 2
    RULE_positionX = 3
    RULE_positionY = 4

    ruleNames =  [ "roboticfinger", "line", "command", "positionX", "positionY" ]

    EOF = Token.EOF
    INT_NUMBER=1
    DIGIT=2
    TOUCH=3
    PUSH=4
    DRAG=5
    WHITESPACE=6
    NEWLINE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RoboticfingerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RoboticFingerParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RoboticFingerParser.LineContext)
            else:
                return self.getTypedRuleContext(RoboticFingerParser.LineContext,i)


        def getRuleIndex(self):
            return RoboticFingerParser.RULE_roboticfinger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoboticfinger" ):
                listener.enterRoboticfinger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoboticfinger" ):
                listener.exitRoboticfinger(self)




    def roboticfinger(self):

        localctx = RoboticFingerParser.RoboticfingerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_roboticfinger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.line()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RoboticFingerParser.TOUCH) | (1 << RoboticFingerParser.PUSH) | (1 << RoboticFingerParser.DRAG))) != 0)):
                    break

            self.state = 15
            self.match(RoboticFingerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(RoboticFingerParser.CommandContext,0)


        def positionX(self):
            return self.getTypedRuleContext(RoboticFingerParser.PositionXContext,0)


        def positionY(self):
            return self.getTypedRuleContext(RoboticFingerParser.PositionYContext,0)


        def NEWLINE(self):
            return self.getToken(RoboticFingerParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = RoboticFingerParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.command()
            self.state = 18
            self.positionX()
            self.state = 19
            self.positionY()
            self.state = 20
            self.match(RoboticFingerParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(RoboticFingerParser.WHITESPACE, 0)

        def TOUCH(self):
            return self.getToken(RoboticFingerParser.TOUCH, 0)

        def PUSH(self):
            return self.getToken(RoboticFingerParser.PUSH, 0)

        def DRAG(self):
            return self.getToken(RoboticFingerParser.DRAG, 0)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = RoboticFingerParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RoboticFingerParser.TOUCH) | (1 << RoboticFingerParser.PUSH) | (1 << RoboticFingerParser.DRAG))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 23
            self.match(RoboticFingerParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PositionXContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(RoboticFingerParser.WHITESPACE, 0)

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RoboticFingerParser.INT_NUMBER)
            else:
                return self.getToken(RoboticFingerParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_positionX

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionX" ):
                listener.enterPositionX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionX" ):
                listener.exitPositionX(self)




    def positionX(self):

        localctx = RoboticFingerParser.PositionXContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_positionX)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.match(RoboticFingerParser.INT_NUMBER)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RoboticFingerParser.INT_NUMBER):
                    break

            self.state = 30
            self.match(RoboticFingerParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PositionYContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RoboticFingerParser.INT_NUMBER)
            else:
                return self.getToken(RoboticFingerParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_positionY

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionY" ):
                listener.enterPositionY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionY" ):
                listener.exitPositionY(self)




    def positionY(self):

        localctx = RoboticFingerParser.PositionYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_positionY)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.match(RoboticFingerParser.INT_NUMBER)
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RoboticFingerParser.INT_NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





