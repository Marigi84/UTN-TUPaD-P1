#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for numero in range(101):
    print(numero)




#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.


# Se inicia un bucle infinito, hasta que el usuario ingrese un número entero válido.
while True:
    # Se solicita al usuario que ingrese un valor y se almacena en la variable 'entrada'.
    entrada = input("Ingrese un número entero: ")
    # Se intenta convertir la entrada del usuario a un número entero.
    try:
        numero_usuario = int(entrada)
        # Si la conversión es exitosa, se sale del bucle 'while' utilizando la sentencia 'break'.
        break
    # Si la conversión falla, se genera una excepción de tipo ValueError. El bucle 'while' continuará.
    except ValueError:
        
        print("La entrada no es un número entero válido. Intente nuevamente.")

# Una vez que el usuario ha ingresado un número entero válido, se procede a contar la cantidad de dígitos.

# Se verifica si el número ingresado es 0.
if numero_usuario == 0:
    # El número 0 tiene un solo dígito (se crea variable cantidad_digitos).
    cantidad_digitos = 1
# Si el número no es 0, se procede con el siguiente bloque.
else:
    # Se inicializa la variable 'cantidad_digitos' en 0.
    cantidad_digitos = 0

    # Se obtiene el valor absoluto del número ingresado.
    numero_abs = abs(numero_usuario)

    # Se inicia un bucle 'while' que continuará mientras el valor absoluto del número sea mayor que 0.
    while numero_abs > 0:
        # Se realiza una división entera del 'numero_abs' por 10. Con '//' en cada iteración, esto elimina el último dígito del número.
        numero_abs //= 10
        # Se incrementa el contador de dígitos en 1 por cada dígito eliminado.
        cantidad_digitos += 1

# Finalmente, se muestra en la pantalla el número ingresado por el usuario y la cantidad de dígitos que contiene.
print(f"El número '{numero_usuario}' tiene {cantidad_digitos} dígitos.")



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Para asegurarnos que el usuario ingrese un número entero, se inicia un bucle 'while' que se ejecutará indefinidamente hasta que se cumpla una condición.
while True:
    # El bloque 'try'intentará convertir el ingreso del usuario a un número entero, sino generarará una excepción (error).
    try:
        # Se solicita al usuario que ingrese un texto, almacenandolo en la variable 'inicio_str'
        inicio_str = input("Ingrese el primer número entero: ")
        # Se intenta convertir la cadena de texto ingresada por el usuario a un número entero. Si la conversión es exitosa, en la variable 'inicio'.
        inicio = int(inicio_str)
        # Si la conversión fue exitosa, la sentencia 'break' que causa la salida inmediata del bucle 'while' actual.
        break
    # El bloque 'except ValueError' se ejecuta si ocurre una excepción de tipo 'ValueError' dentro del bloque 'try'.
    #cuando por ejemplo, el usuario ingresa letras en lugar de números).
    except ValueError:
        # Si ocurre un 'ValueError', se muestra un mensaje informativo al usuario y se le pide que intente nuevamente.
        print("La entrada no es un número entero válido. Intente nuevamente.")
        # Después, el bucle 'while True' continúa su siguiente iteración,
       

# Solicitar al usuario el segundo valor entero
# Este es otro bucle 'while True', idéntico en su estructura al anterior, pero diseñado para obtener el segundo número entero.
while True:
    try:
        fin_str = input("Ingrese el segundo número entero: ")
       
        fin = int(fin_str)
       
        break
    except ValueError:
        
        print("La entrada no es un número entero válido. Intente nuevamente.")

# Asegurarse de que 'inicio' sea menor que 'fin'

if inicio > fin:
    # Si 'inicio' es mayor que 'fin', esta línea realiza una asignación múltiple para intercambiar los valores de las dos variables.
    # El valor de 'fin' se asigna a 'inicio', y el valor de 'inicio' se asigna a 'fin' simultáneamente.
    
        inicio, fin = fin, inicio

# Inicializar la variable para almacenar la suma

suma = 0

# Iterar a través de los números enteros comprendidos entre 'inicio' y 'fin', excluyendo los valores de 'inicio' y 'fin'
# Se inicia un bucle 'for' que itera sobre una secuencia de números. 'inicio + 1' genera que el rango comience desde el valor siguiente a 'inicio' 
# y terminan justo antes del valor de 'fin'. Esto asegura que los valores límite ('inicio' y 'fin') no se incluyan en la suma.
for numero in range(inicio + 1, fin):
    # En cada iteración del bucle, la variable 'numero' toma el valor del siguiente entero en la secuencia generada por 'range()'.
    # en la variable 'suma', se va sumando el valor adoptado por 'numero'.
    suma += numero

print(f"La suma de los números enteros entre {inicio} y {fin} (excluyéndolos) es: {suma}")
# Finalmente, la cadena de texto formateada se muestra en la consola, proporcionando al usuario el resultado de la suma.

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


# Inicializa la variable total en 0 para acumular la suma de los números
total = 0

# Inicia un bucle infinito que se romperá cuando se cumpla una condición
while True:
    # Solicita al usuario un número entero y lo convierte a int
    numero = int(input("Ingrese un número entero (0 para terminar): "))

    # Verifica si el número ingresado es 0
    if numero == 0:
        # Si es 0, rompe el bucle
        break
    
    # Suma el número ingresado al total acumulado
    total += numero

# Muestra el total acumulado después de salir del bucle
print("El total acumulado es:", total)



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# importamos el módulo 'random' para generar números aleatorios.
import random

#generamos un numero secreto del 0 al 9 y lo guardamos en la variable 'numero_secreto'.
numero_secreto = random.randint(0,9)
intentos = 0 #inicializamos el contador de intentos en 0

print("Adivina el número secreto entre 0 y 9") #imprimimos un mensaje de bienvenida

while True:#Iniciamos el bucle infinito
    intento = int(input("Ingresa tu intento: "))#solicitamos al usuario que realice un intento y lo guardamos en la variable
    intentos +=1 #incrementamos el contador en 1

    if intento == numero_secreto: #verificamos si el numero ingresado es igual al numero secreto.
        print(f"Feliciataciones! Adivinaste el numero secreto en {intentos} intentos. ") #si es igual imprimimos mensaje de felicitaciones.
    elif intento < numero_secreto: #continua el programa pidiendo mas intentos.
        print("El número es mayor")
    else:
        print("El número es menor")


#6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

# Utilizamos un ciclo for que comienza en 100 y termina antes de -1(0).
# Decrementa en 2 en cada paso esto asegura que la secuencia generada contenga solo los números pares
    for numero in range(100, -1, -2):
  # En cada iteración, el valor actual de la secuencia se asigna a la variable 'numero'.
  # con la función print() mostramos el valor de la variable 'numero' en cada iteración.
  
        print(numero)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Pedir al usuario que ingrese un número entero positivo
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero positivo.")

# Inicializar la variable para almacenar la suma
    suma = 0

# Iterar a través de los números enteros desde 0 hasta 'numero'
    for i in range(numero + 1):
        suma += i

# Mostrar el resultado
    print(f"La suma de los números enteros desde 0 hasta {numero} es: {suma}")



    #8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    #programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    #negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
    #menor, pero debe estar preparado para procesar 100 números con un solo cambio).

    # Inicializar contadores para cada tipo de número
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0 

    # Iterar 
    for _ in range(100):
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
                
            if numero > 0:
                positivos += 1
            else:
                negativos += 1
        except ValueError:
            print("Entrada inválida. Ingrese un número entero válido.")

    # Mostrar resultados    
    print("\n--- Resultados ---")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Cantidad de números positivos: {positivos}")
    print(f"Cantidad de números negativos: {negativos}")



        #9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    #media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
    #poder procesar 100 números cambiando solo un valor).

    suma = 0 # Inicializa la variable para almacenar la suma de los números.
    contador = 0 # Inicializa la variable para contar cuántos números se ingresan.

    print("Ingrese 100 números enteros:") # Informa al usuario sobre la entrada esperada.

    for i in range(100): # Inicia un bucle que se ejecutará 100 veces 
        try:
            numero = int(input(f"Ingrese el número {i + 1}: ")) # Solicita un número al usuario y lo intenta convertir a entero.
            suma += numero    # Suma el número ingresado a la variable 'suma'.
            contador += 1    # Incrementa el contador de números válidos ingresados.
        except ValueError:
            print("Entrada inválida. Ingrese un número entero válido.") # Maneja el error si la entrada no es un entero.

    if contador > 0: # Verifica si se ingresó al menos un número para evitar división por cero.
        media = suma / contador # Calcula la media dividiendo la suma total por la cantidad de números.
        print(f"La media de los {contador} números ingresados es: {media}") # Muestra la media calculada.



    #10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
    #usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

    numero_str = input("Ingrese un número entero: ") # Solicita al usuario que ingrese un número y lo guarda como cadena.
    numero_invertido_str = "" # Inicializa una cadena vacía para almacenar el número invertido.
    longitud = len(numero_str) # Obtiene la longitud de la cadena del número.

    for i in range(longitud): # Inicia un bucle que itera sobre cada dígito de la cadena original.
        caracter = numero_str[longitud - 1 - i] # Accede a los caracteres de la cadena original en orden inverso.
        numero_invertido_str += caracter # Concatena cada carácter (dígito) al final de la cadena invertida.

    print(f"El número invertido es: {numero_invertido_str}") # Muestra la cadena con los dígitos en orden inve
                

