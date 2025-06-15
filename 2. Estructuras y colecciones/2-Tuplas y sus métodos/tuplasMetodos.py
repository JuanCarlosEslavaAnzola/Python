# Tuplas y sus métodos en Python: 
## Una tupla es una colección ordenada, inmutable (no editable) y permite duplicados.
## Se escribe entre paréntesis ():
coordenadas = (4, 7)
colores = ("rojo", "verde", "azul")

print(coordenadas)
print(colores)

## Diferencias principales con listas
###     Lista                       -->            	Tupla
###     Se usa con []               -->     		Se usa con ()
###     Es modificable              -->     		Es inmutable
###     Más pesada en memoria       -->     		Más liviana y rápida


## Acceder a elementos
##Como con listas:
frutas = ("manzana", "banana", "pera")
print(frutas[0])     # manzana
print(frutas[-1])    # pera


## No se puede modificar
## frutas[1] = "uva"  # Error: 'tuple' object does not support item assignment


## Métodos disponibles para tuplas
### Tuplas no tienen tantos métodos como las listas, pero sí los más básicos:

###     Método	    Descripción	                                                Ejemplo
###     count(x)	Cuenta cuántas veces aparece un valor	                    mi_tupla.count("rojo")
###     index(x)	Devuelve la posición del primer elemento igual a x	        mi_tupla.index("azul")


## Ejemplo completo:
colores = ("rojo", "verde", "azul", "rojo")

print(colores.count("rojo"))   # 2
print(colores.index("verde"))  # 1

for color in colores:
    print(f"Color: {color}")

### ¿Por qué usar tuplas?
### - Para proteger datos que no deben cambiar (ej. coordenadas, fechas).
### - Más eficientes en rendimiento que las listas.
### - Pueden usarse como claves en diccionarios.


## Conversión entre lista y tupla
lista = [1, 2, 3]
print (lista) # imprime lista

tupla = tuple(lista)  # convierte a tupla
print (tupla) # imprime tupla

nueva_lista = list(tupla)  # convierte a lista para poder modificar
print (nueva_lista) # imprime tupla a lista para 


## Ejercicio 1: crear y acceder
## Crea una tupla llamada dias con los días de la semana.        
## Imprime el primer y último día.
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

print("Primer día:", dias[0])
print("Último día:", dias[-1])


## Ejercicio 2: contar elementos repetidos
colores = ("rojo", "azul", "rojo", "verde", "rojo", "azul")

print("Rojo aparece:", colores.count("rojo"))       # 3
print("Azul aparece:", colores.count("azul"))       # 2


## Ejercicio 3: encontrar posición de un elemento
animales = ("perro", "gato", "loro", "pez")

print("El gato está en la posición:", animales.index("gato"))  # 1


## Ejercicio 4: recorrer la tupla con for
coordenadas = (10, 20, 30)

for valor in coordenadas:
    print(f"Valor: {valor}")


## Ejercicio 5: tuplas dentro de listas
## Crea una lista de tuplas, donde cada tupla representa un alumno con su nombre y nota.
## Imprime solo los alumnos que sacaron más de 70.
alumnos = [("Ana", 85), ("Luis", 65), ("Marta", 90), ("Pedro", 70)]

for nombre, nota in alumnos:
    if nota > 70:
        print(f"{nombre} aprobó con {nota}")


## Reto final: tupla de temperaturas
## - Crea una tupla con las temperaturas de 7 días.
## - Calcula la temperatura promedio.
## - Cuenta cuántos días fueron mayores de 30°C.
temperaturas = (28, 32, 30, 35, 29, 31, 27)

promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.2f}°C")

dias_calor = 0
for temp in temperaturas:
    if temp > 30:
        dias_calor += 1

print(f"Días con más de 30°C: {dias_calor}")