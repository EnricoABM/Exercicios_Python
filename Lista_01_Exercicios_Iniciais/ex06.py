"""
Elaborar um programa que receba o salário de um 
funcionário e o percentual de aumento, calcule e mostre o 
valor do aumento e o novo salário

Entradas: Salario e Percentual de aumento
Saídas: Valor do aumento e Novo salário

Narrativa 
1 - Informe o salário
2 - Informe o percentual de aumento
3 - Calcule o valor do aumento
4 - Calcule o novo salário
5 - Imprimir o valor do aumento
6 - Imprimir o novo salário
"""

salario1 = float(input("Digite o valor do salário atual: R$"))
percentual = float(input("Digite o percentual de aumento(%):"))
aumento = salario1*percentual/100
salario2 = salario1+aumento
print("O aumento no salário foi de: R${:.2f}".format(aumento))
print("O novo valor do salário é de: {:.2f}".format(salario2))