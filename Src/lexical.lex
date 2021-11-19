D       [0-9]           /* digito */
L       [A-Za-z_]       /* letras */
H       [a-fA-F0-9]     /* hex */
E       [Ee][+-]?{D}?   /* Notacion cientifica */
FS		(f|F|l|L)
IS		(u|U|l|L)*


%{
    #include <stdio.h> 
	#include "syntactical.tab.h"
    int     LINE_NO = 1;
%}

%%

"."                                 {return (DOT);}
"*"                                 {return (MUL);}
"/"                                 {return (DIV);}
"let"                               {return (LET);}
"const"                             {return (CONST);}
"func"                              {return (FUNC);}       
"void"                              {return (VOID);}                    
"char"                              {return (CHAR);}                    
"int"                               {return (INT);}
"string"                            {return (STRING);}
"bool"                              {return (BOOL);}
"from"                              {return (FROM);} 
"float"                             {return (FLOAT);}                     
"="                                 {return (EQUALS);}
"++"                                {return (INC_OP);}
"--"                                {return (DEC_OP);}
"+"                                 {return (PLUS);}
"-"                                 {return (MINUS);}
"<="                                {return (LE_OP);}
">="                                {return (GE_OP);}
"=="                                {return (EQ_OP);}
"!="                                {return (NE_OP);}
"&&"                                {return (AND_OP);}
"||"                                {return (OR_OP);}
"if"                                {return (IF);}                     
"else"                              {return (ELSE);}
":"                                 {return (COLON);}
";"                                 {return (SEMICOLON);}
"->"                                {return (ARROW);}
"("                                 {return (RND_PAR_OPEN);}
")"                                 {return (RND_PAR_CLOSE);}
"["                                 {return (BOX_PAR_OPEN);}
"]"                                 {return (BOX_PAR_CLOSE);}
"{"                                 {return (CUR_PAR_OPEN);}
"}"                                 {return (CUR_PAR_CLOSE);}
","                                 {return (COMMA);}

\".*\"                              {return (STRING_LITERAL);}

[-+]?\\.[0-9]*                      {return (NUMERIC);}
[-+]?[0-9]*                         {return (NUMERIC);}

[a-zA-Z_]([a-zA-Z_0-9])*            {return (IDENTIFIER);}

[ \t]                               {}
\n                                  {++LINE_NO;}
.                                   {}

%%

int main(void)
{
   yyparse();
   return 0;
}

yywrap()
{
	return(1);
}