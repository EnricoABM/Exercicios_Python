"""
9) Elaborar um programa que receba o peso de uma pessoa em quilos. Calcule e mostre: 
a. O novo peso se a pessoa engordar 15% sobre o peso digitado;
b. O novo peso se a pessoa emagrecer 20% sobre o peso digitado;

Entradas: Peso atual da pessoa. (pAtual)
Saídas: Peso após engordar 15% e Peso após emagrecer 20%. (pEng, pEma)
"""

pAtual = float(input("Informe seu peso em quilos: "))
pEng = pAtual*1.15
pEma = pAtual*0.8
print("Se a pessoa engordar 15% pesará {:.2f} quilos\nSe a pessoa emagrecer 20% pesará {:.2f} quilos".format(pEng,pEma))