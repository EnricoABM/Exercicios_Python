"""
Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome, 
telefone e o salário líquido, considerando:
a) os dados do funcionário: nome, RG e telefone.
b) salário bruto de R$ 2500,00
c) descontos de R$ 300,00

Entradas: Nome, RG, Telefone, Salário Bruto e Desconto;
Saídas: Salário Líquido, Nome e Telefone;

Narrativa:
1 - Informe o seu nome;
2 - Informe o seu RG;
3 - Informe o seu telefone; 
4 - Calcule o salário líquido; 
5 - Mostre o salário líquido, nome e telefone;

Código
"""
nome = input("Informe seu nome: ")
RG = input("Informe seu RG: ")
telefone = ("Informe seu telefone: ")
sLiq = 2500-300 #sBrt-des
print("O funcionário {} de telefone {} recebe R${} de salário líquido.".format(nome,telefone,sLiq))
