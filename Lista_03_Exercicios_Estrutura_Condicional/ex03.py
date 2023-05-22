#Elaborar um programa que deve receber um número qualquer e exibir se é par ou ímpar.

#Entradas: n;
#Saídas: par_impar;

print("Programa para comparar se um número é ímpar ou par")
n = int(input("Digite um número:"))

par_impar = n%2

if (par_impar != 0):
    print("O número {} é ímpar".format(n))
else:
    print("O número {} é par".format(n))