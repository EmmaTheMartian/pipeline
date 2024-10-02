# Generated from Language.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by LanguageParser#program.
    def enterProgram(self, ctx:LanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by LanguageParser#program.
    def exitProgram(self, ctx:LanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by LanguageParser#stat.
    def enterStat(self, ctx:LanguageParser.StatContext):
        pass

    # Exit a parse tree produced by LanguageParser#stat.
    def exitStat(self, ctx:LanguageParser.StatContext):
        pass


    # Enter a parse tree produced by LanguageParser#stat_var.
    def enterStat_var(self, ctx:LanguageParser.Stat_varContext):
        pass

    # Exit a parse tree produced by LanguageParser#stat_var.
    def exitStat_var(self, ctx:LanguageParser.Stat_varContext):
        pass


    # Enter a parse tree produced by LanguageParser#stat_assign.
    def enterStat_assign(self, ctx:LanguageParser.Stat_assignContext):
        pass

    # Exit a parse tree produced by LanguageParser#stat_assign.
    def exitStat_assign(self, ctx:LanguageParser.Stat_assignContext):
        pass


    # Enter a parse tree produced by LanguageParser#stat_return.
    def enterStat_return(self, ctx:LanguageParser.Stat_returnContext):
        pass

    # Exit a parse tree produced by LanguageParser#stat_return.
    def exitStat_return(self, ctx:LanguageParser.Stat_returnContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr.
    def enterExpr(self, ctx:LanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr.
    def exitExpr(self, ctx:LanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by LanguageParser#func.
    def enterFunc(self, ctx:LanguageParser.FuncContext):
        pass

    # Exit a parse tree produced by LanguageParser#func.
    def exitFunc(self, ctx:LanguageParser.FuncContext):
        pass


    # Enter a parse tree produced by LanguageParser#invoke.
    def enterInvoke(self, ctx:LanguageParser.InvokeContext):
        pass

    # Exit a parse tree produced by LanguageParser#invoke.
    def exitInvoke(self, ctx:LanguageParser.InvokeContext):
        pass


    # Enter a parse tree produced by LanguageParser#block.
    def enterBlock(self, ctx:LanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by LanguageParser#block.
    def exitBlock(self, ctx:LanguageParser.BlockContext):
        pass



del LanguageParser