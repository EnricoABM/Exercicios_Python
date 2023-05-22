'''
Dada a lista abaixo:
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Exibir as seguintes listas, derivadas da lista acima.
a) Intervalo de 1 a 9
b) Intervalo de 8 a 13
c) Números pares
d) Números ímpares
e) Todos os múltiplos de 2, 3 e 4
f) Lista reversa
g) Soma do intervalo de 10 a 15
h) Uma lista com um novo elemento
i) Substituir o elemento com índice 6
'''

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#a)
print("a",lista[1:10])
#b)
print("b",lista[8:14])
#c)
print("c",lista[2:16:2])
#d)
print("d",lista[1:16:2])
#e)
print("e",lista[2:16:2])
print("e",lista[3:16:3])
print("e",lista[4:16:4])
#f)
listaRev = lista[:]
listaRev.reverse()
print("f",listaRev)
#g)
print("g",sum(lista[10:16]))
#h)
lista.append(16)
print("h",lista)
#i)
lista[6] = -6
print("i",lista)