'''
Elaborar um programa que leia uma lista com 4 números reais, em seguida o programa deve 
exibir as notas e a média.
'''
l1 = []
for x in range(0,4):
	l1.append(float(input("Digite um número: ")))
print("Notas:",l1)
print("Média:",sum(l1)/4)
	