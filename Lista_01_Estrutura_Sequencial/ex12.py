"""
Elaborar um programa que receba o raio de uma esfera. 
O algoritmo deve calcular e exibir a área e o volume da 
esfera.

Entradas: Raio de uma esfera
Saídas: Área da esfera e Volume da esfera

Narrativa
1 - Informar o raio da esfera
2 - Calcular o área da esfera
3 - Calcular o volume da esfera
4 - Imprimir a área da esfera
5 - Imprimir o volume da esfera
"""

import math
raio = float(input("Digite o raio da esfera: "))
area = 4*math.pi*math.pow(raio,2)
volume = (4/3)*math.pi*math.pow(raio,3)
print("A área da esfera é de {:.2f} m²\nO volume da esfera é {:.2f} m³".format(area,volume))
