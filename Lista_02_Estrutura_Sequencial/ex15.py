"""
15) Elaborar um programa que receba o salário-base de um funcionário. Calcule e imprima o salário 
a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além 
disso, ele paga 7% de imposto sobre o salário-base.

Entradas: Salário base. (salBase)
Saídas: Salário a receber. (salRec)
"""

salBase = float(input("Informe o salário base do funcionário: "))
salRec = (salBase*1.05) - (salBase*0.07)
print("O salário base do funcionário é de R$ {:.2f}, e o salário a receber é de R$ {:.2f}".format(salBase,salRec))