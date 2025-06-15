# Set y sus métodos en Python: 
## Los sets son una estructura de datos muy útil cuando quieres almacenar elementos únicos, 
## sin repeticiones, y realizar operaciones como un matemático: unión, intersección, diferencia, etc.

## Un set es una colección no ordenada, sin elementos duplicados, y mutable.
frutas = {"manzana", "banana", "naranja"}
print(frutas)  # {'manzana', 'banana', 'naranja'}

## Se usan llaves {} como los diccionarios, pero sin pares clave:valor.
## También puedes usar set() para crearlos.

# ¿Por qué usar sets?
## - Para eliminar duplicados fácilmente
## - Para realizar operaciones matemáticas entre grupos de datos
## - Para comprobar existencia rápida (in)


# Métodos y operaciones de sets
## Agregar elementos
frutas = {"pera", "uva"}
frutas.add("mango")     # Agrega un nuevo elemento
print(frutas)           # {'uva', 'mango', 'pera'}

## Eliminar elementos
frutas.remove("pera")   # Elimina "pera" (lanza error si no existe)
print(frutas)           # {'uva', 'mango'}
frutas.discard("uva")   # Elimina sin error si no existe
print(frutas)           # {'mango'}
frutas.clear()          # Elimina todo el contenido
print(frutas)           # set()


## Operaciones entre sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6} - Devuelve un nuevo conjunto con elementos del conjunto y todos los demás.
print(a.intersection(b)) # {3, 4} - Devuelve un nuevo conjunto con elementos comunes al conjunto y todos los demás.
print(a.difference(b))   # {1, 2} - Devuelve un nuevo conjunto con elementos del conjunto que no están en los otros.
print(b.difference(a))   # {5, 6} - Devuelve un nuevo conjunto con elementos del conjunto que no están en los otros.
print(a.symmetric_difference(b))  # {1, 2, 5, 6} - Devuelve un nuevo conjunto con elementos en el conjunto o en el otro, pero no en ambos.


## Comprobaciones
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))    # True - Informar si otro conjunto contiene este conjunto.
print(b.issuperset(a))  # True - Informar si este conjunto contiene otro conjunto.  
print(a.isdisjoint({6, 7}))  # True (no comparten elementos) - Devuelve Verdadero si dos conjuntos tienen una intersección nula.


## Recorrer un set
colores = {"rojo", "verde", "azul"}
for color in colores:
    print(color)


## Ejemplo práctico: eliminar duplicados
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6]
sin_repetidos = set(numeros)
print(sin_repetidos)  # {1, 2, 3, 4, 5}


## Lo que no puedes hacer con sets
## ❌ No acceder por índice: mi_set[0] da error
## ❌ No hay orden
## ❌ No puedes tener listas o diccionarios dentro de un set (deben ser elementos inmutables)

##  Acción	                    Método/Operación
### Agregar	                    .add(elem)
### Eliminar	                .remove(), .discard()
### Limpiar	                    .clear()
### Unión	                    `a
### Intersección	            a & b o a.intersection(b)
### Diferencia	                a - b
### Diferencia simétrica	    a ^ b

print("-------------")

## Ejercicio 1: Eliminar duplicados de una lista
# Dada esta lista con elementos repetidos:
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(numeros)
# 1. Crea un set a partir de esa lista
setNumeros = set(numeros)
print(type(setNumeros))
print(setNumeros)
# 2. Convierte el set de nuevo en lista y muéstrala sin duplicados
numeros = list(setNumeros)
print(numeros)


## Ejercicio 2: Palabras únicas
# Pregunta al usuario una frase:
frase = input("Escribe una frase: ")
print(frase)
# 1. Divide la frase en palabras
# 2. Guarda solo las palabras únicas usando un set
setPalabras = set(frase.split(sep=" ")) 
print(setPalabras)
# 3. Muestra cuántas palabras distintas escribió
print(len(setPalabras))



## Ejercicio 3: Alumnos comunes en dos materias
materia1 = {"Ana", "Luis", "Carlos", "Valeria"}
materia2 = {"Carlos", "Valeria", "Mario", "Diana"}
print(materia1)
print(materia2)
# 1. Muestra los alumnos que están en ambas materias
print(materia1.intersection(materia2))
# 2. Muestra los que están solo en la primera
print(materia1.difference(materia2))
# 3. Muestra todos los alumnos sin repetir nombres
print(materia1.union(materia2))


## Ejercicio 4: Números pares e impares sin repetir
numeros = [1, 2, 3, 2, 4, 5, 6, 7, 8, 4, 6, 7]
# 1. Usa sets para separar números pares e impares únicos
pares = set()
impares = set()

for num in numeros:
    if num % 2 == 0:
        pares.add(num)
    else:
        impares.add(num)

# 2. Muestra los dos sets resultantes
print(pares)
print(impares)


## Ejercicio 5: Encuentra la diferencia simétrica
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Muestra los elementos que están en uno u otro, pero no en ambos
print(a.difference(b))
print(b.difference(a))
# (diferencia simétrica)
print(a.symmetric_difference(b))