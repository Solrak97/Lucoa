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

"let"                               {return (LET);}       
"void"                              {return (VOID);}                    
"char"                              {return (CHAR);}                    
"int"                               {return (INT);}
"string"                            {return (STRING);}
"bool"                              {return (BOOL);}                    
"="                                 {return (EQUALS);}
"++"                                {return (INC_OP);}
"--"                                {return (DEC_OP);}
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

[0-9]+                              {return (CONSTANT);}
[0-9]+"."[0-9]+                      {return (CONSTANT);}   /* Requiere revision */
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