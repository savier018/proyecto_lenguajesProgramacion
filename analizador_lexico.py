import ply.lex as lex
from datetime import datetime

error_messages = []

def checkErrorsL():
    if len(error_messages)==0:
        return False
    else:
        return True
    
def getErrorsL():
    return error_messages

def deleteErrorsL():
    error_messages.clear()

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COMMA', 'DOT','DOTS', 'COLON', 'SEMICOLON', 'MOD',
    'EQUAL', 'NOTEQUAL', 'GREATERTHAN', 'LESSTHAN', 'GREATEROREQUAL', 'LESSOREQUAL',
    'ASSIGN', 'INSTANCE_VAR', 'GLOBAL_VAR', 'CONST', 'APOSTROPHE', 'DAPOSTROPHE', 'LBRACKET', 'RBRACKET'
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
    'gets':'GETS',
    'set':'SET'
}

tokens = tokens + list(reserved_words.values())

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
t_DOTS = r'\.\.'
t_COLON = r':'
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

def t_NUMBER(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value) if '.' in t.value or 'e' in t.value or 'E' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.value = t.value[1:-1]  # Remove the surrounding quotes
    return t

# Comentarios
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar los comentarios

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t\f\n\r'

def t_error(t):
    global error_messages
    error_message = f"Carácter ilegal '%s'" % t.value[0]
    error_messages.append(error_message)
    print(len(error_messages))
    print(error_message)
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()


# Analizar el código y generar logs
def analizar_codigoL(codigo):
    lexer.input(codigo)
    tokens_reconocidos = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        tokens_reconocidos.append(tok)

