# GRAMATICA HOJA DE TRABAJO 2

## Alfabeto

### Simbolos Terminales

#### Expresiones Regulares


| Token             | Patrón      |
|-------------------|-------------|
|   parentesis_O    | (           |
|   parentesis_C    | )           |
|   corchete_O      | [           |
|   corchete_C      | ]           |
|   letters         | [a-zA-Z]+   |
|   num             | [0-9]+      |

### Simbolos no terminales

| Token             | Descripción |
|-------------------|-------------|
|   L_INST          | Lista de expresiones |

## Sintáxis

#### Precedencia 


| Precedencia       | Operador    |    Asociatividad    |
|-------------------|-------------|---------------------|
|   2               | Agrupación  |  Ninguna          |
|   1               | Acceso a arreglo  |  izquierda          |

## Producciones

```

Simbolo incial = INITIAL

INITIAL : parentesis_o L_INTS parentesis_c
       | corchete_o L_INTS corchete_c
       | L_INTS

L_INTS : L_INTS INTS
       | INST   

INTS : num
       | letters
       | corchete_O L_INTS corchete_C
       | parentesis_O L_INTS parentesis_C

``` 

# Arbol Sintactico

![Arbol Sintacto](imagenes/arbol.png)
![Arbol Sintacto 2](imagenes/arbol2.png)


# Errores Sintacticos
![Error Sintactico](imagenes/Error.png)

