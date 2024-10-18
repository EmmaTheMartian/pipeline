grammar Language;

// Tokens
EQ: '=';
COMMA: ',';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
LCURLY: '{';
RCURLY: '}';

OP_DOT: '.';
OP_NOT: 'not';
OP_AND: 'and';
OP_OR: 'or';
OP_EQ: '==';
OP_NEQ: '!=';
OP_GT: '>';
OP_GTEQ: '>=';
OP_LT: '<';
OP_LTEQ: '<=';
OP_IS: 'is';
OP_IN: 'in';
OP_INC: '++';
OP_DEC: '--';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

VAR: 'var';
CONST: 'const';
RETURN: 'return';
FUN: 'fun';
IMPURE: 'impure';
PURE: 'pure';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
FOR: 'for';

INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\n\r\f]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '#' '{' .*? '#' '}' -> skip;
// https://stackoverflow.com/a/24559773
UNTERMINATED_STRING: '"' (~["\\] | '\\' ( . | EOF))*;
STRING: UNTERMINATED_STRING '"';

// Grammar
program: (stat ';')* EOF;

stat: stat_var
    | stat_const
    | stat_assign
    | stat_return
    | expr
    ;

stat_var: 'var' ID '=' expr;
stat_const: 'const' ID '=' expr;
stat_assign: ID '=' expr;
stat_return: 'return' expr;

expr:
    // Operators
    expr '.' ID
    | expr 'is' expr
    | expr 'in' expr
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr '==' expr
    | expr '!=' expr
    | expr '>' expr
    | expr '>=' expr
    | expr '<' expr
    | expr '<=' expr
    // Math
    | expr '*' expr
    | expr '/' expr
    | expr '%' expr
    | expr '+' expr
    | expr '-' expr
    | expr '++'
    | expr '--'
    // Control flow and friends
    | expr_func
    | expr part_invoke
    | expr_block
    | expr_if
    | expr_for
    // Literals (+ID)
    | INT
    | STRING
    | TRUE
    | FALSE
    | ID
    ;

expr_func: ('impure'|'pure') '(' (ID ','?)* ')' stat;
expr_block: 'pure'? '{' (stat ';')* '}';
expr_if: 'if' '(' expr ')' expr ('else' expr)?;
expr_for: 'for' '(' expr ';' expr ';' expr ')' stat;

// "Parts"
// Allow me to break things up into smaller parts for ease-of-use
part_invoke: '(' (expr ','?)* ')';
