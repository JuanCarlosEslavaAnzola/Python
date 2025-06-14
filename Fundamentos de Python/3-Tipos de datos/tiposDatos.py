# Tipos de datos en Python: En Python, cada valor tiene un tipo de dato, 
# que indica qué tipo de información es y qué operaciones se pueden hacer con él.

##  Tipo de dato        Descripción	                            Ejemplo
##  int	                Número entero	                        5, -3, 100
##  float	            Número decimal	                        3.14, -0.5
##  str (string)	    Texto o cadena de caracteres	        "hola", 'Python'
##  bool	            Booleano (Verdadero/Falso)	            True, False
##  list	            Lista (colección de elementos)	        [1, 2, 3], ["a", "b"]
##  tuple	            Tupla (como lista, pero inmutable)      (1, 2), ("a", "b")
##  dict	            Diccionario (clave:valor)	            {"nombre": "Ana"}
##  set	                Conjunto (colección sin repeticiones)	{1, 2, 3}

# Números (int y float)
entero = 10
decimal = 3.1416

print(entero)
print(decimal)

## Puedes hacer operaciones matemáticas:
suma = 2 + 3
print(f"Suma = 2 + 3 = {suma}")

division = 10 / 4   # devuelve float: 2.5
print(f"Division = 10 / 4 = {division}")

division_entera = 10 // 4  # resultado: 2
print(f"Division_entera = 10 // 4 = {division_entera}")


# Cadenas de texto (str)
nombre = "Juan"
saludo = 'Hola, ' + nombre
print(saludo)

## Puedes acceder a letras:
letra = nombre[0]  # "J"
print(letra)

## O usar funciones útiles:
print(nombre.upper())  # "JUAN"
print(nombre.lower())  # "juan"
print(len(nombre))     # longitud: 4


# Booleanos (bool)
es_mayor = True
tiene_licencia = False

print(f"El señor {nombre} es mayor de edad? {es_mayor}")
print(f"El señor {nombre} tiene licencia para conducir camion? {tiene_licencia}")

## Se usan en condiciones:
if es_mayor:
    print(f"El señor {nombre}, puede votar.")


# Listas (list)
numeros = [1, 2, 3, 4]
nombres = ["Ana", "Luis", "Pedro"]

print(numeros)  
print(nombres)

## Puedes acceder y modificar elementos:
print(nombres[0])  # "Ana"
nombres[1] = "Lucía"

## Y agregar más:
nombres.append("María")
print(nombres)


# Tuplas (tuple) Parecidas a las listas, pero no se pueden cambiar:
coordenadas = (10, 20, 30)
print(coordenadas)


# Diccionarios (dict) Guardan pares clave:valor
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # "Ana"

## Puedes agregar datos:
persona["ciudad"] = "Madrid"
print(persona)


# Conjuntos (set)
numeros = {1, 2, 3, 2, 3, 2, 1, 0}
print(numeros)  # {1, 2, 3}


# ¿Cómo saber el tipo de dato?
x = 5
print(type(x))  # <class 'int'>
print(type(numeros))   # <class 'set'>


# Ejercicio
nombre = "Sara"
edad = 28
altura = 1.65
es_estudiante = True
colores = ["rojo", "azul"]
coordenadas = (10, 20)
persona = {"nombre": "Sara", "edad": 28}
numeros_unicos = {1, 2, 3}

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))
print(type(colores))
print(type(coordenadas))
print(type(persona))
print(type(numeros_unicos))