"""
6) Elaborar um programa que receba o custo de um espetáculo teatral e o preço do convite deste 
espetáculo. Esse programa deve calcular e mostrar a quantidade de convites que devem ser 
vendidos para que pelo menos o custo do espetáculo seja alcançado.

Entradas: Custo total do espetáculo e Preço do convite. (cEsp,pCon)
Saídas: Quantidade a ser vendida. (qVen)
"""

cEsp = float(input("Informe o custo total do espetáculo: "))
pCon = float(input("Informe o preço do convite: "))
qVen = cEsp/pCon
print("É necessário vender {:.2f} convites para cobrir o custo total do espetáculo".format(qVen))