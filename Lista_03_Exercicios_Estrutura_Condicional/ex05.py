#Elaborar um programa que receba os valores A,B,C e mostre na tela se a soma de A+B é menor que C.

#Entradas: a, b, c
#Saídas: soma, comp;

print("Programa que informa se a soma de dois números é maior que um terceiro número")
a = float(input("Digite o primeiro número"))
b = float(input("Digite o segundo número"))
c = float(input("Digite o terceiro número"))
soma = a+b
if (soma > c):
    print("A soma do primeiro e do segundo número é maior que o terceiro número")
else:
    print("O terceiro número é maior que a soma do primeiro e do segundo número")
    