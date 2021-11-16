%{
      #include <stdio.h>
      int yylex(void);
%}

/* TOKENS */
%token LET IDENTIFIER
%token COLON SEMICOLON
%token EQUALS 
%token CONSTANT

/* Tipos de dato */
%token VOID CHAR INT FLOAT STRING BOOL

%token INC_OP DEC_OP
%token LE_OP GE_OP
%token EQ_OP NE_OP
%token AND_OP OR_OP
%token IF ELSE
%start program


%%


/* Entry point de la gramatica */
program
      : declaration
      | program declaration
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
      : init_declarator SEMICOLON {printf("Variable encontrada\n");}
      ;

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
      ;


/* Expresiones */
primary_expression
      : IDENTIFIER
      | CONSTANT
      ;

additive_expression
      : primary_expression
      | additive_expression '+' primary_expression
      | additive_expression '-' primary_expression
      ;

assignment_expression
      : additive_expression
      | primary_expression EQUALS additive_expression 
      ;


%%
yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}