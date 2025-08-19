listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listas)

listas_vacia = []

listas_vacia.append("Hola")
print(listas_vacia)

listas_vacia.insert(1, "true")
print(listas_vacia)
print(listas_vacia[-1])

print(len(listas_vacia))

listas_vacia.remove(1)
listas_vacia.pop()
print(listas_vacia)

#listas_vacia [0] = "modificado"
#print(listas_vacia)

lista_de_listas = [1, 2, 3], [4, 5, 6], [7, 8, 9]
print(lista_de_listas)

print(listas_vacia[1][2])
import random

lista_aleatoria = random.sample(range(1, 100), 10)
print(lista_aleatoria)

import numpy as np
lista_numpy = np.random.randint(1, 100, size=10).tolist()
print(lista_numpy)

lista_numpy.sort() #ordenar la lista numpy
print(lista_numpy)

lista_numpy.reverse() #invertir la lista numpy
print(lista_numpy)

#buscar un elemento en la lista
print("\033[33m Buscar un elemento en la lista numpy:", 30 in lista_numpy, "\033[0m")

#buscar en la lista vacia 
print("\033[33m Buscar un elemento en la lista vacia:", 2 in listas_vacia, "\033[0m")

#buscar pero con index
print("\033[33m Buscar un elemento en la lista numpy:", listas_vacia.index(3), "\033[0m") #buscar un elemento enn la lista vacia con index

#contar cuantas veces aparece un elemento en la lista
print("\033[33m Contar elemento en la lista numpy:", lista_numpy.count(50), "\033[0m") #contar cuantas veces aparece un elemento en la lista numpy

#copiar una lista
lista_copiada = lista_numpy.copy()
print("\033[33m Copia de la lista numpy:", lista_copiada, "\033[0m") #copia de la lista numpy

#sumar dos listas 
listaCopia= lista_numpy[:]
print("\033[35m copia num:", listaCopia, "\033[0m")#sumar dos listas

#limpiar lista
lista_numpy.clear()
print("\033[32m Lista numpy despues de limpiar:", lista_numpy, "\033[0m") #limpiar lista numpy

#concatenar dos listas
lista_concatenada = lista_numpy + lista_copiada
print("\033[33m Lista concatenada:", lista_concatenada, "\033[0m") #concatenar dos listas

#sacar mayor valor de la lista
print("\033[34m Mayor valor de la lista copiada:", max(lista_copiada), "\033[0m") #sacar mayor valor de la lista numpy

#tamaño de la lista copiada
print("\033[34m Tamaño de la lista copiada:", len(lista_copiada), "\033[0m") #tamaño de la lista copiada
