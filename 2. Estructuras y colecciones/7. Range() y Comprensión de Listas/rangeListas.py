# range() y Comprensión de Listas
## Range: Es una función incorporada de Python que genera una secuencia de números enteros. 
## Muy útil para bucles y listas.

# Sintaxis de range():
# range(inicio, fin, paso)
# - inicio: el número donde comienza (opcional, por defecto es 0)
# - fin: hasta dónde va (sin incluir ese número)
# - paso: cuánto se incrementa (opcional, por defecto es 1)}

#Ejemplos:
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(2, 8)))     # [2, 3, 4, 5, 6, 7]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(10, 0, -2)))# [10, 8, 6, 4, 2]

# Se usa comúnmente en bucles:
for i in range(3):
    print("Hola", i)


# Comprensión de listas
# Una forma concisa de crear listas nuevas a partir de un iterable (como range() o una lista), con o sin condiciones. 

# Ejemplos con range():
# Números del 0 al 9
lista = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

# Cuadrados de los números
cuadrados = [x**2 for x in range(6)] # [0, 1, 4, 9, 16, 25]
print(cuadrados)

# Solo pares hasta el 10
pares = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
print(pares)

# Con if/else en la expresión par aindicar cuando es par y cuando es impar
etiquetas = ["par" if x % 2 == 0 else "impar" for x in range(5)] # ['par', 'impar', 'par', 'impar', 'par']
print(etiquetas)

# Combinando range() + comprensión
multiplicados = [x * 10 for x in range(1, 6)] # [10, 20, 30, 40, 50]
print(multiplicados)

# Ventajas de comprensión de listas
# - Más rápido que un bucle tradicional
# - Más limpio y legible (si no es muy complejo)

print("-------------")

## Ejercicios

# 1. Crear una lista con los múltiplos de 3 entre 1 y 30
multiplos_tres = list(range(3, 31, 3))
print("Múltiplos de 3 entre 1 y 30:", multiplos_tres)

multiplos_3 = [x for x in range(1, 31) if x % 3 == 0]
print(multiplos_3) # 👉 Resultado: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# 2. Crear una lista de los cuadrados de los números impares entre 1 y 20
cuadrados_impares = [x**2 for x in range(1, 20) if x % 2 != 0]
print("Cuadrados de números impares entre 1 y 20:", cuadrados_impares)

# 3. Crear una lista que diga "Aprobó" o "Reprobó" según una lista de calificaciones aleatorias
import random

lista_calificaciones = [random.randint(1, 10) for _ in range(10)]
print("Calificaciones:", lista_calificaciones)

resultado = ["Aprobó" if x >= 7 else "Reprobó" for x in lista_calificaciones]
print("Resultados:", resultado)
