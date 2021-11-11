%{
    #include <stdio.h> 
	#include "y.tab.h"

    int     LINE_NO = 1;
%}

%%

"let"                               return LET_KW;
"loop"                              return LOOP_KW;
"while"                             return WHILE_KW;
"if"                                return IF_KW;
"else"                              return ELSE_KW;
"int" | "char" | "bool" | "float"               return PRIMITIVE;

[A-Za-z_]+[A-Za-z_0-9]*             return VAR_NAME;








[ \t]               ;
\n                  ++LINE_NO;
.                   printf("unexpected character %s at line %d\n", yytext, LINE_NO); 

%%

yywrap()
{
	return 1;
}