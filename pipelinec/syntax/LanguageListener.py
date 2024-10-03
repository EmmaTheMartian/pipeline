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


    # Enter a parse tree produced by LanguageParser#stat_const.
    def enterStat_const(self, ctx:LanguageParser.Stat_constContext):
        pass

    # Exit a parse tree produced by LanguageParser#stat_const.
    def exitStat_const(self, ctx:LanguageParser.Stat_constContext):
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


    # Enter a parse tree produced by LanguageParser#expr_func.
    def enterExpr_func(self, ctx:LanguageParser.Expr_funcContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr_func.
    def exitExpr_func(self, ctx:LanguageParser.Expr_funcContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr_invoke.
    def enterExpr_invoke(self, ctx:LanguageParser.Expr_invokeContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr_invoke.
    def exitExpr_invoke(self, ctx:LanguageParser.Expr_invokeContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr_block.
    def enterExpr_block(self, ctx:LanguageParser.Expr_blockContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr_block.
    def exitExpr_block(self, ctx:LanguageParser.Expr_blockContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr_if.
    def enterExpr_if(self, ctx:LanguageParser.Expr_ifContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr_if.
    def exitExpr_if(self, ctx:LanguageParser.Expr_ifContext):
        pass


    # Enter a parse tree produced by LanguageParser#expr_for.
    def enterExpr_for(self, ctx:LanguageParser.Expr_forContext):
        pass

    # Exit a parse tree produced by LanguageParser#expr_for.
    def exitExpr_for(self, ctx:LanguageParser.Expr_forContext):
        pass



del LanguageParser