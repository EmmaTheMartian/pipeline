# Generated from Language.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,44,266,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,
        1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,4,37,212,8,37,
        11,37,12,37,213,1,38,1,38,5,38,218,8,38,10,38,12,38,221,9,38,1,39,
        4,39,224,8,39,11,39,12,39,225,1,39,1,39,1,40,1,40,5,40,232,8,40,
        10,40,12,40,235,9,40,1,40,1,40,1,41,1,41,1,41,5,41,242,8,41,10,41,
        12,41,245,9,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,
        3,42,257,8,42,5,42,259,8,42,10,42,12,42,262,9,42,1,43,1,43,1,43,
        1,243,0,44,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,1,
        0,6,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,
        3,0,9,10,12,13,32,32,2,0,10,10,13,13,2,0,34,34,92,92,273,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,
        0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,
        0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,1,89,1,0,0,0,3,91,1,0,0,0,
        5,93,1,0,0,0,7,95,1,0,0,0,9,97,1,0,0,0,11,99,1,0,0,0,13,101,1,0,
        0,0,15,103,1,0,0,0,17,105,1,0,0,0,19,109,1,0,0,0,21,113,1,0,0,0,
        23,116,1,0,0,0,25,119,1,0,0,0,27,122,1,0,0,0,29,124,1,0,0,0,31,127,
        1,0,0,0,33,129,1,0,0,0,35,132,1,0,0,0,37,135,1,0,0,0,39,138,1,0,
        0,0,41,141,1,0,0,0,43,144,1,0,0,0,45,146,1,0,0,0,47,148,1,0,0,0,
        49,150,1,0,0,0,51,152,1,0,0,0,53,154,1,0,0,0,55,158,1,0,0,0,57,164,
        1,0,0,0,59,171,1,0,0,0,61,175,1,0,0,0,63,182,1,0,0,0,65,187,1,0,
        0,0,67,192,1,0,0,0,69,198,1,0,0,0,71,201,1,0,0,0,73,206,1,0,0,0,
        75,211,1,0,0,0,77,215,1,0,0,0,79,223,1,0,0,0,81,229,1,0,0,0,83,238,
        1,0,0,0,85,251,1,0,0,0,87,263,1,0,0,0,89,90,5,61,0,0,90,2,1,0,0,
        0,91,92,5,44,0,0,92,4,1,0,0,0,93,94,5,59,0,0,94,6,1,0,0,0,95,96,
        5,40,0,0,96,8,1,0,0,0,97,98,5,41,0,0,98,10,1,0,0,0,99,100,5,123,
        0,0,100,12,1,0,0,0,101,102,5,125,0,0,102,14,1,0,0,0,103,104,5,46,
        0,0,104,16,1,0,0,0,105,106,5,110,0,0,106,107,5,111,0,0,107,108,5,
        116,0,0,108,18,1,0,0,0,109,110,5,97,0,0,110,111,5,110,0,0,111,112,
        5,100,0,0,112,20,1,0,0,0,113,114,5,111,0,0,114,115,5,114,0,0,115,
        22,1,0,0,0,116,117,5,61,0,0,117,118,5,61,0,0,118,24,1,0,0,0,119,
        120,5,33,0,0,120,121,5,61,0,0,121,26,1,0,0,0,122,123,5,62,0,0,123,
        28,1,0,0,0,124,125,5,62,0,0,125,126,5,61,0,0,126,30,1,0,0,0,127,
        128,5,60,0,0,128,32,1,0,0,0,129,130,5,60,0,0,130,131,5,61,0,0,131,
        34,1,0,0,0,132,133,5,105,0,0,133,134,5,115,0,0,134,36,1,0,0,0,135,
        136,5,105,0,0,136,137,5,110,0,0,137,38,1,0,0,0,138,139,5,43,0,0,
        139,140,5,43,0,0,140,40,1,0,0,0,141,142,5,45,0,0,142,143,5,45,0,
        0,143,42,1,0,0,0,144,145,5,43,0,0,145,44,1,0,0,0,146,147,5,45,0,
        0,147,46,1,0,0,0,148,149,5,42,0,0,149,48,1,0,0,0,150,151,5,47,0,
        0,151,50,1,0,0,0,152,153,5,37,0,0,153,52,1,0,0,0,154,155,5,118,0,
        0,155,156,5,97,0,0,156,157,5,114,0,0,157,54,1,0,0,0,158,159,5,99,
        0,0,159,160,5,111,0,0,160,161,5,110,0,0,161,162,5,115,0,0,162,163,
        5,116,0,0,163,56,1,0,0,0,164,165,5,114,0,0,165,166,5,101,0,0,166,
        167,5,116,0,0,167,168,5,117,0,0,168,169,5,114,0,0,169,170,5,110,
        0,0,170,58,1,0,0,0,171,172,5,102,0,0,172,173,5,117,0,0,173,174,5,
        110,0,0,174,60,1,0,0,0,175,176,5,105,0,0,176,177,5,109,0,0,177,178,
        5,112,0,0,178,179,5,117,0,0,179,180,5,114,0,0,180,181,5,101,0,0,
        181,62,1,0,0,0,182,183,5,112,0,0,183,184,5,117,0,0,184,185,5,114,
        0,0,185,186,5,101,0,0,186,64,1,0,0,0,187,188,5,116,0,0,188,189,5,
        114,0,0,189,190,5,117,0,0,190,191,5,101,0,0,191,66,1,0,0,0,192,193,
        5,102,0,0,193,194,5,97,0,0,194,195,5,108,0,0,195,196,5,115,0,0,196,
        197,5,101,0,0,197,68,1,0,0,0,198,199,5,105,0,0,199,200,5,102,0,0,
        200,70,1,0,0,0,201,202,5,101,0,0,202,203,5,108,0,0,203,204,5,115,
        0,0,204,205,5,101,0,0,205,72,1,0,0,0,206,207,5,102,0,0,207,208,5,
        111,0,0,208,209,5,114,0,0,209,74,1,0,0,0,210,212,7,0,0,0,211,210,
        1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,76,1,
        0,0,0,215,219,7,1,0,0,216,218,7,2,0,0,217,216,1,0,0,0,218,221,1,
        0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,78,1,0,0,0,221,219,1,0,
        0,0,222,224,7,3,0,0,223,222,1,0,0,0,224,225,1,0,0,0,225,223,1,0,
        0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,6,39,0,0,228,80,1,0,
        0,0,229,233,5,35,0,0,230,232,8,4,0,0,231,230,1,0,0,0,232,235,1,0,
        0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,233,1,0,
        0,0,236,237,6,40,0,0,237,82,1,0,0,0,238,239,5,35,0,0,239,243,5,123,
        0,0,240,242,9,0,0,0,241,240,1,0,0,0,242,245,1,0,0,0,243,244,1,0,
        0,0,243,241,1,0,0,0,244,246,1,0,0,0,245,243,1,0,0,0,246,247,5,35,
        0,0,247,248,5,125,0,0,248,249,1,0,0,0,249,250,6,41,0,0,250,84,1,
        0,0,0,251,260,5,34,0,0,252,259,8,5,0,0,253,256,5,92,0,0,254,257,
        9,0,0,0,255,257,5,0,0,1,256,254,1,0,0,0,256,255,1,0,0,0,257,259,
        1,0,0,0,258,252,1,0,0,0,258,253,1,0,0,0,259,262,1,0,0,0,260,258,
        1,0,0,0,260,261,1,0,0,0,261,86,1,0,0,0,262,260,1,0,0,0,263,264,3,
        85,42,0,264,265,5,34,0,0,265,88,1,0,0,0,9,0,213,219,225,233,243,
        256,258,260,1,6,0,0
    ]

class LanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    COMMA = 2
    SEMI = 3
    LPAREN = 4
    RPAREN = 5
    LCURLY = 6
    RCURLY = 7
    OP_DOT = 8
    OP_NOT = 9
    OP_AND = 10
    OP_OR = 11
    OP_EQ = 12
    OP_NEQ = 13
    OP_GT = 14
    OP_GTEQ = 15
    OP_LT = 16
    OP_LTEQ = 17
    OP_IS = 18
    OP_IN = 19
    OP_INC = 20
    OP_DEC = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    VAR = 27
    CONST = 28
    RETURN = 29
    FUN = 30
    IMPURE = 31
    PURE = 32
    TRUE = 33
    FALSE = 34
    IF = 35
    ELSE = 36
    FOR = 37
    INT = 38
    ID = 39
    WS = 40
    COMMENT = 41
    MULTILINE_COMMENT = 42
    UNTERMINATED_STRING = 43
    STRING = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "','", "';'", "'('", "')'", "'{'", "'}'", "'.'", "'not'", 
            "'and'", "'or'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
            "'is'", "'in'", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'var'", "'const'", "'return'", "'fun'", "'impure'", 
            "'pure'", "'true'", "'false'", "'if'", "'else'", "'for'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", 
            "OP_DOT", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ", "OP_NEQ", "OP_GT", 
            "OP_GTEQ", "OP_LT", "OP_LTEQ", "OP_IS", "OP_IN", "OP_INC", "OP_DEC", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "VAR", "CONST", "RETURN", 
            "FUN", "IMPURE", "PURE", "TRUE", "FALSE", "IF", "ELSE", "FOR", 
            "INT", "ID", "WS", "COMMENT", "MULTILINE_COMMENT", "UNTERMINATED_STRING", 
            "STRING" ]

    ruleNames = [ "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", 
                  "OP_DOT", "OP_NOT", "OP_AND", "OP_OR", "OP_EQ", "OP_NEQ", 
                  "OP_GT", "OP_GTEQ", "OP_LT", "OP_LTEQ", "OP_IS", "OP_IN", 
                  "OP_INC", "OP_DEC", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "VAR", "CONST", "RETURN", "FUN", "IMPURE", "PURE", "TRUE", 
                  "FALSE", "IF", "ELSE", "FOR", "INT", "ID", "WS", "COMMENT", 
                  "MULTILINE_COMMENT", "UNTERMINATED_STRING", "STRING" ]

    grammarFileName = "Language.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


