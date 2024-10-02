# Generated from Language.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,58,8,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,81,8,5,10,5,12,5,84,9,5,1,6,1,6,5,6,88,
        8,6,10,6,12,6,91,9,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,99,8,7,10,7,12,
        7,102,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,111,8,8,10,8,12,8,114,
        9,8,1,8,1,8,1,8,0,1,10,9,0,2,4,6,8,10,12,14,16,0,1,1,0,19,20,130,
        0,23,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,39,1,0,0,0,8,43,1,0,0,0,
        10,57,1,0,0,0,12,85,1,0,0,0,14,95,1,0,0,0,16,105,1,0,0,0,18,19,3,
        2,1,0,19,20,5,6,0,0,20,22,1,0,0,0,21,18,1,0,0,0,22,25,1,0,0,0,23,
        21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,
        1,27,1,1,0,0,0,28,33,3,4,2,0,29,33,3,6,3,0,30,33,3,8,4,0,31,33,3,
        10,5,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        3,1,0,0,0,34,35,5,16,0,0,35,36,5,24,0,0,36,37,5,4,0,0,37,38,3,10,
        5,0,38,5,1,0,0,0,39,40,5,24,0,0,40,41,5,4,0,0,41,42,3,10,5,0,42,
        7,1,0,0,0,43,44,5,17,0,0,44,45,3,10,5,0,45,9,1,0,0,0,46,47,6,5,-1,
        0,47,58,5,23,0,0,48,58,5,27,0,0,49,58,5,21,0,0,50,58,5,22,0,0,51,
        58,3,12,6,0,52,58,3,14,7,0,53,58,3,16,8,0,54,55,5,3,0,0,55,58,3,
        10,5,9,56,58,5,24,0,0,57,46,1,0,0,0,57,48,1,0,0,0,57,49,1,0,0,0,
        57,50,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,
        0,0,0,57,56,1,0,0,0,58,82,1,0,0,0,59,60,10,8,0,0,60,61,5,1,0,0,61,
        81,3,10,5,9,62,63,10,7,0,0,63,64,5,2,0,0,64,81,3,10,5,8,65,66,10,
        6,0,0,66,67,5,11,0,0,67,81,3,10,5,7,68,69,10,5,0,0,69,70,5,12,0,
        0,70,81,3,10,5,6,71,72,10,4,0,0,72,73,5,13,0,0,73,81,3,10,5,5,74,
        75,10,3,0,0,75,76,5,14,0,0,76,81,3,10,5,4,77,78,10,2,0,0,78,79,5,
        15,0,0,79,81,3,10,5,3,80,59,1,0,0,0,80,62,1,0,0,0,80,65,1,0,0,0,
        80,68,1,0,0,0,80,71,1,0,0,0,80,74,1,0,0,0,80,77,1,0,0,0,81,84,1,
        0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,82,1,0,0,0,85,
        89,5,7,0,0,86,88,5,24,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,
        0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,8,0,0,93,94,
        3,2,1,0,94,13,1,0,0,0,95,96,5,24,0,0,96,100,5,7,0,0,97,99,3,10,5,
        0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,
        103,1,0,0,0,102,100,1,0,0,0,103,104,5,8,0,0,104,15,1,0,0,0,105,106,
        7,0,0,0,106,112,5,9,0,0,107,108,3,2,1,0,108,109,5,6,0,0,109,111,
        1,0,0,0,110,107,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,116,5,10,0,0,116,17,
        1,0,0,0,8,23,32,57,80,82,89,100,112
    ]

class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'='", "','", 
                     "';'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'var'", "'return'", "'fun'", "'impure'", 
                     "'pure'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "LCURLY", "RCURLY", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "VAR", "RETURN", "FUN", "IMPURE", 
                      "PURE", "TRUE", "FALSE", "INT", "ID", "WS", "COMMENT", 
                      "STRING" ]

    RULE_program = 0
    RULE_stat = 1
    RULE_stat_var = 2
    RULE_stat_assign = 3
    RULE_stat_return = 4
    RULE_expr = 5
    RULE_func = 6
    RULE_invoke = 7
    RULE_block = 8

    ruleNames =  [ "program", "stat", "stat_var", "stat_assign", "stat_return", 
                   "expr", "func", "invoke", "block" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    EQ=4
    COMMA=5
    SEMI=6
    LPAREN=7
    RPAREN=8
    LCURLY=9
    RCURLY=10
    ADD=11
    SUB=12
    MUL=13
    DIV=14
    MOD=15
    VAR=16
    RETURN=17
    FUN=18
    IMPURE=19
    PURE=20
    TRUE=21
    FALSE=22
    INT=23
    ID=24
    WS=25
    COMMENT=26
    STRING=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LanguageParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.SEMI)
            else:
                return self.getToken(LanguageParser.SEMI, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 167444616) != 0):
                self.state = 18
                self.stat()
                self.state = 19
                self.match(LanguageParser.SEMI)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(LanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_var(self):
            return self.getTypedRuleContext(LanguageParser.Stat_varContext,0)


        def stat_assign(self):
            return self.getTypedRuleContext(LanguageParser.Stat_assignContext,0)


        def stat_return(self):
            return self.getTypedRuleContext(LanguageParser.Stat_returnContext,0)


        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = LanguageParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.stat_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.stat_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.stat_return()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LanguageParser.VAR, 0)

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def EQ(self):
            return self.getToken(LanguageParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_stat_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_var" ):
                listener.enterStat_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_var" ):
                listener.exitStat_var(self)




    def stat_var(self):

        localctx = LanguageParser.Stat_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(LanguageParser.VAR)
            self.state = 35
            self.match(LanguageParser.ID)
            self.state = 36
            self.match(LanguageParser.EQ)
            self.state = 37
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def EQ(self):
            return self.getToken(LanguageParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_stat_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_assign" ):
                listener.enterStat_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_assign" ):
                listener.exitStat_assign(self)




    def stat_assign(self):

        localctx = LanguageParser.Stat_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(LanguageParser.ID)
            self.state = 40
            self.match(LanguageParser.EQ)
            self.state = 41
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LanguageParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(LanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_stat_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_return" ):
                listener.enterStat_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_return" ):
                listener.exitStat_return(self)




    def stat_return(self):

        localctx = LanguageParser.Stat_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stat_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(LanguageParser.RETURN)
            self.state = 44
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LanguageParser.INT, 0)

        def STRING(self):
            return self.getToken(LanguageParser.STRING, 0)

        def TRUE(self):
            return self.getToken(LanguageParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LanguageParser.FALSE, 0)

        def func(self):
            return self.getTypedRuleContext(LanguageParser.FuncContext,0)


        def invoke(self):
            return self.getTypedRuleContext(LanguageParser.InvokeContext,0)


        def block(self):
            return self.getTypedRuleContext(LanguageParser.BlockContext,0)


        def NOT(self):
            return self.getToken(LanguageParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExprContext,i)


        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def AND(self):
            return self.getToken(LanguageParser.AND, 0)

        def OR(self):
            return self.getToken(LanguageParser.OR, 0)

        def ADD(self):
            return self.getToken(LanguageParser.ADD, 0)

        def SUB(self):
            return self.getToken(LanguageParser.SUB, 0)

        def MUL(self):
            return self.getToken(LanguageParser.MUL, 0)

        def DIV(self):
            return self.getToken(LanguageParser.DIV, 0)

        def MOD(self):
            return self.getToken(LanguageParser.MOD, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 47
                self.match(LanguageParser.INT)
                pass

            elif la_ == 2:
                self.state = 48
                self.match(LanguageParser.STRING)
                pass

            elif la_ == 3:
                self.state = 49
                self.match(LanguageParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 50
                self.match(LanguageParser.FALSE)
                pass

            elif la_ == 5:
                self.state = 51
                self.func()
                pass

            elif la_ == 6:
                self.state = 52
                self.invoke()
                pass

            elif la_ == 7:
                self.state = 53
                self.block()
                pass

            elif la_ == 8:
                self.state = 54
                self.match(LanguageParser.NOT)
                self.state = 55
                self.expr(9)
                pass

            elif la_ == 9:
                self.state = 56
                self.match(LanguageParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 60
                        self.match(LanguageParser.AND)
                        self.state = 61
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 63
                        self.match(LanguageParser.OR)
                        self.state = 64
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 66
                        self.match(LanguageParser.ADD)
                        self.state = 67
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 69
                        self.match(LanguageParser.SUB)
                        self.state = 70
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 72
                        self.match(LanguageParser.MUL)
                        self.state = 73
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(LanguageParser.DIV)
                        self.state = 76
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = LanguageParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(LanguageParser.MOD)
                        self.state = 79
                        self.expr(3)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LanguageParser.RPAREN, 0)

        def stat(self):
            return self.getTypedRuleContext(LanguageParser.StatContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.ID)
            else:
                return self.getToken(LanguageParser.ID, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = LanguageParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(LanguageParser.LPAREN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 86
                self.match(LanguageParser.ID)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(LanguageParser.RPAREN)
            self.state = 93
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LanguageParser.ID, 0)

        def LPAREN(self):
            return self.getToken(LanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LanguageParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(LanguageParser.ExprContext,i)


        def getRuleIndex(self):
            return LanguageParser.RULE_invoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvoke" ):
                listener.enterInvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvoke" ):
                listener.exitInvoke(self)




    def invoke(self):

        localctx = LanguageParser.InvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_invoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LanguageParser.ID)
            self.state = 96
            self.match(LanguageParser.LPAREN)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 167248008) != 0):
                self.state = 97
                self.expr(0)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(LanguageParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(LanguageParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(LanguageParser.RCURLY, 0)

        def IMPURE(self):
            return self.getToken(LanguageParser.IMPURE, 0)

        def PURE(self):
            return self.getToken(LanguageParser.PURE, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LanguageParser.StatContext)
            else:
                return self.getTypedRuleContext(LanguageParser.StatContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(LanguageParser.SEMI)
            else:
                return self.getToken(LanguageParser.SEMI, i)

        def getRuleIndex(self):
            return LanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = LanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 106
            self.match(LanguageParser.LCURLY)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 167444616) != 0):
                self.state = 107
                self.stat()
                self.state = 108
                self.match(LanguageParser.SEMI)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(LanguageParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




