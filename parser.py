import ply.yacc as yacc
from lexer import tokens

# Reglas gramaticales
def p_programa(p):
    '''programa : funcion_main'''

def p_funcion_main(p):
    '''funcion_main : Palabra_reservada_main Parentesis_de_apertura Parentesis_de_cierre Llave_de_apertura declaraciones Llave_de_cierre'''

def p_declaraciones(p):
    '''declaraciones : declaracion
                    | declaraciones declaracion'''

def p_declaracion(p):
    '''declaracion : Tipo_de_dato Identificador Punto_y_coma'''

def p_error(p):
    if p:
        if p.type == 'PALABRA_RESERVADA_MAIN':
            print(f"Error de sintaxis en la línea {p.lineno}: La palabra reservada 'main' debe estar al inicio del programa y seguida de paréntesis.")
        elif not p.value:
            print(f"Error de sintaxis en la línea {p.lineno}: Se esperaba un identificador válido después de 'int'.")
        else:
            print(f"Error de sintaxis en la línea {p.lineno}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis: Fin de archivo inesperado.")

# Construcción del analizador sintáctico
parser = yacc.yacc()