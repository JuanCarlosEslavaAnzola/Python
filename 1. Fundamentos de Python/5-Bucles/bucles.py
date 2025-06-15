# Bucles for y while en Python

## Un bucle permite repetir un bloque de código varias veces, ya sea:
### Un número fijo de veces (for)
### Mientras se cumpla una condición (while)

## for: Bucle controlado
### Sintaxis:
### for variable in secuencia:
    # código a repetir

## Ejemplo con range():
for i in range(5):
    print(i)

## Ejemplo: contar hasta 10
for numero in range(1, 11):
    print(f"Voy por el número {numero}")



## while: Bucle condicional
### Sintaxis:
### while condición:
    # código a repetir

##  Ejemplo:
contador = 1
while contador <= 5:
    print(f"Vuelta {contador}")
    contador += 1  # suma 1 en cada vuelta

## Cuidado con bucles infinitos
## while True:
##    print("Esto nunca termina")
## Esto se repite para siempre... ¡ten cuidado con la condición!

# Ejercicio (con for):
for i in range(1, 31):
    if i % 3 == 0:
        print(i)


# Ejercicio (con while):
numero = -1

while numero != 0:
    numero = int(input("Ingresa un número (0 para salir): "))
    print(f"Ingresaste: {numero}")


# break y continue
## break: termina el bucle      
## continue: salta a la siguiente vuelta

for i in range(10):
    if i == 5:
        break
    elif i == 3:
        continue
    print(i)