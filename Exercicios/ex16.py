"""
Elaborar um programa que leia 3 notas de um aluno e calcule
a média final deste aluno. Considerar que a média é 
ponderada e que o peso das notas é: 2, 3 e 5, respectivamente

Entradas: Primeira Nota, Segunda Nota e Terceira Nota
Saídas: Média do Aluno 

Narrativa
1 - Informar a primeira nota
2 - Informar a segunda nota
3 - Informar a terceira 
4 - Calcular a média
5 - Imprimir a média 
"""

n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))
media = (n1*2+n2*3+n3*5)/10
print("A nota deste aluno é: {:.2f}".format(media))