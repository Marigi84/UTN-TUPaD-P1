#1 Pedir al usuario que ingrese el ancho y el alto de un rectángulo. 
# Calcular el área usando la fórmula: ancho * alto. 
# Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2). 
# Mostrar ambos resultados en pantalla

ancho = float(input("Ingrese el ancho del rectángulo: "))
alto = float(input("Ingrese el alto del rectángulo: "))

area = ancho * alto
perimetro = (ancho * 2) + (alto * 2)

print(f"El perímetro del rectángulo es: {perimetro} y el área es: {area}")



#2.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))# Solicitar al usuario una temperatura en grados Celsius. 

fahrenheit = (celsius * 9/5) + 32# Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.

print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")# Mostrar el resultado en pantalla.



#3
#1. Declarar dos variables booleanas: a = True, b = False. 
a = True  
b = False

#2. Realizar e imprimir los resultados
print(f"resultado de a or b:",{a and b})
print(f"resultado de not a:",{not a})
print(f"resultado de not b:",{not b})
print(f"resultado de a and b:",{a or b})


# Ejercicio 4
#           	a	                                b	                                c	
#	<<Variable no definida (A).>>	    <<Variable no definida (B).>>	    <<Variable no definida (C).>>	
#	<<Variable no definida (A).>>	    <<Variable no definida (B).>>	    <<Variable no definida (C).>>	
#	<<Variable no inicializada (A).>>	<<Variable no inicializada (B).>>	<<Variable no inicializada (C).>>	
#	            5                   	<<Variable no inicializada (B).>>	<<Variable no inicializada (C).>>	
#	            5                               	3	                    <<Variable no inicializada (C).>>	
#	            5                               	3                               	8	
#	            2                               	3                               	8	
#           	2                               	3                               	8	

#El valor de c se calcula como la suma de a (5) y b (3), resultando en 8.
#  La posterior reasignación de a a 2 no afecta el valor de c.ya contiene el resultado de la suma realizada previamente.


#Ejercicio 5

# Pedir número al usuario
numero = float(input("Ingrese un número: "))

# Calcular el cuadrado
cuadrado = numero * numero

# Mostrar resultado
print(f"El cuadrado de {numero} es: {cuadrado}")




#Ejercicio 6 

# Declarar variables
x = 10
y = 20

# Mostrar valores antes del intercambio
print(f"Antes del intercambio: x = {x}, y = {y}")

# Intercambiar valores usando operaciones aritméticas
x = x + y  # x = 10 + 20 = 30
y = x - y  # y = 30 - 20 = 10
x = x - y  # x = 30 - 10 = 20

# Mostrar valores después del intercambio
print(f"Después del intercambio: x = {x}, y = {y}")


# Ejercicio 7

# Solicitar peso y altura al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"Tu IMC es: {imc:.1f}")



# Ejercicio 8

# 2. Calcular y mostrar
# a) Cantidad total de letras (sin contar espacios)
total_letras = len(nombre.replace(" ", ""))
print(f"Cantidad total de letras: {total_letras}")

# b) Primeras 3 letras del nombre
primeras_tres = nombre[:3]
print(f"Primeras 3 letras: {primeras_tres}")

# c) Nombre con letras mayúsculas y minúsculas alternadas
resultado = ""
for i in range(len(nombre)):
    if i % 2 == 0:
        resultado += nombre[i].upper()
    else:
        resultado += nombre[i].lower()
print(f"Nombre alternado: {resultado}")


#Ejercicio 9

# 1. Declarar variables
a = 7.5
b = 3.2

# 2. Calcular y mostrar
# a) Suma
suma = a + b
print(f"Suma (a + b): {suma}")

# b) Redondeo de la división a 2 decimales
division = round(a / b, 2)
print(f"División redondeada (a / b): {division}")

# c) Potencia
potencia = a ** b
print(f"Potencia (a ** b): {potencia}")



#Ejercicio 10
# 1. Pedir el precio original
precio_original = float(input("Ingrese el precio original del producto: "))

# 2. Pedir el porcentaje de descuento
descuento = float(input("Ingrese el porcentaje de descuento: "))

# 3. Calcular el precio final
precio_final = precio_original - (precio_original * (descuento / 100))
#precio_final = precio_original 

# 4. Mostrar el precio con descuento
print(f"El precio final con descuento es: ${precio_final:.2f}")
