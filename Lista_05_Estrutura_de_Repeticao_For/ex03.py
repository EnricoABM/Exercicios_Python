"""
3) Elaborar um programa que lê 20 números inteiros e para cada número inserido exibir se é par 
ou ímpar.
"""
for rep in range(0,20):
    num = int(input("Informe um número inteiro: "))
    if (num % 2 == 0):
        print("Este número é par")
    elif (num % 2 != 0):
        print("Este número é ímpar")