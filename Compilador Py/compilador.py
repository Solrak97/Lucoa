# ------------------------------------------------------------
# main.py
#
# Punto de inicio 
# 
# ------------------------------------------------------------

from Compilador.lexing import lexer
from Compilador.syntactic import parser
from Compilador.generation import generar_codigo
import sys

if len(sys.argv) == 0:
    print("No se ha especificado ningun archivo")
    exit()

#   Carga del archivo CSV 
PATH = sys.argv[1]
data = ''

with open(PATH, mode='r', encoding='utf-8') as file:
    data = file.read()
 

#   Lexing
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: 
        break      
#    print(tok)


#   Reset del contador
lexer.lineno = 1


#   Se obtiene el objeto padre que contiene la informacion del archivo
parser.parse(data)

generar_codigo()