"""
Elaborar um programa que receba o ano de nascimento de uma
pessoa e o ano atual, calcule e mostre: 
- A idade desta pessoa hoje;
- A idade desta pessoa em 2035

Entradas: Ano de nascimento e Ano atual
Saídas: Idade hoje e Idade em 2025

Narrativa 
1 - Informar o ano atual
2 - Informar o ano de nascimento 
3 - Calcular idade hoje
4 - Calcular idade em 2025
5 - Imprimir a idade hoje 
6 - Imprimir a idade em 2025
"""

anoHoje = int(input("Digite o ano atual:"))
anoNascimento = int(input("Digite o ano do seu nascimento:"))
idadeHoje = anoHoje-anoNascimento
idade2025 = 2025-anoNascimento
print("Esta pessoa possui {} anos de idade\nEm 2025 ela tinha/terá {} anos de idade".format(idadeHoje,idade2025))