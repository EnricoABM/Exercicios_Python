"""
Elaborar um programa que dados dois lados de um triângulo 
retângulo calcule e exiba a respectiva hipotenusa

Entradas: Cateto 1 e Cateto 2 
Saídas: Hipotenusa

Narrativa
1 - Informe o valor do cateto 1
2 - Informe o valor do cateto 2
3 - Calcule o quadrado da hipotenusa
4 - Calcule a raiz quadrada da hipotenusa
5 - Imprima o valor da hipotenusa
"""

import math
cat1 = float(input("Digite o comprimento do primeiro cateto em cm: "))
cat2 = float(input("Digite o comprimento do segundo cateto em cm: "))
hipotenusa2 = math.pow(cat1,2)+math.pow(cat2,2)
hipotenusa = math.sqrt(hipotenusa2)
print("O comprimento da hipotenusa é {:.2f} centimetros".format(hipotenusa))
