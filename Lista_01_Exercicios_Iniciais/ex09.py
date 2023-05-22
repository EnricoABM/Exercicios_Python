"""
Elaborar um programa que receba um número positivo e maior
que zero, calcule e mostre: 
a) o número digitado ao quadrado;
b) a raiz quadrada do número digitado

Entradas: Número positivo maior que zero
Saídas: Número ao quadrado e Raiz quadrada do número

Narrativa
1 - Informe um número positivo maior que zero
2 - Calcule a raiz quadrada deste número
3 - Calcule o quadrado deste número
4 - Imprimir a raiz quadrada número
5 - Imprimir o quadrado deste número
"""
import math
n = float(input("Digite um número positivo maior que zero:"))
raiz = math.sqrt(n)
pot = math.pow(n,2)
print("O quadrado deste número é igual a: {}\nA raiz quadrada deste número é: {}".format(pot,raiz))
