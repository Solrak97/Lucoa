# ------------------------------------------------------------
# xmlex.py
#
# tokenizador para un subset de xml
# 
# ------------------------------------------------------------

from .ply import lex

#    Lista de tokens
tokens = (  

    #Keyword
    'LET', 'CONST', 'FUNC', 'FROM', 
    #Data Types 
    'VOID', 'BOOL', 'CHAR', 'INT', 'FLOAT', 'STRING',
    'STRING_LITERAL', 'FLOAT_LITERAL', 'INT_LITERAL',
    'IDENTIFIER',

    #Operators
    'PLUS', 'MINUS', 'MUL', 'DIV', 'EQUALS', 'INC_OP',
    'DEC_OP', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'AND_OP',
    'OR_OP', 'IF', 'ELSE', 'COLON', 'SEMICOLON', 'ARROW',
    'COMMA', 'GREATER_OP', 'LESS_OP', 'WHILE', 
    

    #Parentesis
    'RND_PAR_OPEN', 'RND_PAR_CLOSE',
    'BOX_PAR_OPEN', 'BOX_PAR_CLOSE',
    'CUR_PAR_OPEN', 'CUR_PAR_CLOSE',
    
)

#    TAG REGEX

t_MUL = r'\*'
t_DIV = r'/'
t_INC_OP = r'\+\+'
t_DEC_OP = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'

t_ARROW = r'->'
t_RND_PAR_OPEN = r'\('
t_RND_PAR_CLOSE = r'\)'
t_BOX_PAR_OPEN = r'\['
t_BOX_PAR_CLOSE = r'\]'
t_CUR_PAR_OPEN = r'{'
t_CUR_PAR_CLOSE = r'}' 

t_COMMA = r','
t_EQUALS = r'='

t_GREATER_OP = r'>'
t_LESS_OP = r'<'

t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_COLON = r':'
t_SEMICOLON = r';'
t_STRING_LITERAL = r'".*"|\'.*\''


def t_COMMENT(t):
    r'(\#.+(\n)?)'
    t.lexer.lineno += len(t.value)
    pass

def t_LET(t):
    r'let'
    return t

def t_CONST(t):
    r'const'
    return t

def t_FUNC(t):
    r'func'
    return t

def t_VOID(t):
    r'void'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_STRING(t):
    r'string'
    return t

def t_FROM(t):
    r'from'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FLOAT_LITERAL(t): 
    r'[-+]?[0-9]*\.[0-9]+'
    return t

def t_INT_LITERAL(t): 
    r'[-+]?[0-9]+'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_]([a-zA-Z_0-9])*'
    return t

#    Regla para contar numeros
def t_newline(t):
     r'[\n]+'
     t.lexer.lineno += len(t.value)
     pass
#    Caracteres a ignorar
t_ignore  = ' \t'

def t_error(t):
     print("Expresion ilegal en '%s'" % t.value[0])
     t.lexer.skip(1)
     pass
 
lexer = lex.lex()

