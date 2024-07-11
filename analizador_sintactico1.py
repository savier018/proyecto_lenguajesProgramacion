import ply.yacc as yacc
from analizador_lexico import tokens

# Lista global para almacenar los errores

variables = {}
funciones = {}
errores_sintacticos = []

def get_type(value):
    if isinstance(value, int):
        return 'Integer'
    elif isinstance(value, float):
        return 'Float'
    elif isinstance(value, str):
        return 'String'
    elif isinstance(value, list):
        return 'Array'
    elif isinstance(value, dict):
        return 'Hash'
    elif isinstance(value, bool):
        return 'Boolean'
    else:
        return 'Unknown'

# Reglas de producción del parser
def p_codigo(p):
    '''codigo : statement
              | codigo statement'''

def p_statement(p):
    '''statement : assign
                 | aritmeticExpresion
                 | control_structures
                 | data_structure
                 | while_loop
                 | case
                 | p_function_zero_parameter
                 | p_function_one_parameter
                 | p_function_two_parameter
                 | function_call
                 | impression
                 | data_input'''

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

def p_assign(p):
    '''assign : INSTANCE_VAR ASSIGN value
              | GLOBAL_VAR ASSIGN value
              | ID ASSIGN value
              | INSTANCE_VAR ASSIGN aritmeticExpresion
              | GLOBAL_VAR ASSIGN aritmeticExpresion
              | ID ASSIGN aritmeticExpresion
              | INSTANCE_VAR ASSIGN conditions
              | GLOBAL_VAR ASSIGN conditions
              | ID ASSIGN conditions
              | INSTANCE_VAR ASSIGN data_structure
              | GLOBAL_VAR ASSIGN data_structure
              | ID ASSIGN data_structure'''

def p_aritmeticExpresion(p):
    '''aritmeticExpresion : value operator value
                          | value operator function_call
                          | aritmeticExpresion operator value
                          | LPAREN aritmeticExpresion RPAREN
                          | LPAREN aritmeticExpresion RPAREN operator value'''
    if not isinstance(p[1],str) or p[1] in variables:
        if isinstance(p[1], int) or isinstance(p[1], float) or isinstance(p[1], p_aritmeticExpresion):
            pass
        else:
            genLogsSemantico(f"{p[1]} no es un NUMBER o una Expresion")
    else: 
        print(f"Error Semantico: la variable {p[1]} no ha sido inicializada") 
        genLogsSemantico(f"la variable {p[1]} no ha sido inicializada")
        return
    if not isinstance(p[3],str) or p[3] in variables:
        if isinstance(p[3], int) or isinstance(p[3], float) or isinstance(p[1], p_aritmeticExpresion):
            pass
        else:
            genLogsSemantico(f"{p[3]} no es un NUMBER o una Expresion")
    else: 
        genLogsSemantico(f"la variable {p[3]} no ha sido inicializada")
        return

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD
                '''
    
def p_conditions(p):
    '''conditions : condition
                  | condition conector conditions
                  | condition conector LPAREN conditions RPAREN'''

def p_condition(p):
    '''condition : value operComp value
                 | value operComp aritmeticExpresion'''
    
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
    
def p_control_structures(p):
    '''control_structures : if_block
                          | if_block elsif_blocks
                          | if_block elsif_blocks else_block
                          | if_block else_block
                          '''

def p_if_block(p):
    '''if_block : IF conditions codigo
                | IF conditions codigo END
                | IF LPAREN conditions RPAREN codigo
                | IF LPAREN conditions RPAREN codigo END'''

def p_elsif_blocks(p):
    '''elsif_blocks : elsif_block
                    | elsif_blocks elsif_block'''

def p_elsif_block(p):
    '''elsif_block :  ELSIF conditions RPAREN codigo
                    | ELSIF LPAREN conditions RPAREN codigo'''

def p_else_block(p):
    '''else_block : ELSE codigo END'''

def p_while_loop(p):
    '''while_loop : WHILE conditions codigo END
                  | WHILE LPAREN conditions RPAREN codigo END
                  | WHILE conditions DO codigo END
                  | WHILE LPAREN conditions RPAREN DO codigo END'''

def p_case(p):
    '''case : CASE value whens END'''

def p_whens(p):
    '''whens : whens when
             | when'''
    
def p_when(p):
    '''when : WHEN value codigo
            | ELSE codigo'''

def p_data_structure(p):
    '''data_structure : array
                      | hash
                      | set'''

def p_emptyarray(p):
    '''array : LBRACKET RBRACKET'''

def p_array(p):
    '''array : LBRACKET values RBRACKET'''

def p_empty_hash(p):
    '''hash : LBRACE RBRACE'''

def p_hash(p):
    '''hash : LBRACE hash_contents RBRACE'''

def p_hash_contents(p):
    '''hash_contents : hash_pair
                     | hash_contents COMMA hash_pair'''

def p_hash_pair(p):
    '''hash_pair : value COLON value'''
    
def p_empty_set(p):
    '''set : SET LPAREN LBRACKET RBRACKET RPAREN'''

def p_set(p):
    '''set : SET LPAREN LBRACKET values RBRACKET RPAREN'''

def p_function_zero_parameter(p):
    '''p_function_zero_parameter : DEF ID LPAREN RPAREN codigo END'''

def p_function_one_parameter(p):
    '''p_function_one_parameter : DEF ID LPAREN param RPAREN codigo END
                                | DEF ID LPAREN param RPAREN codigo RETURN p_expression END
                                | DEF ID LPAREN param RPAREN codigo p_function_control_structures END
                                | DEF ID LPAREN param RPAREN p_function_control_structures codigo END
                                | DEF ID LPAREN param RPAREN p_function_control_structures RETURN p_expression END
                                | DEF ID LPAREN param RPAREN p_function_control_structures END'''

def p_function_two_parameter(p):
    '''p_function_two_parameter : DEF ID LPAREN params RPAREN codigo END
                                | DEF ID LPAREN params RPAREN codigo RETURN p_expression END
                                | DEF ID LPAREN params RPAREN p_function_control_structures END
                                | DEF ID LPAREN params RPAREN p_function_control_structures codigo END
                                | DEF ID LPAREN params RPAREN p_function_control_structures RETURN p_expression END'''

def p_function_control_structures(p):
    '''p_function_control_structures : p_function_if_conditions
                                     | p_function_if_conditions p_function_else_conditions'''

def p_function_if_conditions(p):
    '''p_function_if_conditions : IF conditions RETURN p_expression
                                | IF LPAREN conditions RPAREN RETURN p_expression
                                | IF conditions codigo RETURN p_expression
                                | IF LPAREN conditions RPAREN codigo RETURN p_expression
                                | IF conditions RETURN p_expression END
                                | IF LPAREN conditions RPAREN RETURN p_expression END
                                | IF conditions codigo RETURN p_expression END
                                | IF LPAREN conditions RPAREN codigo RETURN p_expression END'''
    
def p_function_else_conditions(p):
    '''p_function_else_conditions : ELSE RETURN p_expression END
                                  | ELSE codigo RETURN p_expression END'''
    
def p_expression(p):
    '''p_expression : value
                    | aritmeticExpresion'''

def p_function_call(p):
    '''function_call : ID LPAREN RPAREN
                     | ID LPAREN params RPAREN
                     | ID LPAREN param RPAREN'''

def p_param(p):
    '''param : value
             | aritmeticExpresion'''

def p_params(p):
    '''params : value COMMA value
              | aritmeticExpresion COMMA aritmeticExpresion'''

def p_impression(p):
    '''impression : PRINT LPAREN value RPAREN
                  | PRINT value
                  | PUTS LPAREN value RPAREN
                  | PUTS value
                  | P LPAREN value RPAREN
                  | P value'''
    
def p_data_input(p):
    '''data_input : ID ASSIGN GETS STRING
                  | INSTANCE_VAR ASSIGN GETS STRING
                  | GLOBAL_VAR ASSIGN GETS STRING
                  | ID ASSIGN GETS NUMBER
                  | INSTANCE_VAR ASSIGN GETS NUMBER
                  | GLOBAL_VAR ASSIGN GETS NUMBER'''

def p_error(p):
    if p:
        error_message = f"Syntax error in input! {p.value}', line {p.lineno}"
        errores_sintacticos.append(error_message)
    else:
        errores_sintacticos.append("Syntax error at EOF")

# Construcción del parser
parser = yacc.yacc()

def analizar_codigoS(codigo):
    parser.parse(codigo)

def genLogsSemantico(error):
    error_message = f"Semantic Error in input! {error}"
    errores_sintacticos.append(error_message)
    print(error_message)

    

def checkErrorsSS():
    if len(errores_sintacticos)==0:
        return False
    else:
        return True
    
def getErrorsSS():
    return errores_sintacticos

def deleteErrorsSS():
    errores_sintacticos.clear()

# Ejemplo de uso
if __name__ == "__main__":
    codigo_ruby = """
    set = Set([1, 2, 3])
    """
    errores = analizar_codigo_ruby(codigo_ruby)
    if errores:
        print("Errores sintácticos encontrados:")
        for error in errores:
            print(error)
    else:
        print("No se encontraron errores sintácticos.")

