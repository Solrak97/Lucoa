SECTION .bss
	a: RESB 4
	b: RESB 4
	c: RESB 4
	d: RESB 4
	var: RESB 8
	_asign: RESB 1
SECTION .text
	
	;Asignacion de a, b a sus respectivos registros
	LOAD a, R2
	LOAD b, R3
	ADD R2, R3, R1
	
	;Asignacion de R1, c a sus respectivos registros
	MOV R1, R2
	LOAD c, R3
	MUL R1, R3, R1
	
	;Asignacion de R1, 4 a sus respectivos registros
	MOV R1, R2
	LOADI 4, R3
	DIV R1, R3, R1
	
	;Asignacion de b, c a sus respectivos registros
	LOAD b, R2
	LOAD c, R3
	ADD R2, R3, R1
	
	;Asignacion de R1, var a sus respectivos registros
	MOV R1, R2
	LOAD var, R3
	MUL R1, R3, R1
	
	;Asignacion de a, R1 a sus respectivos registros
	LOAD a, R2
	MOV R1, R3
	;Asuma que AND retorna a R1
	AND R2 R1, R1
	
	;Asignacion de 25, 7 a sus respectivos registros
	LOADI 25, R2
	LOADI 7, R3
	DIV R2, R3, R1
	
	;Asignacion de 2, 7 a sus respectivos registros
	LOADI 2, R2
	LOADI 7, R3
	MUL R2, R3, R1
	
	;Asignacion de R1, 65 a sus respectivos registros
	MOV R1, R2
	LOADI 65, R3
	;Asuma que CMP retorna a R1
	CMP R1, R3, R1
	
	;Asignacion de R1, R1 a sus respectivos registros
	MOV R1, R2
	MOV R1, R3
	;Asuma que CMP retorna a R1
	CMP R1, R1, R1
	
	;Asignacion de a, R1 a sus respectivos registros
	LOAD a, R2
	MOV R1, R3
	;Asuma que OR retorna a R1
	OR R2 R1, R1
