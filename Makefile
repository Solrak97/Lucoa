INCLUDE = Src/

lucoa: syntactical.tab.c syntactical.tab.h lex.yy.c
	gcc lex.yy.c syntactical.tab.c -I $(INCLUDE) -o lucoa 
	rm syntactical.tab.c syntactical.tab.h lex.yy.c

lex.yy.c: syntactical.tab.c syntactical.tab.h Src/lexical.lex
	lex Src/lexical.lex 

syntactical.tab.c syntactical.tab.h: Src/syntactical.y
	bison -d Src/syntactical.y  