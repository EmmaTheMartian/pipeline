grammar Language;

// Tokens
AND: 'and';
OR: 'or';
NOT: 'not';
EQ: '=';
COMMA: ',';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
LCURLY: '{';
RCURLY: '}';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

VAR: 'var';
RETURN: 'return';
FUN: 'fun';
IMPURE: 'impure';
PURE: 'pure';
TRUE: 'true';
FALSE: 'false';

INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\n\r\f]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
STRING: '"' .*? '"';

// Grammar
program: (stat ';')* EOF;

stat: stat_var
    | stat_assign
    | stat_return
    | expr
    ;

stat_var: 'var' ID '=' expr;
stat_assign: ID '=' expr;
stat_return: 'return' expr;

expr: INT
    | STRING
    | TRUE
    | FALSE
    | func
    | invoke
    | block
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | expr '%' expr
    | ID
    ;

func: '(' ID* ')' stat;
invoke: ID '(' expr* ')';
block: ('impure'|'pure') '{' (stat ';')* '}';
