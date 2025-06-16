# Comprensión de listas en Python
## Es una técnica elegante, concisa y poderosa para crear listas a partir de otras listas o iterables, 
## todo en una sola línea.

# Es una forma compacta de construir listas usando una expresión seguida de un bucle for, e incluso con condiciones opcionales.
## Sintaxis básica:
## nueva_lista = [expresión for elemento in iterable]
## Es lo mismo que escribir un for normal, pero todo en una sola línea.

# Ejemplo básico: elevar al cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]


# Con condición (if)
pares = [x for x in range(100) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8...]
## Solo incluye los elementos que cumplen la condición.


# Con if/else en la expresión
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(clasificacion)  # ['par', 'impar', 'par', 'impar', 'par']
## Aquí el if está dentro de la expresión, no al final.


# Ejemplos prácticos
## Convertir a mayúsculas
palabras = ["hola", "mundo", "python"]
mayusculas = [p.upper() for p in palabras]
print(mayusculas)


# Filtrar palabras largas
palabras = ["sol", "computadora", "ratón", "teclado"]
largas = [p for p in palabras if len(p) > 5]
print(largas)


# Dobles de números impares
dobles = [x * 2 for x in range(10) if x % 2 != 0]
print(dobles)

# Lista de pares ordenados (tuplas)
pares = [(x, y) for x in range(3) for y in range(3)]
print(pares) # Resultado: [(0,0), (0,1), (0,2), (1,0), ..., (2,2)]

## 🔥 Ventajas
## ✅ Código más corto y legible
## ✅ Muy eficiente
## ✅ Útil con filtros, transformaciones y combinaciones

## ⚠️ Cuándo no usarlo
## ❌ Si la lógica es muy compleja
## ❌ Si necesitas varias líneas o muchas condiciones anidadas
## → Mejor usar un for tradicional para mantener claridad