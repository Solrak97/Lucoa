%{
      #include <stdio.h>
      #include "SymbolTable.h"
      int yylex(void);
%}

/* RESWORDS */
%token LET CONST IDENTIFIER FUNC FROM
%token COLON SEMICOLON COMMA
%token RND_PAR_OPEN RND_PAR_CLOSE BOX_PAR_OPEN BOX_PAR_CLOSE CUR_PAR_OPEN CUR_PAR_CLOSE
%token EQUALS ARROW
%token NUMERIC DOT

/* Tipos de dato */
%token VOID CHAR INT FLOAT STRING BOOL STRING_LITERAL

/* Operadores */
%token MUL DIV PLUS MINUS INC_OP DEC_OP
%token LE_OP GE_OP EQ_OP NE_OP AND_OP OR_OP IF ELSE

/* ENTRY POINT */
%start program

%%


/* Entry point de la gramatica */
program
      : declaration
      | program declaration
      | function_definition
      | loop
      ;

/* Tipos aceptados */
type_specifier 
      : VOID
      | CHAR
      | INT
      | FLOAT
      | STRING
      | BOOL
      ;


/*
Declaraciones
*/

/*
      : let a: int;
      | let a: int = 7;
      | let a: int = let b: int = 7;
*/
declaration 
      : init_declarator SEMICOLON {printf("Variable asignada\n"); tableInsertion(0,0);}
      ;
      /*instrucción NASM equivalente: mov nombreVariable, valorVariable/*

/*
      : let a: int
      | let a: int = 7
      | let a: int = let b: int
*/
init_declarator
      : declarator
      | declarator EQUALS assignment_expression
      ; 


/* 
      let a: int  
*/
declarator
      : LET IDENTIFIER COLON type_specifier
      | CONST IDENTIFIER COLON type_specifier
      ;


/* Expresiones */
primary_expression
      : IDENTIFIER               
      | NUMERIC DOT NUMERIC       
      | NUMERIC                  
      | STRING_LITERAL            
      ;

additive_expression
      : primary_expression                          
      | additive_expression PLUS primary_expression 
      | additive_expression MINUS primary_expression
      ;

multiplicative_expression
      : additive_expression                                
      | multiplicative_expression MUL additive_expression  
      | multiplicative_expression DIV additive_expression  
      ;

assignment_expression
      : multiplicative_expression                          
      | primary_expression EQUALS multiplicative_expression
      ;

/* Función */
function_definition
      : FUNC IDENTIFIER RND_PAR_OPEN identifier_list RND_PAR_CLOSE ARROW type_specifier compound_statement {printf("Función encontrada\n");}
      ;

identifier_list
      :
      | IDENTIFIER
      | IDENTIFIER COMMA IDENTIFIER

/* Sentencia */
statement
      : IDENTIFIER
      ;

compound_statement 
      : CUR_PAR_OPEN CUR_PAR_CLOSE
      | CUR_PAR_OPEN statement_list CUR_PAR_CLOSE
      ;

statement_list
      : statement
      | statement_list statement
      ;

/* Ciclo */
loop
      : FROM BOX_PAR_OPEN primary_expression COMMA primary_expression BOX_PAR_CLOSE COLON INC_OP compound_statement {printf("Ciclo encontrado\n");}
      | FROM BOX_PAR_OPEN primary_expression COMMA primary_expression BOX_PAR_CLOSE COLON DEC_OP compound_statement {printf("Ciclo encontrado\n");}
      ;


%%
yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}