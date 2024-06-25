# DIEGO CONTRERAS
import ply.yacc as yacc
from analizador_lexico import tokens

#PRODUCCIÓN INICIAL
def p_codigo(p):
    '''codigo : assign
              | impression
              | tupla
              | conditions
              | while_loop
              | case
              | Sfunction
              | array
              | p_SfunctionINV
              | p_function_one_parameter
              | p_function_two_parameter
              | aritmeticExpresion
              | operator
              | dataIn
              | control_structures
              | hash'''

def p_value(p):
    '''value : NUMBER
             | STRING
             | BOOLEAN
             | INSTANCE_VAR
             | GLOBAL_VAR
             | ID'''
    
def p_values(p):
    '''values : value
              | value COMMA values'''


#MENSAJE DE ERROR DEL ANALIZADOR SINTÁCTICO
def p_error(p):
    print(f"Syntax error in input! {p.value}', line {p.lineno}")


#DEFINICIÓN DE VARIABLES
def p_assign(p):
    '''assign : INSTANCE_VAR ASSIGN value
              | GLOBAL_VAR ASSIGN value
              | ID ASSIGN value
              | INSTANCE_VAR ASSIGN data_structure
              | GLOBAL_VAR ASSIGN data_structure
              | ID ASSIGN data_structure'''


#EXPRESIONES ARITMETICAS CON UNO O MAS OPERADORES
def p_aritmeticExpresion(p):
    '''aritmeticExpresion : value operator value
                          | aritmeticExpresion operator value'''

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''
    

#ESTRUCTURAS DE DATOS
def p_data_structure(p):
    '''data_structure : array
                      | tupla
                      | hash'''


#IMPLEMENTACIÓN DEL ARRAY
def p_emptyarray(p):
    '''array : LBRACKET RBRACKET'''

def p_array(p):
    '''array : LBRACKET values RBRACKET'''


#IMPLEMENTACIÓN DEL HASH
def p_empty_hash(p):
    '''hash : LBRACE RBRACE'''

def p_hash(p):
    '''hash : LBRACE hash_contents RBRACE'''

def p_hash_contents(p):
    '''hash_contents : hash_pair
                     | hash_contents COMMA hash_pair'''

def p_hash_pair(p):
    '''hash_pair : value COLON value'''


#CONDICIONES CON UNO O MÁS CONECTORES
def p_conditions(p):
    '''conditions : condition
                  | condition conector conditions'''
    
def p_condition(p):
    '''condition : value operComp value'''

def p_conector(p):
    '''conector : AND
                | OR'''

def p_operComp(p):
    '''operComp : LESSTHAN
                | GREATERTHAN
                | GREATEROREQUAL
                | LESSOREQUAL
                | EQUAL
                | NOTEQUAL'''


#CONDICIONALES IF, ELSIF, ELSE
def p_control_structures(p):
    '''control_structures : if_block
                          | if_block elsif_blocks
                          | if_block elsif_blocks else_block
                          | if_block else_block'''

def p_if_block(p):
    '''if_block : IF condition codigo END'''

def p_elsif_blocks(p):
    '''elsif_blocks : elsif_block
                    | elsif_blocks elsif_block'''

def p_elsif_block(p):
    '''elsif_block : ELSIF condition codigo'''

def p_else_block(p):
    '''else_block : ELSE codigo'''

#CONDICIONAL WHEN (?)
def p_when(p):
    '''when : WHEN conditions codigo'''

def p_whens(p):
    '''whens : when
             | whens'''

def p_case(p):
    '''case : CASE whens END'''

#ADD HERE ABOUT SIMPLE FUNCION DECLARATION WITHOUT PARAMETERS.

def p_Sfunction(p):
    '''Sfunction : DEF ID codigo END'''

def p_SfunctionINV(p):
    '''p_SfunctionINV : ID
                      | ID LPAREN RPAREN'''
    

#FUNCIONES DE 1 Y 2 PARAMETROS
def p_function_one_parameter(p):
    '''p_function_one_parameter : DEF ID LPAREN ID RPAREN codigo END'''

def p_function_two_parameter(p):
    '''p_function_two_parameter : DEF ID LPAREN ID COMMA ID RPAREN codigo END'''
    

# RECORDAR PUTS DA SALTO DE PAGINAS AGREGAR DE UNA FORMA.

#Impresión y solicitud de datos
def p_impression(p):
    '''impression : PRINT LPAREN values RPAREN
                  | PRINT values
                  | PUTS values
                  | PUTS LPAREN values RPAREN
                  | P LPAREN values RPAREN
                  | P values
                  | PRINT
                  | PUTS
                  '''

#solicitud de datos
def p_dataIn(p):
    '''dataIn : ID ASSIGN GETS
              | INSTANCE_VAR ASSIGN GETS
              | GLOBAL_VAR ASSIGN GETS '''

# While loop Alexis Loor
def p_while_loop(p):
    '''while_loop : WHILE condition DO codigo END'''

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