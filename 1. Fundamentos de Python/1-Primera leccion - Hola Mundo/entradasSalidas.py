# Entrada y salida en Python
## Entrada de datos: input()
## La función input() permite leer datos desde el teclado.
## Lo que el usuario escriba se devuelve como texto (str), ¡siempre!
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)


## Si quieres usar ese dato como número, debes convertirlo:
edad = int(input("¿Qué edad tienes? "))
print("En 5 años tendrás", edad + 5)

## Puedes convertirlo a:
###     int() → para números enteros
###     float() → para decimales
###     bool() → para verdadero/falso
###     list() → para convertir a lista, si es adecuado


## Salida de datos: print()
## La función print() se usa para mostrar información por pantalla.
## Ejemplos:
print("Hola mundo")                         # texto
print("Tu edad es", edad)                   # variables
print("Suma:", 3 + 4)                       # operaciones
print(f"Hola {nombre}, tienes {edad}")      # f-strings (¡muy útiles!)


## Algunas opciones de print()
print("Hola", end="!")     # No hace salto de línea
print("Mundo")             # Salida: Hola!Mundo
print("1", "2", "3", sep="-")  # Salida: 1-2-3


## Entrada + Salida combinada
numero = int(input("Ingresa un número: "))
cuadrado = numero ** 2
print(f"El cuadrado de {numero} es {cuadrado}")


## Ejercicio práctico
nombre = input("¿Cómo te llamas? ")
año_nacimiento = int(input("¿En qué año naciste? "))
edad = 2025 - año_nacimiento
print(f"{nombre}, en 2025 tendrás {edad} años.")


## Entrada en una línea
## Puedes pedir varios datos en una sola línea, por ejemplo usando .split():
entrada = input("Ingresa nombre y edad separados por coma: ")
nombre, edad = entrada.split(",")
print(f"Nombre: {nombre} | Edad: {edad}")