'''
Desenvolva um algoritmo que escreve em disco um
arquivo com números ordenados crescentemente de
1 a 100. Cada número deve ser separado por “;”. O
arquivo deve se chamar “crescente.txt”.
'''

arquivo = open("crescente.txt","w")
lista = [str(n) + ";" for n in range(1,101)]
arquivo.writelines(lista)
arquivo.close()