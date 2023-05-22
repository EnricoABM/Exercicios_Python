"""
12) Elaborar um programa que leia o valor da hora de trabalho (em reais) e o número de horas 
trabalhadas no mês. O programa deve exibir o valor a ser pago ao funcionário, adicionando 12% 
sobre o valor calculado.

Entradas: Valor da hora de trabalho e Número de horas trabalhadas no mês. (vHT, nHT)
Saídas: Salário. (salario)
"""

vHT = float(input("Informe o valor da hora de trabalho: "))
nHT = float(input("Informe a quantidade de horas trabalhadas em um mês: "))
salario = (vHT*nHT)*1.12
print("O salário do funcionário já acrescido de 12% é de {:.2f}".format(salario))