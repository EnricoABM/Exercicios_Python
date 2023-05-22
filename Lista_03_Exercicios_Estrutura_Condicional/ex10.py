'''
Elaborar um programa que leia o número de identificação,
as 3 notas obtidas por um aluno nas 3 verificações e a 
média dos exercícios que fazem parte da avaliação, e 
calcule a média de aproveitamento, usando a fórmula:
    MA = (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7

A atribuição dos conceitos obedece a tabela abaixo. O
algoritmo deve escrever o número do aluno, suas notas, a
média dos exercícios, a média de aproveitamento, o conceito
correspondente e a mensagem 'Aprovado' se o conceito for A,
B ou C, e 'Reprovado' se o conceito for D ou E.

----------------------------------
-Média de aproveitamento Conceito-
----------------------------------
-         >= 90          -   A   -
-     >= 75 e < 90       -   B   -
-     >= 60 e < 75       -   C   -
-     >= 40 e < 60       -   D   -
-         < 40           -   E   -
----------------------------------
'''

#Entradas: Número de identificação, Nota 1, Nota 2, Nota 3, Média dos exercicios;
#Processamento: Média de aproveitamento, Conceito, Mensagem;
#Sáidas: Média de aproveitamento, Número de identificação, Notas, Média dos exercicios, Conceito, Mensagem;

print("Calculo de Aproveitamento de um Aluno")
nID = input("Informe seu número de identificação: ")
n1 = float(input("Informe a nota da primeira avaliação: ")) 
n2 = float(input("Informe a nota da segunda avaliação: "))
n3 = float(input("Informe a nota da terceira avaliação: "))
mEX = (n1 + n2 + n3)/3
mA = (n1 + n2 * 2 + n3 * 3 + mEX)/7
conc = ""
sit = ""

if (mA >= 90):
    conc = "A"
elif (mA >= 75) and (mA < 90):
    conc = "B"
elif (mA >= 60) and (mA < 75):
    conc = "C"
elif (mA >= 40) and (mA < 60):
    conc = "D"
elif (mA < 40):
    conc = "E"

if (conc == "A") or (conc == "B") or (conc == "C"):
    sit = "Aprovado"
elif (conc == "D") or (conc == "E"):
    sit = "Reprovado" 

print('''
Número do aluno: {};
Avalição 1: {};             Avalição 2: {};
Avalição 3: {};             Média dos exercícios: {:.2f}; 
Média de Aproveitamento: {:.2f};
Conceito: {}                Situação: {};
'''.format(nID, n1, n2, n3, mEX, mA, conc, sit))