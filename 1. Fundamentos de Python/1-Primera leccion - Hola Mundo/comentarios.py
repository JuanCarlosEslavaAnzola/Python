# comentarios en Python
## Son líneas que no se ejecutan, se usan para explicar el código, desactivarlo temporalmente o dar contexto.

## Comentario de una sola línea
## Se escribe usando el símbolo #

# Esto es un comentario de una línea
nombre = "Luis"  # Guardamos el nombre del usuario
## Todo lo que esté después de # en esa línea no se ejecuta.

## Comentarios multilínea (docstring)
## Aunque Python no tiene comentarios multilínea oficiales como otros lenguajes, 
## puedes usar strings de varias líneas con comillas triples """ o ''' como una forma común de hacerlos.
## Se usan sobre todo para documentar funciones o bloques de código.

"""
Este programa calcula la edad
a partir del año de nacimiento.
Autor: Luis
"""
nombre = input("¿Nombre? ")


## Docstrings en funciones
## Los docstrings son una forma especial de comentario usado dentro de funciones, 
## clases o módulos para explicar qué hacen.
def saludar(nombre):
    """Esta función saluda al usuario por su nombre."""
    print(f"Hola {nombre}!")


## Puedes acceder a ese comentario con:
print(saludar.__doc__)


## ¿Para qué sirven los comentarios?
## - Explicar qué hace una parte del código
## - Anotar mejoras o cambios pendientes
## - Apagar partes del código sin borrarlas
## - Documentar funciones o scripts
## - Facilitar el mantenimiento

## Buenas prácticas
## No hagas esto:
# sumar 1
x = 0
x = x + 1

## Mejor:
# Incrementamos el contador en 1 porque 
x += 1