import ply.lex as lex
import os
from datetime import datetime

# DIEGO CONTRERAS

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COMMA', 'DOT', 'SEMICOLON', 'MOD',
    'EQUAL', 'NOTEQUAL', 'GREATERTHAN', 'LESSTHAN', 'GREATEROREQUAL', 'LESSOREQUAL',
    'ASSIGN', 'INSTANCE_VAR', 'GLOBAL_VAR', 'CONST', 'APOSTROPHE', 'DAPOSTROPHE', 'LBRACKET', 'RBRACKET', 'BOOLEAN'
]

reserved_words = {
    'def': 'DEF',
    'class': 'CLASS',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'do': 'DO',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'print': 'PRINT',
    'return': 'RETURN',
    'nil': 'NIL',
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'in': 'IN',
    'None': 'NONE',
    'end': 'END',
    'puts': 'PUTS',
    'case': 'CASE',
    'when': 'WHEN',
    'p': 'P',
    'gets': 'GETS'
}

tokens = tokens + list(reserved_words.values())

""" SAVIER ACOSTA
Reglas de expresiones regulares para tokens """

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_DOT = r'\.'
t_SEMICOLON = r';'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_ASSIGN = r'='
t_APOSTROPHE = r'\''
t_DAPOSTROPHE = r'\"'
t_BOOLEAN = r'(true|false)'


# ID (Variables locales, clases, nombres de funciones)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t


# Variable de instancia
def t_INSTANCE_VAR(t):
    r'@[a-zA-Z_][a-zA-Z0-9_]*'
    return t


# Variable global o constante
def t_GLOBAL_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'GLOBAL_VAR' if not t.value[1:].isupper() else 'CONST'
    return t


# AlexisLoor
# Reglas para números, cadenas y caracteres ignorados
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\".*?\"'
    t.value = str(t.value)
    return t


t_ignore = ' \t\f\n\r'


def t_error(t):
    print(f"Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# Construcción del lexer
lexer = lex.lex()


# # Analizar el código y generar logs
# def analizar_codigo(codigo, usuario_git):
#     lexer.input(codigo)
#     tokens_reconocidos = []
#
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)
#         tokens_reconocidos.append(tok)
#
#     fecha_hora = datetime.now().strftime('%d%m%Y-%Hh%M')
#
#     nombre_archivo_log = f"lexico-{usuario_git}-{fecha_hora}.txt"
#
#     if not os.path.exists('logs'):
#         os.makedirs('logs')
#
#     ruta_archivo_log = os.path.join('logs', nombre_archivo_log)
#
#     with open(ruta_archivo_log, 'w') as archivo_log:
#         for token in tokens_reconocidos:
#             archivo_log.write(f"{token}\n")
#
#     print(f"Log guardado en: {ruta_archivo_log}")

#
# # Testing de algoritmos
# codigo_ruby_alexisloor = '''
# def getFibonacci(n)
#   firstTerm = 0
#   secondTerm = 1
#   nextTerm = 0
#   counter = 1
#   result = []
#   puts "The first #{n} terms of Fibonacci series are:-"
#   result.push(firstTerm)
#   while(counter <= n + 1)
#     if(counter <= 1)
#         nextTerm = counter
#     else
#         result.push(nextTerm)
#         nextTerm = firstTerm + secondTerm
#         firstTerm = secondTerm
#         secondTerm = nextTerm
#     end
#     counter += 1
#   end
#
#   puts result.to_s
# end
# '''
#
# analizar_codigo(codigo_ruby_alexisloor, "alexisloor")
#
# codigo_ruby_ItsDiegoTBG = '''
# def factorial(n)
#     if n == 0
#         return 1
#     else
#         return n * factorial(n-1)
#     end
# end
# '''
#
# analizar_codigo(codigo_ruby_ItsDiegoTBG, "ItsDiegoTBG")
#
#
# codigo_ruby_savier018 = '''
# def suma_numeros_naturales(n)
#     suma = 0
#     for i in 1..n
#         suma += i
#     end
#     return suma
# end
#
# puts "Ingresa un número:"
# n = 10
#
# resultado = suma_numeros_naturales(n)
# '''
#
# analizar_codigo(codigo_ruby_savier018, "savier018")
