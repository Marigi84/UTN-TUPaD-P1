'''#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario''' 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingrese un número entero: "))

for i in range(1, numero+1):
    print(f"El factorial de {i} es {factorial(i)}")



'''#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

numero = int(input("Ingrese un número entero: "))

for i in range(0, numero+1):
    print(f"La posición {i} de la serie de Fibonacci es {fibonacci(i)}")


'''#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. '''

def potencia(n, m):
    # Caso base: cualquier número elevado a 0 es 1
    if m == 0:
        return 1
    else:
        # Paso recursivo
        return n * potencia(n, m - 1)

# Algoritmo general de prueba
def prueba_potencia():
    # Pedimos al usuario la base y el exponente
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    
    # Calculamos la potencia usando la función recursiva
    resultado = potencia(base, exponente)
    
    # Mostramos el resultado
    print(f"{base} elevado a la {exponente} es: {resultado}")

# Llamamos al algoritmo de prueba
prueba_potencia()


'''#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. '''

# Definimos una función llamada decimal_a_binario que convierte un número decimal a binario de forma recursiva
def decimal_a_binario(n):
    # Caso base: si n es 0, retorna una cadena vacía
    if n == 0:
        return ""
    else:
        # Llamada recursiva: divide n por 2 (división entera) y concatena el resto (n % 2) convertido a cadena
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitamos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validamos que el número ingresado sea positivo
if numero < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Si el número es válido, mostramos el número convertido a binario usando la función decimal_a_binario
    print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")


    

'''5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed().'''

def es_palindromo(palabra, inicio=0, fin=None):
    # Si es la primera llamada, inicializamos 'fin' con el último índice
    if fin is None:
        fin = len(palabra) - 1

    # Caso base: si ya cruzamos los índices, es palíndromo
    if inicio >= fin:
        return True

    # Si los caracteres no coinciden, no es palíndromo
    if palabra[inicio] != palabra[fin]:
        return False

    # Llamada recursiva, avanzando los índices hacia el centro
    return es_palindromo(palabra, inicio + 1, fin - 1)

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")


'''6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) '''

def suma_digitos(n):
    # Caso base: si el número es menor que 
    if n <= 1:
        return 1
    else:
        ultimo_digito = n % 10
        resto = n//10
        resultado = ultimo_digito + suma_digitos(resto)
        return resultado

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")



'''Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)'''

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

numero = int(input("Ingrese un número entero positivo: "))




'''8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4
contar_digito(123456, 7)     → 0  '''

def contar_digito(numero, digito):
    # Caso base: si el número ya es 0, no hay más dígitos
    if numero == 0:
        return 0
    else:
        # Obtenemos el último dígito
        ultimo_digito = numero % 10
        
        # Comparamos si es igual al dígito buscado
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

