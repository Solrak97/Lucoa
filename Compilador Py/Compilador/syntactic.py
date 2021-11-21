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
        | function_definition
        | iteration_statement
        | selection_statement
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


def p_assignment_expression(t):
    '''
    assignment_expression : multiplicative_expression
        | primary_expression EQUALS multiplicative_expression
    '''

    if len(t) > 2:
        t[0] = f"MOV {t[1]}, {t[3]}"
    else:
        t[0] = t[1]
    pass  

def p_selection_statement(t):
    '''
    selection_statement : IF conditional_expression compound_statement
        | IF conditional_expression compound_statement ELSE compound_statement
    '''

def p_statement(t):
    '''
    statement : declaration
        | iteration_statement
        | selection_statement
    '''

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

def p_identifier_list(t):
    '''
    identifier_list : IDENTIFIER
        | identifier_list COMMA IDENTIFIER
    '''

def p_relational_expression(t):
    '''
    relational_expression : multiplicative_expression
        | relational_expression LESS_OP multiplicative_expression
        | relational_expression GREATER_OP multiplicative_expression
        | relational_expression LE_OP multiplicative_expression
        | relational_expression GE_OP multiplicative_expression
    '''

def p_equality_expression(t):
    '''
    equality_expression : relational_expression
        | equality_expression EQ_OP relational_expression
        | equality_expression NE_OP relational_expression
    '''

def p_and_expression(t):
    '''
    and_expression : equality_expression
        | and_expression AND_OP equality_expression
    '''

def p_or_expression(t):
    '''
    or_expression : and_expression
        | or_expression OR_OP and_expression
    '''

def p_conditional_expression(t):
    '''
    conditional_expression : or_expression
        | or_expression QUESTION assignment_expression COLON conditional_expression
    '''

def p_function_definition(t):
    '''
    function_definition : FUNC IDENTIFIER RND_PAR_OPEN identifier_list RND_PAR_CLOSE ARROW type_specifier compound_statement
    '''

def p_iteration_statement(t):
    '''
    iteration_statement : FROM BOX_PAR_OPEN primary_expression COMMA primary_expression BOX_PAR_CLOSE COLON INC_OP compound_statement
        | FROM BOX_PAR_OPEN primary_expression COMMA primary_expression BOX_PAR_CLOSE COLON DEC_OP compound_statement
        | WHILE conditional_expression compound_statement
        | DO compound_statement WHILE conditional_expression SEMICOLON
    '''
    ### OJO CON EL DO (POSIBLE ERROR CON EL PUNTO Y COMA FINAL)

def p_error(t):
    print(f"Syntax error in line {t.lineno} at {t.value}") 
    pass
    
parser = yacc.yacc()