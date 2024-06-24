# DIEGO CONTRERAS

import ply.yacc as yacc
from analizador_lexico import tokens
import os
from datetime import datetime

def p_error(p):
    print("Syntax error in input!")

def p_assign(p):
    '''assign : INSTANCE_VAR ASSIGN value | GLOBAL_VAR ASSIGN value '''

def p_value(p):
    '''value : NUMBER
            |  STRING
            |  BOOLEAN'''
    
def p_code(p):
    '''code : aritmeticExpresion 
              | impresion
              | tupla
              | asignacion
              | condiciones'''
    

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
    '''array: LBRACKET RBRACKET'''

def p_array(p):
    '''array : LPAREN values RPAREN'''


#ADD HERE ABOUT CASE

def p_conector(p):
    '''conector : AND
                | OR'''

def p_operComp(p):
    '''operComp : LESSTHAN
                | MORETHAN'''

def p_condition(p):
    'condition : value operComp value'

def p_conditions(p):
    '''conditions : condition 
                  | condition conector conditions'''

def p_when(p):
    'when : WHEN conditions code'


def p_whens(p):
    '''whens : when 
                | whens'''

def p_case(p):
    '''case: CASE whens END'''



#ADD HERE ABOUT SIMPLE FUNCION DECLARATION WITHOUT PARAMETERS.

def p_Sfunction(p){
    '''Sfunction : DEF ID code END'''
}

def p_SfunctionINV(p){
    '''p_SfunctionINV : ID | ID LPAREN RPAREN'''
}

# RECORDAR PUTS DA SALTO DE PAGINAS AGREGAR DE UNA FORMA.

#Impresión y solicitud de datos

def p_impression(p):
    '''impression : PRINT LPAREN values RPAREN 
    | PRINT values 
    | PUTS values \n 
    | PUTS LPAREN values RPAREN \n 
    | P LPAREN values RPAREN 
    | P values'''

#solicitud de datos   

def dataIn(p):
    '''dataIn: ASSIGN GETS '''



# Diego´s part ends here.




parser = yacc.yacc()