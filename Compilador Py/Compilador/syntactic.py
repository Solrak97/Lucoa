# ------------------------------------------------------------
# xmlparser.py
#
# generador de objetos a partir de un subset xml
# 
# ------------------------------------------------------------
from .symbol_table import crea_variable
from .generation import code, define
from .ply import yacc as yacc
from .lexing import tokens

def p_program(t):
    '''
    program : declaration
        | program declaration
    '''
    pass

def p_declaration(t):
    '''
    declaration : init_declarator SEMICOLON 
    '''
    pass
    
    
def p_init_declarator(t):
    '''
    init_declarator : declarator
        | declarator EQUALS assignment_expression
    '''
    pass

    
def p_declarator(t):
    '''
    declarator : LET IDENTIFIER COLON type_specifier
        | CONST IDENTIFIER COLON type_specifier
    '''
    correcto, address = (crea_variable(t[2], t[4]) )
    if not correcto:
        print(f"Error: variable {t[2]} redefinida en la linea {t.lexer.lineno}")
    else:
        define(f"{t[2]}: RESB {address}")
    pass


def p_type_specifier(t):
    '''
    type_specifier : VOID
        | CHAR
        | INT
        | FLOAT
        | STRING
        | BOOL
    '''
    t[0] = t[1]
    pass


def p_literal(t):
    '''
    literal : INT_LITERAL
        | FLOAT_LITERAL
        | STRING_LITERAL
    '''
    t[0] = t[1]
    pass  


def p_primary_expression(t):
    '''
    primary_expression : IDENTIFIER
        | literal
    '''
    t[0] = t[1]
    pass


def p_additive_expression(t):
    '''
    additive_expression : primary_expression          
        | additive_expression PLUS primary_expression
        | additive_expression MINUS primary_expression
    '''

    if len(t) > 2:
        if t[2] == "+":
            t[0] = f"ADD {t[1]}, {t[3]}"            
        else:
            t[0] = f"SUB {t[1]}, {t[3]}"
    else:
        t[0] = t[1]
    pass


def p_multiplicative_expression(t):
    '''
    multiplicative_expression : additive_expression
        | multiplicative_expression MUL additive_expression
        | multiplicative_expression DIV additive_expression
    '''

    if len(t) > 2:
        if t[2] == "*":      
            t[0] = f"MUL {t[1]}, {t[3]}"       
        else:
            t[0] = f"DIV {t[1]}, {t[3]}"
    else:
        t[0] = t[1]
    pass


def p_assigment_expression(t):
    '''
    assignment_expression : multiplicative_expression
        | primary_expression EQUALS multiplicative_expression
    '''

    if len(t) > 2:
        t[0] = f"MOV {t[1]}, {t[3]}"
    else:
        t[0] = t[1]
    pass  


def p_error(t):
    print(f"Syntax error in line {t.lineno} at {t.value}") 
    pass
    
parser = yacc.yacc()