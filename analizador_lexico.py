import ply.lex as lex

# DIEGO CONTRERAS

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COMMA', 'DOT', 'SEMICOLON', 'MOD' ,
    'EQUAL', 'NOTEQUAL', 'GREATERTHAN', 'LESSTHAN', 'GREATEROREQUAL', 'LESSOREQUAL',
    'ASSIGN', 'INSTANCE_VAR', 'GLOBAL_VAR', 'CONST'
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
    'None': 'NONE'
}

tokens = tokens + list(reserved_words.values())


""" SAVIER ACOSTA
Reglas de expresiones regulares para tokens """

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
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

