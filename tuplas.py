#las tuplas no se pueden modificar despues de su creacion
#las tuplas son inmutables, no se pueden modificar despues de su creacion

"""las listas se crean con corchetes [], las tuplas con parentesis ()"""

tupla = (1, 2, 3, 4, 5)
print("\033[32m Tupla:", tupla, "\033[0m")  # imprimir tupla

#operaciones de las tuplas
print("\033[33m Longitud de la tupla:", len(tupla), "\033[0m")  # longitud de la tupla

print("\033[34m Primer elemento de la tupla:", tupla[0], "\033[0m")  # convertir tupla a lista

print("\033[35m Ultimo elemento de la tupla:", tupla[-1], "\033[0m")  # ultimo elemento de la tupla

#buscar un elemento en la tupla
print("\033[36m Buscar elemento 3 en la tupla:", 3 in tupla, "\033[0m")  # buscar un elemento en la tupla

#otra forma usando index
print("\033[37m Buscar elemento 3 en la tupla con index:", tupla.index(3), "\033[0m") # buscar un elemento en la tupla con index

