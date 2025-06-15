# Condicionales if, else y elif

## ¿Qué es una condicional? 
## Es una estructura que permite ejecutar una parte del código solo si se cumple una condición.

# Sintaxis básica:
##  if condición:
        ## código si la condición es verdadera
#3   else:
        ## código si la condición es falsa

edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")



# elif: Múltiples condiciones 
## elif significa "else if", sirve para evaluar más de una condición.

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bien hecho")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")


# Operadores de comparación:

##  Operador    Significado             Ejemplo
##  ==          Igual a                 x == 5
##  !=          Distinto de             x != 3
##  <           Menor que               x < 10
##  >           Mayor que               x > 2
##  <=          Menor o igual que       x <= 8
##  >=          Mayor o igual que       x >= 1


# Operadores lógicos
##  Operador        Significado	            Ejemplo
##  and             Y (ambas ciertas)	    edad > 18 and tiene_dni
##  or	            O (una u otra)	        es_admin or es_editor
##  not	            No (niega)	            not esta_lleno


# Ejemplo práctico:
usuario = input("Ingresa tu usuario: ")
clave = input("Ingresa tu clave: ")

if usuario == "admin" and clave == "1234":
    print("Bienvenido al sistema.")
else:
    print("Usuario o clave incorrectos.")


# Ejercicio
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puede entrar al cine.")
elif edad >= 13 and edad < 18:
    print("Puede entrar al cine en compañía de un adulto.")
else:
    print("No puede entrar al cine porque es menor de 13 años.")

