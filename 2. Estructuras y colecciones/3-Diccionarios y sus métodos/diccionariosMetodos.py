# Diccionarios y sus métodos en Python: 
# Un diccionario es una colección desordenada, mutable y que almacena datos en pares clave:valor.
persona = {
    "nombre": "Luis",
    "edad": 30,
    "ciudad": "Bogotá"
    #3"correo": "correo@correo.com"
}

## "nombre" es una clave
## "Luis" es el valor asociado a esa clave


## Acceder a valores
print(persona["nombre"])   # Luis
print(persona["edad"])     # 30


##También puedes usar .get() para evitar errores si la clave no existe:
print(persona.get("correo"))  # None


## Modificar o agregar elementos
persona["edad"] = 31            # Modifica
persona["correo"] = "a@b.com"   # Agrega

print(persona)


## Eliminar elementos
del persona["ciudad"]     # Elimina la clave "ciudad"

edad = persona.pop("edad")       # Elimina y devuelve el valor de "edad"
print(edad)

print(persona)


## Métodos útiles de los diccionarios
###     Método	        Descripción
###     keys()	        Devuelve todas las claves
###     values()	    Devuelve todos los valores
###     items()	        Devuelve lista de tuplas (clave, valor)
###     get(clave)	    Devuelve el valor de una clave
###     pop(clave)	    Elimina la clave y devuelve su valor
###     clear()	        Elimina todo el contenido del diccionario
###     update(dic2)	Actualiza un diccionario con otro



## Recorrer un diccionario
for clave in persona:
    print(clave, ":", persona[clave])

##3 O así:
for clave, valor in persona.items():
    print(f"{clave} => {valor}")



## Ejemplo completo:
estudiante = {
    "nombre": "Marta",
    "edad": 22,
    "cursos": ["Python", "SQL"]
}

print(estudiante["cursos"][0])      # Python
estudiante["cursos"].append("HTML") # Agrega curso
print(estudiante)



## ¿Cuándo usar diccionarios?
## - Cuando necesitas acceso rápido a datos por nombre/clave.
## - Para representar objetos del mundo real (usuarios, productos, configuraciones).
## - Cuando no importa el orden, pero sí la relación entre clave y valor.


### Ejercicios con Diccionarios en Python

## Ejercicio 1: Crear y acceder
persona = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Lima"
}

print(persona["nombre"])  # Juan
print(persona.get("correo", "No hay correo"))  # No hay correo


## Ejercicio 2: Agregar y modificar datos
persona["edad"] = 29
persona["correo"] = "juan@gmail.com"

print(persona)


## Ejercicio 3: Eliminar claves
persona.pop("ciudad")
del persona["correo"]

print(persona)

      
## Ejercicio 4: Recorrer un diccionario
for clave in persona:
    print(clave, ":", persona[clave])

# o también
for clave, valor in persona.items():
    print(f"{clave} => {valor}")



## Ejercicio 5: Diccionario de listas
estudiante = {
    "nombre": "Ana",
    "cursos": ["Python", "HTML", "CSS"]
}

print(estudiante["cursos"][1])  # HTML

for curso in estudiante["cursos"]:
    print("Está inscrita en:", curso)


## Ejercicio 6: Lista de diccionarios
alumnos = [
    {"nombre": "Carlos", "nota": 85},
    {"nombre": "María", "nota": 92},
    {"nombre": "Lucía", "nota": 78}
]

for alumno in alumnos:
    if alumno["nota"] >= 80:
        print(f"{alumno['nombre']} aprobó con {alumno['nota']}")



### Reto: Registro de productos
## - Crea un diccionario llamado producto.
## - Guarda: nombre, precio, stock.
## - Calcula el valor total del inventario (precio * stock).
producto = {
    "nombre": "Camiseta",
    "precio": 20,
    "stock": 15
}

total = producto["precio"] * producto["stock"]
print(f"Inventario total: ${total}")