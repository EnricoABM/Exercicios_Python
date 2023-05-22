"""
Elaborar um programa que receba o raio e a altura de uma 
lata de óleo para calcular e apresentar o valor do volume 
desta lata, dado: V = π*r2*h

Entradas: Raio de uma lata e Altura de uma lata
Saídas: Valor do volume da lata

Narrativa
1 - Informe o raio da lata
2 - Informe a altura da lata
3 - Calcular o volume da lata
4 - Imprimir o volume da lata
"""

import math 
raio = float(input("Digite o comprimento do raio da lata em cm: "))
altura = float(input("Digite a altura da lata em cm: "))
volume = math.pi*math.pow(raio,2)*altura
print("O volume desta lata é de {:.2f} cm³".format(volume))