# DIEGO CONTRERAS
import ply.yacc as yacc
from analizador_lexico import tokens

def p_error(p):
    print(f"Syntax error in input! {p.value}', line {p.lineno}")

# Definir producción inicial
def p_program(p):
    '''program : statement_list'''

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''

def p_statement(p):
    '''statement : assign
                 | impression
                 | tupla
                 | conditions
                 | while_loop
                 | case
                 | Sfunction
                 | array
                 | p_SfunctionINV
                 | aritmeticExpresion
                 | operator
                 '''

def p_assign(p):
    '''assign : INSTANCE_VAR ASSIGN value
              | GLOBAL_VAR ASSIGN value
              '''

def p_value(p):
    '''value : NUMBER
            |  STRING
            |  BOOLEAN'''

# def p_code(p):
#     '''code : aritmeticExpresion
#               | impression
#               | tupla
#               | assign
#               | conditions
#               | while_loop'''


def p_values(p):
    '''values : value
              | value COMMA values'''

# Try and add here about PEDMAS arithmetic equation

def p_aritmeticExpresion(p):
    '''aritmeticExpresion : value operator value '''


def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''

def p_emptyarray(p):
    '''array : LBRACKET RBRACKET'''

def p_array(p):
    '''array : LBRACKET values RBRACKET'''

#ADD HERE ABOUT CASE

def p_conector(p):
    '''conector : AND
                | OR'''

def p_operComp(p):
    '''operComp : LESSTHAN
                | GREATERTHAN'''

def p_condition(p):
    '''condition : value operComp value'''

def p_conditions(p):
    '''conditions : condition
                  | condition conector conditions'''

def p_when(p):
    '''when : WHEN conditions statement_list'''

def p_whens(p):
    '''whens : when
             | whens'''

def p_case(p):
    '''case : CASE whens END'''

#ADD HERE ABOUT SIMPLE FUNCION DECLARATION WITHOUT PARAMETERS.

def p_Sfunction(p):
    '''Sfunction : DEF ID statement_list END'''

def p_SfunctionINV(p):
    '''p_SfunctionINV : ID
                      | ID LPAREN RPAREN'''

# RECORDAR PUTS DA SALTO DE PAGINAS AGREGAR DE UNA FORMA.

#Impresión y solicitud de datos

def p_impression(p):
    '''impression : PRINT LPAREN values RPAREN
                  | PRINT values
                  | PUTS values
                  | PUTS LPAREN values RPAREN
                  | P LPAREN values RPAREN
                  | P values'''

#solicitud de datos
def dataIn(p):
    '''dataIn: ASSIGN GETS '''

# While loop Alexis Loor
def p_while_loop(p):
    '''while_loop : WHILE condition DO statement_list END'''

# Definicion para 'tupla'
def p_tupla(p):
    '''tupla : LPAREN values RPAREN'''

# Diego´s part ends here.
parser = yacc.yacc()


while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print (result)