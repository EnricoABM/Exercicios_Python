'''
8) Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida
pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o
número 1 a repetição termina. Exibir no final todos os elementos da lista.

'''

ListaN = []
num = int(input("Digite um número inteiro: "))
while(num != 1):
    if (num > 0) and (num%2 == 0):
        ListaN.append(num)
    num = int(input("Digite um número inteiro: "))

print(ListaN)


