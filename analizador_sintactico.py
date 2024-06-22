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
    

def p_values(p):
    '''values : value 
    | value COMMA values'''
    
# Try and add here about PEDMAS

def p_expresionAritmetica(p):
    '''expresionAritmetica : value operator value '''


def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''
    
def p_emptyarray(p):
    '''array: LBRACKET RBRACKET'''

def p_tuplaVacia(p):
    '''tupla : LPAREN RPAREN'''


def p_array(p):
    '''array : LPAREN values RPAREN'''


#ADD HERE ABOUT CASE


#ADD HERE ABOUT SIMPLE FUNCION DECLARATION.



#Impresión y solicitud de datos



# Diego´s part ends here.




parser = yacc.yacc()