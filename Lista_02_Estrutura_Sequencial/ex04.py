"""
4) Elaborar um programa em que o usuário deve inserir três números reais (B, b, h). Logo após, 
deve calcular a área de um trapézio e exibir o resultado. Tendo como fórmula:
A = ((B + b) .h)/2.

Entradas: Lado B, Lado b e Altura h. (B, b, h)
Saídas: Área do trapézio. (A)
"""

B = float(input("Informe o lado B do trapézio: "))
b = float(input("Informe o lado b do trapézio: "))
h = float(input("Informe a altura h do trapézio: "))
A = ((B + b)*h)/2
print("A área do trapézio equivale a {:.2f} unidades de área".format(A)) #unidades de área = pode ser cm², m², n². Não foi especificado.