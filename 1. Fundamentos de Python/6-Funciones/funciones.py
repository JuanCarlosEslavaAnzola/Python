# Funciones en Python (def)

## Una función es un bloque de código que:
## - Tiene un nombre
## - Puede recibir valores de entrada (parámetros)
## - Puede devolver un resultado
## - Se puede reutilizar las veces que quieras

## Sintaxis básica:
##  def nombre_funcion():
    # código de la función

## Ejemplo:
def saludar():
    print("¡Hola, te saludo desde una función!")

saludar()

## Funciones con parámetros
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Luis")
saludar("Ana")


## Funciones con retorno (return)
def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(5, 3)
print(f"La suma es: {suma}")


## Ejemplo práctico
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

print(calcular_area_rectangulo(4, 5))  # Resultado: 20


## Ejercicio
def verificar_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

verificacion = verificar_edad(int(input("Ingrese su edad: ")))
print(verificacion)


## Práctica: Funciones + Listas + Bucles
### Ejercicio 1: sumar todos los elementos de una lista
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = [3, 7, 1, 9]
resultado = sumar_lista(numeros)
print(f"La suma es: {resultado}")


### Ejercicio 2: contar cuántos números son mayores que un valor dado
def contar_mayores(lista, limite):
    contador = 0
    for numero in lista:
        if numero > limite:
            contador += 1
    return contador

numeros = [5, 12, 3, 20, 8]
print(contar_mayores(numeros, 10))  # Resultado: 2


### Ejercicio 3: devolver una lista con los cuadrados de otra
def cuadrados(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero ** 2)
    return nueva_lista

print(cuadrados([2, 3, 4]))  # Resultado: [4, 9, 16]


### Ejercicio 4: verificar si un elemento está en la lista
def esta_en_lista(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return True
    return False

nombres = ["Ana", "Luis", "Carlos"]
print(esta_en_lista(nombres, "Luis"))   # True
print(esta_en_lista(nombres, "Marta"))  # False


### Ejercicio 5: Cuente cuantas personas son matores de edad de una lista
def contar_mayores_de_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

lista_edades = [12, 20, 17, 25, 16, 18]
print(f"Mayores de edad: {contar_mayores_de_edad(lista_edades)}")  # Resultado: 3
