# Manejo de Errores en Python
## El manejo de errores te permite evitar que tu programa se caiga cuando ocurre un problema inesperado. 
## Es clave para crear programas robustos y confiables.

# Hay dos tipos principales:
## 1. Errores de sintaxis
## Ocurren cuando escribes mal el código. Ejemplo:
## print("Hola"
## SyntaxError: '(' was never closed
## No puedes atraparlos con manejo de errores. Debes corregirlos.

## 2. Excepciones (errores en tiempo de ejecución)
## Son errores que suceden mientras se ejecuta el código. Ejemplos:
## x = 5 / 0          # ZeroDivisionError
## lista = [1, 2]
## print(lista[10])   # IndexError
## Estos sí se pueden atrapar y manejar con try y except.

## Sintaxis de manejo de errores
##  try:
        # Código que puede causar error
##  except TipoDeError:
        # Código que se ejecuta si ocurre ese error

# Ejemplo básico:
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("¡Eso no es un número!")

# Varios except
## Puedes manejar diferentes tipos de errores con bloques separados:
try:
    x = int(input("Número: "))
    resultado = 10 / x
except ValueError: # Valor de argumento inapropiado (de tipo correcto).
    print("Debes escribir un número.")
except ZeroDivisionError: # El segundo argumento de una operación de división o módulo era cero.
    print("No se puede dividir por cero.")

# Uso de else y finally
try:
    x = int(input("Número 2: "))
except ValueError:
    print("Error al convertir.")
else:
    print("Todo salió bien, el número es", x)
finally:
    print("Esto siempre se ejecuta.")

## else: se ejecuta si no hubo errores
## finally: se ejecuta siempre, haya error o no


# Ejemplo práctico
try:
    archivo = open("datos.txt")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Fin del programa.")


# Lista de errores comunes
##  Error	¿Cuándo ocurre?
##  ValueError	Conversión incorrecta (como int("hola"))
##  ZeroDivisionError	Dividir por cero
##  TypeError	Operar tipos incompatibles
##  IndexError	Acceder a índice inexistente en listas
##  KeyError	Acceder a clave inexistente en diccionario
##  FileNotFoundError	Archivo no encontrado

##   ¿Por qué usar manejo de errores?
##  ✅ Previene caídas del programa
##  ✅ Mejora la experiencia del usuario
##  ✅ Permite recuperar o corregir fallos

print("-------------")

# Ejercicio 1: División segura
## Pide al usuario dos números y muestra el resultado de dividir el primero por el segundo.
## Maneja estos errores:
## - El usuario escribe texto en vez de número (ValueError)
## - División por cero (ZeroDivisionError)
try:
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    print(f"El resultado de {x} / {y} es: {x / y:.2f}")
except ValueError:
    print("El usuario escribe texto en vez de número ")
except ZeroDivisionError:
    print("División por cero")


# Ejercicio 2: Acceder a una lista
## Dada una lista fija, pide al usuario que ingrese una posición (índice) para mostrar el valor en esa posición.
## Maneja estos errores:
## - Índice fuera de rango (IndexError)
## - Índice no válido (si no es número → ValueError)
try:
    elementos = ["manzana", "banana", "naranja", "pera"]
    print("Lista:", elementos)
    x = int(input("Ingrese un numero del elemento que desea imprimir: "))
    print(elementos[x])
except IndexError:
    print("Índice fuera de rango (IndexError)")
except ValueError:
    print("Índice no válido (si no es número → ValueError)")

# Ejercicio 3: Abrir un archivo
## Pide al usuario que ingrese el nombre de un archivo para abrir y mostrar su contenido.
## Maneja el error si el archivo no existe (FileNotFoundError)
try:
    nombre = input("Ingresa el nombre del archivo: ")
    with open(nombre) as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe. (FileNotFoundError)")