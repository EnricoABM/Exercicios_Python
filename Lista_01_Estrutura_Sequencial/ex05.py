"""
Elaborar um programa que leia o saldo de uma aplicação e
imprimir o novo saldo, considerando um reajuste de 15%
Entradas: Valor do salário
Saídas: Valor do reajuste

Narrativa
1 - Informe o valor do salário
2 - Calcular o valor do reajuste
3 - Imprimir o valor do reajsute
"""
salario = float(input("Digite o salário atual: R$"))
reajsute = salario*1.15
print("O valor do salário foi alterado para: R${:.2f}".format(reajsute))