# Archivos .txt (open())en Python
# Cómo abrir, leer y escribir archivos usando open()

# open() — Abrir un archivo
## archivo = open("datos.txt", "r")

##  Modo        Significado
##  'r'	        Leer (read)
##  'w'	        Escribir (write) — ¡borra el archivo si existe!
##  'a'	        Añadir (append) al final del archivo
##  'r+'	    Leer y escribir
##  'w+'	    Escribir y leer (borra contenido)

# Leer archivos .txt
# Supongamos que tienes un archivo llamado "datos.txt"

archivo = open("2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\datos.txt", "r")        # Abrir en modo lectura
contenido = archivo.read()              # Leer todo el contenido
print(contenido)
archivo.close()                         # ¡No olvides cerrarlo!

## También puedes leer línea por línea:
archivo = open("2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\datos.txt", "r")
for linea in archivo:
    print(linea.strip())  # .strip() quita los saltos de línea
archivo.close()


#Escribir en archivos .txt
# Sobrescribir contenido ('w')
archivo = open("2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\nuevo.txt", "w")
archivo.write("Hola, mundo\n")
archivo.write("Segunda linea\n")
archivo.close()
# Si nuevo.txt ya existía, su contenido anterior se borra.

# Añadir contenido ('a')
archivo = open("2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\nuevo.txt", "a")
archivo.write("Linea anadida al final\n")
archivo.close()

# Forma recomendada: with
with open("2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
## Ventajas:
# - No necesitas archivo.close(), se cierra automáticamente
# - Más limpio y seguro

# Ejercicio simple
## Crea un archivo llamado notas.txt con este contenido:
## - Juan: 4.5
## - Ana: 3.8
## - Carlos: 5.0
rutaBase = "2. Estructuras y colecciones\\9. Archivos .txt (open()) en Python\\"
with open(f"{rutaBase}notas.txt", "w") as archivo:
    archivo.write("Juan: 4.5\n")
    archivo.write("Ana: 3.8\n")    
    archivo.write("Carlos: 5.0\n")

# Y escribe un programa que:
## - Lea cada línea
## - Separe nombre y nota
## - Diga quién aprobó (nota >= 3.0)
listNotas = []
with open(f"{rutaBase}notas.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, nota_str = linea.split(": ")
        nota = float(nota_str)
        listNotas.append((nombre, nota))
    archivo.close()

for nombre, nota in listNotas:
    if nota >=3.0:
        print(f"{nombre} aprobó con {nota}")
