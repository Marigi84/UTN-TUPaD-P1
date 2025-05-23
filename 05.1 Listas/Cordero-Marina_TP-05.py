#1) 
#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range.

lista_range = list(range(4,101,4))
print(lista_range)



#2) 

# Crear una lista con cinco elementos
favoritos = ["estrellas", "café", "código", "montañas", "música"]

# Mostrar el penúltimo elemento usando indexación negativa
penultimo = favoritos[-2]
print("El penúltimo elemento es:", penultimo)




#3) 
# Crear una lista vacía
mi_lista = []

# Agregar tres palabras con append
mi_lista.append("sol")
mi_lista.append("luna")
mi_lista.append("cielo")

# Imprimir la lista resultante
print("La lista resultante es:", mi_lista)











#4) 
# # Lista inicial
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo valor (índice 1) con "loro"
animales[1] = "loro"

# Reemplazar el último valor (índice -1) con "oso"
animales[-1] = "oso"

print("La lista resultante es:", animales)





#5) se utiliza el método remove() para eliminar el valor máximo de la lista, que se obtiene con max(numeros). El valor máximo es 22.



#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros.

numeros = list(range(10, 31, 5))
print(numeros[:2])



#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"] 

autos[1] = "palio"
autos[2] = "cronos"

print(autos)



#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)





#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

#a) Agregar "jugo" a la lista del tercer cliente usando append. 
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1] = "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.  
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla 
print(compras)





#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 

#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Imprimir la lista resultante por pantalla.
print(lista_anidada)