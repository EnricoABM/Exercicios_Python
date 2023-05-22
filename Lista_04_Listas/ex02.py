'''
Elaborar um programa que leia uma lista de 6 números inteiros e mostre cada número juntamente 
com a sua posição na lista
'''
l1 = []
for x in range(0,6):
	l1.append(int(input("Digite um número inteiro: ")))
for z in range (0,6):
	print(f"Índice {z + 1}, {l1[z]}")