"""
2) Elaborar um programa que ao receber a cotação do dólar no dia e a quantidade de dólares para 
trocar por real, deve exibir a quantidade em reais.

Entradas: Cotação do dólar e Quantidade de dólares. (cDol,qDol)
Saídas: Quantidade em reais. (qReal)
"""

cDol = float(input("Informe a cotação do dolar em reais: "))
qDol = float(input("Informe a quantidade de dólares: "))
qReal = cDol*qDol
print("A conversão de dólares para reais equivale à: R${:.2f}".format(qReal))