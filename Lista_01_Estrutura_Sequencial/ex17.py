"""
Elaborar um programa que leia a idade de uma pessoa 
expressa em anos, meses e dias e mostre-a expressa apenas 
em dias.

Entradas: Anos de Idade, Meses e Dias
Saídas: Dias de Idade
18 5 14
Narrativa
1 -Informar a idade em anos 
2 -Informar os meses 
3 -Informar os dias
4 -Calcular idade em dias
5 -Imprimir a idade em dias
"""

anos = int(input("Informe sua idade em anos: "))
meses = int(input("Informe quantos meses passaram do seu aniversário: "))
dias = int(input("Informe quantos dias passaram do seu aniversário: "))
diasIdade = anos*365+(anos//4)+meses*30+dias
print("Essa pessoa possui {} dias de idade".format(diasIdade))