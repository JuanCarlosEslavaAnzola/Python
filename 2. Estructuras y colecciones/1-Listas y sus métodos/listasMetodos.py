# Listas y sus métodos en Python: 
# Una lista es una colección ordenada y modificable de elementos.

## Ejemplos
frutas = ["manzana", "banana", "naranja"]
numeros = [5, 10, 15]
mixta = [True, "hola", 3.14]

print(frutas)
print(numeros)
print(mixta)


## Acceder a elementos de una lista
print(frutas[0])  # "manzana"
print(frutas[-1]) # "naranja" (último elemento)


## Modificar elementos
frutas[1] = "pera"
print(frutas)  # ["manzana", "pera", "naranja"]


## Métodos útiles de listas
###  Método	            Descripción	                                        Ejemplo
###  append(x)	        Agrega un elemento al final	                        lista.append("nuevo")
###  insert(i, x)	    Inserta en una posición específica	                lista.insert(1, "medio")
###  remove(x)	        Elimina el primer valor x	                        lista.remove("banana")
###  pop(i)	            Elimina y devuelve el elemento en posición i	    lista.pop(2)
###  sort()	            Ordena la lista (números o letras)	                lista.sort()
###  reverse()	        Invierte el orden de la lista	                    lista.reverse()
###  len(lista)	        Devuelve la cantidad de elementos	                len(lista)


## Ejemplos prácticos:
nombres = ["Ana", "Luis", "Carlos"]

nombres.append("Marta")
print(nombres)  # ["Ana", "Luis", "Carlos", "Marta"]

nombres.remove("Luis")
print(nombres)  # ["Ana", "Carlos", "Marta"]

print(len(nombres))  # 3


## Recorrer listas con for
for fruta in frutas:
    print(f"Me gusta la {fruta}")


## Ejercicio
### Crea una lista vacía llamada numeros. Luego:
numeros = []

### Usa append() para agregar 3 números.
numeros.append(25)
numeros.append(11)
numeros.append(26)

### Usa un bucle para imprimir el doble de cada número.
for numero in numeros:
    dobleNum = numero * 2
    print(f"El doble del numero {numero} es {dobleNum}.")


### Ordena la lista de mayor a menor (sort(reverse=True))
numeros.sort(reverse=True)
print(numeros)