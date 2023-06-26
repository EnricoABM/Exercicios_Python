'''
Desenvolva um algoritmo que escreve em disco um
arquivo com números ordenados decrescentemente
de 100 a 1. Cada número deve estar em uma linha.
O arquivo deve se chamar “decrescente.txt”.
'''
arquivo = open("decrescente.txt","w")
lista = []
for n in range(100,0,-1):
    lista.append(str(n))
arquivo.writelines(lista)
arquivo.close()