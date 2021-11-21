%{
    #include <iostream>
    #include <stdio.h>
    #include <string>
    //#include "SymbolTable.hpp"
    void yyerror(char* s);
    int yylex(void);
    std::string s = new std::String();
%}

%union {
     char* st;
     float ft;
     int   it;
}

/* RESWORDS */
%token LET CONST IDENTIFIER FUNC FROM
%token COLON SEMICOLON COMMA
%token RND_PAR_OPEN RND_PAR_CLOSE BOX_PAR_OPEN BOX_PAR_CLOSE CUR_PAR_OPEN CUR_PAR_CLOSE
%token EQUALS ARROW
%token DOT

/* Tipos de dato */
%token VOID CHAR INT FLOAT STRING BOOL STRING_LITERAL FLOAT_LITERAL 
%token <it> NUMERIC_LITERAL

/* Operadores */
%token MUL DIV PLUS MINUS INC_OP DEC_OP
%token LE_OP GE_OP EQ_OP NE_OP AND_OP OR_OP IF ELSE

%type <st> type_specifier
%type <st> VOID CHAR INT FLOAT STRING BOOL

%type <st> literal 
%type <it> NUMERIC_LITERAL
%type <st> STRING_LITERAL DOT
%type <st> primary_expression
%type <st> additive_expression
%type <st> multiplicative_expression
%type <st> assignment_expression

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
      : VOID                                {$$ = $1;}
      | CHAR                                {$$ = $1;}
      | INT                                 {$$ = $1;}
      | FLOAT                               {$$ = $1;}
      | STRING                              {$$ = $1;}
      | BOOL                                {$$ = $1;}
      ;

literal 
      : NUMERIC_LITERAL       	            {$$ = $1;}
      | NUMERIC_LITERAL DOT NUMERIC_LITERAL     {s = ""; s += $1 + $2 + $3; $$ = s;}
      | STRING_LITERAL                          {$$ = $1;}
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
      : init_declarator SEMICOLON                               { }
      ;
      /*instrucción NASM equivalente: mov nombreVariable, valorVariable/*

/*
      : let a: int
      | let a: int = 7
      | let a: int = let b: int
*/
init_declarator
      : declarator                                              {}
      | declarator EQUALS assignment_expression                 {}
      ; 


/* 
      let a: int  
*/
declarator
      : LET IDENTIFIER COLON type_specifier                     {}
      | CONST IDENTIFIER COLON type_specifier                   {}
      ;


/* Expresiones */
primary_expression
      : IDENTIFIER                                              {}
      | literal                                                 { $$ = $1; std::cout << $1; }
      ;

additive_expression
      : primary_expression                                      { $$ = $1; std::cout << $1 << std::endl; }
      | additive_expression PLUS primary_expression             { $$ = $1; std::cout << $1 << "+" << $3 << std::endl; }
      | additive_expression MINUS primary_expression            { $$ = $1; std::cout << $1 << "-" << $3 << std::endl; }
      ;

multiplicative_expression
      : additive_expression                                     { $$ = $1; std::cout << $1 << std::endl;}
      | multiplicative_expression MUL additive_expression       { $$ = $1; std::cout << $1 << '*' << $3 << std::endl;}
      | multiplicative_expression DIV additive_expression       { $$ = $1; std::cout << $1 << '/' << $3 << std::endl;}
      ;

assignment_expression
      : multiplicative_expression                               { $$ = $1; std::cout << $1 << std::endl;}                          
      | primary_expression EQUALS multiplicative_expression     { $$ = $1; std::cout << $1 << '=' << $3<< std::endl;}
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
void yyerror(char *s)
{
  fprintf(stderr, "%s\n",s);
}