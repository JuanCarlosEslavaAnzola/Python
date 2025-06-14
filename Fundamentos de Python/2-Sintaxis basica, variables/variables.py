# Una variable es como una “caja” donde guardas información. 
# No necesitas declarar el tipo, Python lo detecta automáticamente.

nombre = "Ana"        # cadena de texto || tipo -->  String
edad = 25             # número entero || tipo -->  Int
altura = 1.68         # número decimal (float) || tipo -->  Decimal
es_estudiante = True  # booleano (verdadero/falso) || tipo -->  True/False


# Mostrar variables (output)
x = 5
print (x)

nombre = "Luis"
print("Hola", nombre)

## También puedes usar f-strings para combinar texto y variables:
edad = 30
print(f"Tienes {edad} años")


# Entrada de datos (input)
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")

## Ojo: input() siempre devuelve texto (str), si necesitas un número debes convertirlo:
edad = int(input("¿Cuántos años tienes? "))
print(f"En 5 años tendrás {edad + 5}")


# Ejercicio
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

edad_en_2050 = 2050 - 2025 + edad

print(f"Hola {nombre}, en 2050 tendrás {edad_en_2050} años.")

