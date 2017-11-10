# Generated from RoboticFinger.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\6\7\61\n\7\r\7\16\7")
        buf.write("\62\3\7\3\7\3\b\6\b8\n\b\r\b\16\b9\3\t\6\t=\n\t\r\t\16")
        buf.write("\t>\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2>\2\23\3\2\2\2\4")
        buf.write("%\3\2\2\2\6\'\3\2\2\2\b*\3\2\2\2\n-\3\2\2\2\f\60\3\2\2")
        buf.write("\2\16\67\3\2\2\2\20<\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\5\6\4\2\32\33\5")
        buf.write("\f\7\2\33\34\5\16\b\2\34\35\7\t\2\2\35&\3\2\2\2\36\37")
        buf.write("\5\b\5\2\37 \5\20\t\2 !\7\t\2\2!&\3\2\2\2\"#\5\n\6\2#")
        buf.write("$\7\t\2\2$&\3\2\2\2%\31\3\2\2\2%\36\3\2\2\2%\"\3\2\2\2")
        buf.write("&\5\3\2\2\2\'(\7\7\2\2()\7\b\2\2)\7\3\2\2\2*+\7\6\2\2")
        buf.write("+,\7\b\2\2,\t\3\2\2\2-.\7\5\2\2.\13\3\2\2\2/\61\7\3\2")
        buf.write("\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\65\7\b\2\2\65\r\3\2\2\2\668\7\3\2")
        buf.write("\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\17\3")
        buf.write("\2\2\2;=\7\3\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2")
        buf.write("\2?\21\3\2\2\2\7\25%\629>")
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
    RULE_drag_command = 2
    RULE_push_cmd = 3
    RULE_touch_cmd = 4
    RULE_positionX = 5
    RULE_positionY = 6
    RULE_time = 7

    ruleNames =  [ "roboticfinger", "line", "drag_command", "push_cmd", 
                   "touch_cmd", "positionX", "positionY", "time" ]

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.line()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RoboticFingerParser.TOUCH) | (1 << RoboticFingerParser.PUSH) | (1 << RoboticFingerParser.DRAG))) != 0)):
                    break

            self.state = 21
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

        def drag_command(self):
            return self.getTypedRuleContext(RoboticFingerParser.Drag_commandContext,0)


        def positionX(self):
            return self.getTypedRuleContext(RoboticFingerParser.PositionXContext,0)


        def positionY(self):
            return self.getTypedRuleContext(RoboticFingerParser.PositionYContext,0)


        def NEWLINE(self):
            return self.getToken(RoboticFingerParser.NEWLINE, 0)

        def push_cmd(self):
            return self.getTypedRuleContext(RoboticFingerParser.Push_cmdContext,0)


        def time(self):
            return self.getTypedRuleContext(RoboticFingerParser.TimeContext,0)


        def touch_cmd(self):
            return self.getTypedRuleContext(RoboticFingerParser.Touch_cmdContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RoboticFingerParser.DRAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.drag_command()
                self.state = 24
                self.positionX()
                self.state = 25
                self.positionY()
                self.state = 26
                self.match(RoboticFingerParser.NEWLINE)
                pass
            elif token in [RoboticFingerParser.PUSH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.push_cmd()
                self.state = 29
                self.time()
                self.state = 30
                self.match(RoboticFingerParser.NEWLINE)
                pass
            elif token in [RoboticFingerParser.TOUCH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.touch_cmd()
                self.state = 33
                self.match(RoboticFingerParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Drag_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAG(self):
            return self.getToken(RoboticFingerParser.DRAG, 0)

        def WHITESPACE(self):
            return self.getToken(RoboticFingerParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_drag_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrag_command" ):
                listener.enterDrag_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrag_command" ):
                listener.exitDrag_command(self)




    def drag_command(self):

        localctx = RoboticFingerParser.Drag_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_drag_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(RoboticFingerParser.DRAG)
            self.state = 38
            self.match(RoboticFingerParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Push_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUSH(self):
            return self.getToken(RoboticFingerParser.PUSH, 0)

        def WHITESPACE(self):
            return self.getToken(RoboticFingerParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_push_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush_cmd" ):
                listener.enterPush_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush_cmd" ):
                listener.exitPush_cmd(self)




    def push_cmd(self):

        localctx = RoboticFingerParser.Push_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_push_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(RoboticFingerParser.PUSH)
            self.state = 41
            self.match(RoboticFingerParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Touch_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOUCH(self):
            return self.getToken(RoboticFingerParser.TOUCH, 0)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_touch_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTouch_cmd" ):
                listener.enterTouch_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTouch_cmd" ):
                listener.exitTouch_cmd(self)




    def touch_cmd(self):

        localctx = RoboticFingerParser.Touch_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_touch_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(RoboticFingerParser.TOUCH)
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
        self.enterRule(localctx, 10, self.RULE_positionX)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.match(RoboticFingerParser.INT_NUMBER)
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RoboticFingerParser.INT_NUMBER):
                    break

            self.state = 50
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
        self.enterRule(localctx, 12, self.RULE_positionY)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.match(RoboticFingerParser.INT_NUMBER)
                self.state = 55 
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

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RoboticFingerParser.INT_NUMBER)
            else:
                return self.getToken(RoboticFingerParser.INT_NUMBER, i)

        def getRuleIndex(self):
            return RoboticFingerParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = RoboticFingerParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.match(RoboticFingerParser.INT_NUMBER)
                self.state = 60 
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





