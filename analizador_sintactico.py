# DIEGO CONTRERAS
import ply.yacc as yacc
from analizador_lexico import tokens
import os
from datetime import datetime


# PRODUCCIÓN INICIAL

variables = {}

def p_codigo(p):
    '''codigo : statement
              | codigo statement'''
    
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
             | INSTANCE_VAR
             | GLOBAL_VAR
             | ID'''
    if isinstance(p[1],str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

def p_values(p):
    '''values : value
              | value COMMA values'''

# MENSAJE DE ERROR DEL ANALIZADOR SINTÁCTICO
def p_error(p):
    error_message = f"Syntax error in input! {p.value}', line {p.lineno}"
    print(error_message)
    now = datetime.now()
    timestamp = now.strftime("%d%m%Y-%Hh%M")
    
    user = "alexisloor"  
    log_filename = f"logs/sintactico-{user}-{timestamp}.txt"
    
    with open(log_filename, "a") as log_file:
        log_file.write(error_message + "\n")

# DEFINICIÓN DE VARIABLES
def p_assign(p):
    '''assign : INSTANCE_VAR ASSIGN value
              | GLOBAL_VAR ASSIGN value
              | ID ASSIGN value
              | INSTANCE_VAR ASSIGN data_structure
              | GLOBAL_VAR ASSIGN data_structure
              | ID ASSIGN data_structure'''
    variables[p[1]] = p[3]

# EXPRESIONES ARITMÉTICAS CON UNO O MÁS OPERADORES
def p_aritmeticExpresion(p):
    '''aritmeticExpresion : value operator value
                          | aritmeticExpresion operator value'''
    if not isinstance(p[1],str) or p[1] in variables:
        if isinstance(p[1], int) or isinstance(p[1], float) or isinstance(p[1], p_aritmeticExpresion):
            pass
        else:
            print(f"Error semantico, {p[1]} no es un NUMBER o una Expresion")
    else: 
        print(f"Error Semantico: la variable {p[1]} no ha sido inicializada") 
        return
    if not isinstance(p[3],str) or p[3] in variables:
        if isinstance(p[3], int) or isinstance(p[3], float) or isinstance(p[1], p_aritmeticExpresion):
            pass
        else:
            print(f"Error semantico, {p[3]} no es un NUMBER o una Expresion")
    else: 
        print(f"Error Semantico: la variable {p[3]} no ha sido inicializada") 
        return

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD
                | LPAREN aritmeticExpresion RPAREN'''

# ESTRUCTURAS DE DATOS
def p_data_structure(p):
    '''data_structure : array
                      | tupla
                      | hash'''

# IMPLEMENTACIÓN DEL ARRAY
def p_emptyarray(p):
    '''array : LBRACKET RBRACKET'''

def p_array(p):
    '''array : LBRACKET values RBRACKET'''

# IMPLEMENTACIÓN DEL HASH
def p_empty_hash(p):
    '''hash : LBRACE RBRACE'''

def p_hash(p):
    '''hash : LBRACE hash_contents RBRACE'''

def p_hash_contents(p):
    '''hash_contents : hash_pair
                     | hash_contents COMMA hash_pair'''

def p_hash_pair(p):
    '''hash_pair : value COLON value'''

# CONDICIONES CON UNO O MÁS CONECTORES
def p_conditions(p):
    '''conditions : condition
                  | condition conector conditions'''

def p_condition(p):
    '''condition : value operComp value
                 | value operComp aritmeticExpresion '''

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

# CONDICIONALES IF, ELSIF, ELSE
def p_control_structures(p):
    '''control_structures : if_block END
                          | if_block elsif_blocks
                          | if_block elsif_blocks else_block
                          | if_block else_block'''

def p_if_block(p):
    '''if_block : IF LPAREN condition RPAREN codigo'''

def p_elsif_blocks(p):
    '''elsif_blocks : elsif_block
                    | elsif_blocks elsif_block'''

def p_elsif_block(p):
    '''elsif_block : ELSIF condition codigo'''

def p_else_block(p):
    '''else_block : ELSE codigo END'''

# CONDICIONAL CASE-WHEN
def p_when(p):
    '''when : WHEN conditions codigo'''

def p_whens(p):
    '''whens : when
             | whens when'''

def p_case(p):
    '''case : CASE whens END'''

# DECLARACIÓN SIMPLE DE FUNCIÓN SIN PARÁMETROS
def p_Sfunction(p):
    '''Sfunction : DEF ID codigo END'''

def p_SfunctionINV(p):
    '''p_SfunctionINV : ID
                      | ID LPAREN RPAREN'''

# FUNCIONES DE 1 Y 2 PARÁMETROS
def p_function_one_parameter(p):
    '''p_function_one_parameter : DEF ID LPAREN ID RPAREN codigo END'''

def p_function_two_parameter(p):
    '''p_function_two_parameter : DEF ID LPAREN ID COMMA ID RPAREN codigo END'''

# IMPRESIÓN Y SOLICITUD DE DATOS
def p_impression(p):
    '''impression : PRINT LPAREN values RPAREN
                  | PRINT values
                  | PUTS values
                  | PUTS LPAREN values RPAREN
                  | P LPAREN values RPAREN
                  | P values
                  | PRINT
                  | PUTS'''

def p_dataIn(p):
    '''dataIn : ID ASSIGN GETS
              | INSTANCE_VAR ASSIGN GETS
              | GLOBAL_VAR ASSIGN GETS'''

# BUCLE WHILE
def p_while_loop(p):
    '''while_loop : WHILE LPAREN conditions RPAREN codigo END'''

# DEFINICIÓN DE TUPLA
def p_tupla(p):
    '''tupla : LPAREN values RPAREN'''

# CONSTRUCCIÓN DEL PARSER
parser = yacc.yacc()



def analizar_codigo(codigo, usuario_git):
    try:
        parser.parse(codigo)
        print("Análisis sintáctico exitoso. No se encontraron errores.")
        fecha_hora = datetime.now().strftime('%d%m%Y-%Hh%M')
        nombre_archivo_log = f"sintactico-{usuario_git}-{fecha_hora}.txt"
        if not os.path.exists('logs'):
            os.makedirs('logs')
        ruta_archivo_log = os.path.join('logs', nombre_archivo_log)
        with open(ruta_archivo_log, 'w') as archivo_log:
            archivo_log.write("Análisis sintáctico exitoso. No se encontraron errores.")
        print(f"Log guardado en: {ruta_archivo_log}")
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        fecha_hora = datetime.now().strftime('%d%m%Y-%Hh%M')
        nombre_archivo_log = f"sintactico-error-{usuario_git}-{fecha_hora}.txt"
        if not os.path.exists('logs'):
            os.makedirs('logs')
        ruta_archivo_log = os.path.join('logs', nombre_archivo_log)
        with open(ruta_archivo_log, 'w') as archivo_log:
            archivo_log.write(f"Error de sintaxis:\n{str(e)}")
        print(f"Log de error guardado en: {ruta_archivo_log}")
    


codigo_ruby_ItsDiegoTBG = '''
def factorial(n)
    if n == 0
        return 1
    else
        return n * factorial(n-1)
    end
end
'''

codigo_ruby_ItsDiegoTBGValido = '''
def factorial(n)
    if n == 0
    end
end
'''

codigo_ruby_savier018 = '''
def suma_numeros_naturales(n)
   suma = 0
   for i in 1..n
        suma += i
     end
     return suma
 end

 puts "Ingresa un número:"
 n = 10

 resultado = suma_numeros_naturales(n) '''

codigo_ruby_alexisloor = '''
def getFibonacci(n)
  firstTerm = 0
  secondTerm = 1
  nextTerm = 0
  counter = 1
  result = []
  puts "The first #{n} terms of Fibonacci series are:-"
  while(counter <= n + 1)
    if(counter <= 1)
        nextTerm = counter
    else
        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
    end
  end
end
'''

analizar_codigo(codigo_ruby_alexisloor, "ItsDiegoTBG")