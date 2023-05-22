'''
4) Elaborar um programa que solicite ao usuário vários valores inteiros.
Quando o usuário digitar o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80,
quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário.
'''
num = int(input("Digite um número inteiro: "))
lnum = []
l80 = []
l10 = []
while (num != 100):
    lnum.append(num)
    if (num > 80):
        l80.append(num)
    if (num < 10):
        l10.append(num)
    num = int(input("Digite um número inteiro: "))
len(l80)
len(l10)
med = sum(lnum)/len(lnum)
print(f"{len(l80)} elementos tem valor maior que 80, {len(l10)} elementos tem valor menor que 10, e a média dos valores digitados é  {med}")