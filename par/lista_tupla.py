lista = [0, 2, 1, 4, 3,5]
print(lista)
tupla = (5,4,3,2,1)
print(tupla)
print(lista[2])
print(tupla[3])
# o comando sort ordena as listas
lista.sort()
print(lista)
# o comando len da o tamanho da lista ou tupla
print(len(lista))
# os comandos abaixo passam uma lista para uma tupla e vice versa 
lista_numerica = list(tupla)
print (lista_numerica)
lista_tupla = tuple(lista)
print (lista_tupla)