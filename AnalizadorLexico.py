import ply.lex as lex

#DIEGO CONTRERAS

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COMMA', 'DOT', 'SEMICOLON', 'MOD' ,
    'EQUAL', 'NEGATION', 'GREATERTHAN', 'LESSERTHAN', 'GREATEREEQUAL', 'LESSEREEQUAL',
    'ASSIGN',
]

reserved_words = {
    'def': 'DEF',
    'class': 'CLASS',
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
     'nil': 'NIL',
    'return': 'RETURN',
    "for": "FOR",
    "print": "PRINT",
    "return": "RETURN",
    "True": "TRUE",
    "False": "FALSE",
    "None": "NONE",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "in": "IN"
}

tokens = tokens + list(keywords.values())


