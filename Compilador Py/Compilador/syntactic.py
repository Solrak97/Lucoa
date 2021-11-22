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

# Esto esta horrible pero sirve para llevar control de registros
def loaders(t1, t3):
    t1, v1 = t1
    t2, v2 = t3
    code(f"")
    code(f";Asignacion de {v1}, {v2} a sus respectivos registros")
    if v1 == "R1" or v1 == "R3":
        	code(f"MOV {v1}, R2")
    else:
        if t1:
            code(f"LOAD {v1}, R2")
            v1 = "R2"
        else:
            code(f"LOADI {v1}, R2")
            v1 = "R2"
    if v2 == "R1" or v2 == "R2":
        code(f"MOV {v2}, R3")
    else:
        if t2:
            code(f"LOAD {v2}, R3")
            v2 = "R3"
        else:
            code(f"LOADI {v2}, R3")
            v2 = "R3"
    return (v1, v2)



def p_program(t):
    '''
    program : statement
        | program statement
    '''
    pass


# Producciones para declaracion de variables

def p_declaration(t):
    '''
    declaration : init_declarator SEMICOLON
        | declarator EQUALS function_call 
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


#Especificaciones de tipos de variables

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


# Expresiones con operadores

def p_primary_expression(t):
    '''
    primary_expression : IDENTIFIER
        | literal
        | RND_PAR_OPEN assignment_expression RND_PAR_CLOSE
    '''

    if len(t) < 3: 
        if t[1].isalpha():
            t[0] = (True, t[1])
        else:
            t[0] = (False, t[1])
    else:
        t[0] = t[1]
    pass


def p_additive_expression(t):
    '''
    additive_expression : primary_expression          
        | additive_expression PLUS primary_expression
        | additive_expression MINUS primary_expression
    '''
    op = ""
    if len(t) > 2:
        
        v1, v2 = loaders(t[1], t[3])

        if t[2] == "+":
            op = "ADD"            
        else:
            op = "SUB"
            
        code(f"{op} {v1}, {v2}, R1")
        t[0] = (False, "R1")
    else:
        t[0] = t[1]
    pass


def p_multiplicative_expression(t):
    '''
    multiplicative_expression : additive_expression
        | multiplicative_expression MUL additive_expression
        | multiplicative_expression DIV additive_expression
    '''
    op = ""
    #Cuidado con los () que aun no tienen soporte
    if len(t) > 2 and t[1] != "(":
        v1, v2 =loaders(t[1], t[3])

        if t[2] == "*":      
            op = "MUL"       
        else:
            op = "DIV"
        code(f"{op} {v1}, {v2}, R1")
        t[0] = (False, "R1")
    else:
        t[0] = t[1]
    pass


def p_relational_expression(t):
    '''
    relational_expression : multiplicative_expression
        | relational_expression LESS_OP multiplicative_expression
        | relational_expression GREATER_OP multiplicative_expression
        | relational_expression LE_OP multiplicative_expression
        | relational_expression GE_OP multiplicative_expression
    '''
    #Suponga que el CMP puede retornar el resultado a un registro
    #Para no hacer toda la implementacion por ahora
    if len(t) > 3:
        v1, v2 = loaders(t[1], t[3])
        code(";Asuma que CMP retorna a R1")
        code(f"CMP {v1}, {v2}, R1")
        t[0] = "R1"
    t[0] = t[1]


def p_equality_expression(t):
    '''
    equality_expression : relational_expression
        | equality_expression EQ_OP relational_expression
        | equality_expression NE_OP relational_expression
    '''
    op = ""
    if len(t) > 3:
        v1, v2 = loaders(t[1], t[3])
        code(";Asuma que CMP retorna a R1")
        code(f"CMP {v1}, {v2}, R1")
        t[0] = "R1"
    t[0] = t[1]


def p_and_expression(t):
    '''
    and_expression : equality_expression
        | and_expression AND_OP equality_expression
    '''
    op = ""
    if len(t) > 3:
        v1, v2 =loaders(t[1], t[3])
        code(";Asuma que AND retorna a R1") 
        code(f"AND {v1} {v2}, R1")
        t[0] = "R1"
    t[0] = t[1]


def p_or_expression(t):
    '''
    or_expression : and_expression
        | or_expression OR_OP and_expression
    '''
    op = ""
    if len(t) > 3:
        v1, v2 =loaders(t[1], t[3])
        code(";Asuma que OR retorna a R1")
        code(f"OR {v1} {v2}, R1")
        t[0] = "R1"
    t[0] = t[1]


def p_assignment_expression(t):
    '''
    assignment_expression : or_expression
        | primary_expression EQUALS multiplicative_expression
    '''
    if len(t) > 3:
        code(f"STORE {t[1]}, {t[3]}")
    else:
        t[0] = t[1]
    pass  


# Sentencia

def p_statement(t):
    '''
    statement : function_call
        | compound_statement
        | assignment_statement 
        | function_definition
        | declaration
        | selection_statement
        | iteration_statement
    '''
    pass


def p_statement_list(t):
    '''
    statement_list : statement
        | statement_list statement
    '''


def p_compound_statement(t):
    '''
    compound_statement : CUR_PAR_OPEN CUR_PAR_CLOSE
        | CUR_PAR_OPEN statement_list CUR_PAR_CLOSE
    '''

def p_assignment_statement(t):
    '''
    assignment_statement : assignment_expression SEMICOLON
        | primary_expression EQUALS function_call
    '''
    pass

def p_identifier_list(t):
    '''
    identifier_list : empty 
        | IDENTIFIER COLON type_specifier
        | identifier_list COMMA IDENTIFIER  COLON  type_specifier
    '''


def p_parameter_list(t):
    '''
    parameter_list : empty 
        | assignment_expression
        | parameter_list COMMA assignment_expression
    '''


# Definicion de funciones

def p_function_definition(t):
    '''
    function_definition : FUNC IDENTIFIER RND_PAR_OPEN identifier_list RND_PAR_CLOSE ARROW type_specifier compound_statement
    '''

def p_function_call(t):
    '''
    function_call : IDENTIFIER RND_PAR_OPEN parameter_list RND_PAR_CLOSE SEMICOLON
    '''


# Definicion de condicionales

def p_selection_statement(t):
    '''
    selection_statement : IF assignment_expression compound_statement
        | IF assignment_expression compound_statement ELSE compound_statement
    '''


# Definicion de los loops

def p_iteration_statement(t):
    '''
    iteration_statement : FROM BOX_PAR_OPEN assignment_expression COMMA assignment_expression BOX_PAR_CLOSE COLON INC_OP compound_statement
        | FROM BOX_PAR_OPEN assignment_expression COMMA assignment_expression BOX_PAR_CLOSE COLON DEC_OP compound_statement
        | WHILE assignment_expression compound_statement
    '''


def p_empty(t):
    'empty :'
    pass


def p_error(t):
    if t :
        print(f"Syntax error in line {t.lineno} at {t.value}") 
    pass
    
parser = yacc.yacc()