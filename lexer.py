import ply.lex as lex

tokens = (
    'Tipo_de_dato',
    'Palabra_reservada_main',
    'Parentesis_de_apertura',
    'Parentesis_de_cierre',
    'Llave_de_apertura',
    'Llave_de_cierre',
    'Identificador',
    'Punto_y_coma',
)

# Reglas de expresiones regulares para los tokens
t_Tipo_de_dato = r'int'
t_Palabra_reservada_main = r'main'
t_Parentesis_de_apertura = r'\('
t_Parentesis_de_cierre = r'\)'
t_Llave_de_apertura = r'\{'
t_Llave_de_cierre = r'\}'
t_Identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_Punto_y_coma = r';'
t_ignore = ' \t'

# Manejo de nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()