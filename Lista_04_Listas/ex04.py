'''
Elaborar um programa que leia uma lista que contenha 20 números inteiros e em seguida o 
programa deve exibir o maior e o menor número.
'''
l1 = []
for x in range(0,20):
	l1.append(int(input("Digite um número qualquer: ")))
print("O maior valor da sequência é: ",max(l1))
print("O menor valor da sequência é: ", min(l1))