"""
Elaborar um programa que leia três números inteiros 
(A, B, C) e calcule a seguinte expressão
D = (R + S)/2 onde R = (A+B)² e S = (B+C)². Exibir o valor D

Entradas: A, B e C
Saídas: D, R e S

Narrativa
1 - Informar um número para A 
2 - Informar um número para B 
3 - Informar um número para C
4 - Calcule o valor de R
5 - Calcule o valor de S
6 - Calcule o valor de D
7 - Imprimir o valor de D
"""

import math

numA = int(input("Digite um valor para A: "))
numB = int(input("Digite um valor para B: "))
numC = int(input("Digite um valor para C: "))
numR = numA**2+2*numA*numB+numB**2
numS = numB**2+2*numB*numC+numC**2
numD = (numR + numS)/2
print("O valor de D é: {}".format(numD))