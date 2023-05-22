'''
3) Elaborar um programa que deve ler N números. 
Caso o usuário digite zero (0), o programa deve exibir a somatória e a média dos valores inseridos.

'''

num = float(input("Digite um número: "))
l1 = []

while(num != 0):
    l1.append(num)
    num = float(input("Digite um número: "))

print("A soma dos números digitados é: ", sum(l1))
print("A média dos valores inseridos é:", sum(l1)/len(l1))


