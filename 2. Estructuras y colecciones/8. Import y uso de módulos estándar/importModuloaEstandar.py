# import y uso de módulos estándar en Python
## Un módulo es un archivo de Python con funciones, clases o variables que puedes reutilizar en otros programas.
## Python incluye muchos módulos llamados módulos estándar (ya vienen instalados).

# Usar import
# Hay tres formas comunes de importar un módulo:
# import math           # Importa todo el módulo
# from math import pi   # Importa solo una parte
# import math as m      # Le das un alias

# Módulo math — Matemáticas avanzadas
import math

print(math.sqrt(25))        # Raíz cuadrada → 5.0
print(math.pow(2, 3))       # Potencia → 8.0
print(math.factorial(5))    # Factorial → 120
print(math.pi)              # Valor de PI → 3.1415...
print(math.sin(math.pi/2)) # Seno → 1.0
# Ideal para cálculos científicos, trigonometría, logaritmos, etc.


# Módulo random — Valores aleatorios
import random

print(random.random())          # Número aleatorio entre 0 y 1
print(random.randint(1, 10))    # Entero entre 1 y 10
print(random.choice(["A", "B", "C"]))  # Elemento aleatorio de una lista
print(random.sample(range(1, 50), 6))  # 6 valores únicos de una lista
print(random.shuffle([1, 2, 3, 4]))    # Mezcla una lista (in-place)
# Útil para juegos, simulaciones, sorteos, etc.

# Módulo datetime — Fechas y horas
import datetime

hoy = datetime.date.today()
print(hoy)                     # Fecha actual: 2025-06-14

ahora = datetime.datetime.now()
print(ahora)                   # Fecha y hora: 2025-06-14 12:34:56.789

cumple = datetime.date(1990, 5, 17)
print(hoy - cumple)            # Diferencia de fechas (días)

#También puedes formatear fechas:
print(ahora.strftime("%d/%m/%Y"))  # 14/06/2025
print(ahora.strftime("%H:%M:%S"))  # 12:34:56


# Resumen
# Módulo	    ¿Para qué sirve?	                Ejemplo clave
# math	        Funciones matemáticas avanzadas	    math.sqrt(9)
# random	    Generar números aleatorios	        random.randint(1, 100)
# datetime	    Fechas y tiempos	                datetime.date.today()