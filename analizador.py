import json
import os
import ply.lex as lex
import ply.yacc as yacc

# List of token names.   This is always required
tokens = (
    'parentesis_O',
    'parentesis_C',
    'corchete_O',
    'corchete_C',
    'letters',
    'num',
)

# Regular expression rules for simple tokens
t_parentesis_O = r'\('
t_parentesis_C = r'\)'
t_corchete_O = r'\['
t_corchete_C = r'\]'


def busqueda_col(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# A regular expression rule with some action code


def t_num(t):
    r'(0|[0-9]+)'
    t.value = int(t.value)
    return t

# A regular expression rule with some action code


def t_letters(t):
    r'[a-zA-Z]+'
    t.type = 'letters'
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(t.lineno, busqueda_col(DATA, t),
          f"No se pudo reconocer el lexema '{t.value}'")
    t.lexer.skip(1)


def p_INITIAL(p):
    '''
    INITIAL : corchete_O L_INTS corchete_C
            | parentesis_O L_INTS parentesis_C
            | L_INTS
    '''
    if len(p) == 4:
        if p[1] == '[':
            p[0] = {'corchete_O': p[1],
                    'L_INTS': p[2], 'corchete_C': p[3]}
        elif p[1] == '(':
            p[0] = {'parentesis_O': p[1],
                    'Caracteres': p[2], 'parentesis_C': p[3]}
    else:
        p[0] = p[1]


def p_L_INTS(p):
    '''
    L_INTS : L_INTS INTS
           | INTS
    '''
    if len(p) == 3:
        p[0] = p[1]
        p[0].append({'L_INTS INTS': p[2]})
    else:
        p[0] = [p[1]]


def p_INTS(p):
    '''
    INTS : num
         | letters
         | corchete_O L_INTS corchete_C
         | parentesis_O L_INTS parentesis_C
    '''
    if len(p) == 4:
        if p[1] == '[':
            p[0] = {'corchete_O': p[1], 'L_INTS': p[2], 'corchete_C': p[3]}
        elif p[1] == '(':
            p[0] = {'parentesis_O': p[1],
                    'L_INTS': p[2], 'parentesis_C': p[3]}
    else:
        p[0] = {"INTS": p[1], 'Tipo': p.slice[1].type}


def p_error(p):
    print(p)
    if p:
        print(f"Sintaxis no válida cerca de '{p.value}' ({p.type})")
    else:
        print("Ninguna instrucción válida")


lexer = lex.lex()

parser = yacc.yacc(start='INITIAL')

'''
Cadenas acpetadas
(20[012][0123456789])

Cadenas no aceptadas
abc(def
[01][01]01]
'''

DATA = '''
5859yty7abc
'''

# Give the lexer some input
lexer.input(DATA)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value)

ast = parser.parse(DATA, lexer)

print(json.dumps(ast, indent=4, sort_keys=False))


def graficarDot(ast):
    # -- lo primero es settear los valores que nos preocupan
    grafo = 'digraph "round-table" {\n \tnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'

    grafo += '\n \tA [label="{}"]'.format('INITIAL')
    grafo += '\n \tB [label="{}"]'.format('L_INTS')

    grafo += '\n \tA -> B'
    cont = 0
    apuntador = ''
    if type(ast) == 'dict':
        for key, value in ast.items():
            print(key)
    else:
        for dato in ast:
            for key, value in dato.items():
                if key == 'INTS':
                    letra_1 = f'B_{cont}'
                    grafo += '\n \t{} [label="{}"]'.format(letra_1, key)
                    apuntador = '\n \tB -> {}'.format(letra_1)
                    grafo += apuntador
                    cont += 1
                    # Parte dos
                    letra_2 = f'B_{cont}'
                    grafo += '\n \t{} [label="{}"]'.format(letra_2, value)
                    apuntador = '\n \t{} -> {}'.format(letra_1, letra_2)
                    grafo += apuntador
                    cont += 1
                
                elif key == 'L_INTS INTS':
                    for key, value in value.items():
                        if key == 'INTS':
                            letra_1 = f'B_{cont}'
                            grafo += '\n \t{} [label="L_INTS {}"]'.format(
                                letra_1, key)
                            apuntador = '\n \tB -> {}'.format(letra_1)
                            grafo += apuntador
                            cont += 1
                            # Parte dos
                            letra_2 = f'B_{cont}'
                            grafo += '\n \t{} [label="{}"]'.format(letra_2, value)
                            apuntador = '\n \t{} -> {}'.format(letra_1, letra_2)
                            grafo += apuntador
                            cont += 1
    grafo += '\n}'

    dot = "matriz_{}_dot.txt".format('prueba')
    with open(dot, 'w') as f:
        f.write(grafo)
    result = "matriz_{}.pdf".format('prueba')
    os.system("dot -Tpdf " + dot + " -o " + result)


graficarDot(ast)
