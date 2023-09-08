import ply.lex as lex

# Palabras reservadas
reserved = {
    'Proceso': 'Inicio_Proceso',
    'FinProceso': 'Fin_Proceso',
    'Si': 'Condiciones_Si',
    'Sino': 'Condiciones_Sino',
    'FinSi': 'Condiciones_FinSi',
    'mientras': 'Bucle',
    'Imprimir': 'Impresor',
    'entero': 'Dato_Int',
    'largo': 'Dato_Long',
    'flotante': 'Dato_Flotante',
    'caracter': 'Dato_Caracter',
    'booleano': 'Dato_Booleano',
}

# Lista de tokens
tokens = [
    'Identificador', 'Num_Entero', 'Num_Decimales', 'Op_Suma', 'Op_Resta',
    'Op_Multiplicacion', 'Op_Division', 'Mayor_Q', 'Menor_Q', 'Igualdad',
    'Comparacion', 'Mayor_Igual', 'Menor_Igual', 'Incremento',
    'Comparacion_Igualdad', 'Op_Logico', 'Sum_Asignacion', 'Decremento',
    'Cadena_Texto', 'Comentario', 'Inicio_Parentesis', 'Fin_Parentesis',
    'Punto_Coma', 'Parentesis_Abrir', 'Parentesis_Cerrar', 'Llave_Abrir',
    'Llave_Cerrar','Coma'
] + list(reserved.values())

# Expresiones regulares para los tokens
t_Op_Suma = r'\+'
t_Op_Resta = r'-'
t_Op_Multiplicacion = r'\*'
t_Op_Division = r'%|/'
t_Mayor_Q = r'>'
t_Menor_Q = r'<'
t_Igualdad = r'='
t_Comparacion = r'=='
t_Mayor_Igual = r'>='
t_Menor_Igual = r'<='
t_Incremento = r'\+\+'
t_Comparacion_Igualdad = r'!='
t_Op_Logico = r'OR'
t_Sum_Asignacion = r'\+='
t_Decremento = r'--'
t_Parentesis_Abrir = r'\('
t_Parentesis_Cerrar = r'\)'
t_Llave_Abrir = r'\{'
t_Llave_Cerrar = r'\}'
t_Coma = r'\,'


# Regla para manejar identificadores
def t_Identificador(t):
  r'[_a-zA-Z][_a-zA-Z0-9]*'
  t.type = reserved.get(t.value,
                        'Identificador')  # Verificar palabras reservadas
  return t


def t_Num_Decimales(t):
  r'\d+\.\d+'
  t.value = float(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


def t_Num_Entero(t):
  r'\d+'
  t.value = int(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# Regla para manejar comentarios
def t_Comentario(t):
  r'\/\/.*'
  return t  # Los comentarios se ignorarán


# Regla para manejar cadenas de texto
def t_Cadena_Texto(t):
  r'"([^"\\]|\\.)*"'
  t.value = str(t.value)
  return t


# Build the lexer
lexer = lex.lex()

# Prueba del analizador léxico
data = '''Proceso
Proceso
    flotante Promedio(entero x, entero y, entero z) {
        flotante promedio = (x + y + z) / 3
        retornar promedio
    }
    entero x = 10
    entero y = 20
    entero z = 30
    
    flotante resultado_promedio = Promedio(x, y, z)
    Imprimir "El promedio de " + x + ", " + y + " y " + z + " es: " + resultado_promedio

FinProceso
// Esto es un comentario de línea
'''

lexer.input(data)

for tok in lexer:
  print(tok.type, tok.value)
