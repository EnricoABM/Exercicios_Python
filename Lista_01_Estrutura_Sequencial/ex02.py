"""
Elaborar um programa que receba quatro números inteiros,
que calcule e mostre a soma e a média desses números.

Entradas: Primeiro número, Segundo número, Terceiro número e Quarto número
Saidas: Soma e média

Narrrativa
1 - Inserir o primeiro número
2 - Inserir o segundo número
3 - Inserir o terceiro número
4 - Inserir o quarto número
5 - Calcular soma dos números
6 - Calcular média dos números
7 - Imprimir o valor da soma
8 - Imprimir o valor da média
"""
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))
num4 = float(input("Digite o quarto número:"))
soma = num1 + num2 + num3 + num4
media = soma/4
print("Soma dos 4 números é: {}\nA média entre os 4 números é: {}".format(soma,media)) 
