%{
    #include <stdio.h> 
	#include "y.tab.h"

    int     LINE_NO = 0;
%}

%%

"let"               return LET;
[\w_]+[\w_\d]*      return VAR;
[ \t]               ;
\n                  ++LINE_NO;
.                   printf("unexpected character %s at line %d\n", yytext, LINE_NO); 
%%

yywrap()
{
	return 1;
}