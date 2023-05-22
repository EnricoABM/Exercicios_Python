#Elaborar um programa que calcule a soma de dois números quaisquer e apresente na tela o resultado dessa soma.
#Caso a soma seja superior a 30 indicar qual é o maior valor entre eles.

#Entradas: n1, n2;
#Sáidas: soma, maior;

print("Programa para somar dois números e apresentar o resultado")
n1 = float(input("Digite o valor do primeiro número:"))
n2 = float(input("Digite o valor do segundo número:"))
soma = n1 + n2
print("O resultado da soma é: {:.2f}".format(soma))
if (soma > 30):
    if (n1 > n2):
        print("O maior número entre eles é:", n1)
    else:
        print("O maior número entre eles é:", n2)

    