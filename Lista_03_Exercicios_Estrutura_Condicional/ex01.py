
#Elaborar um programa que leia dois números e apresente-os em ordem crescente.

#Entradas: n1, n2;
#Saídas: ordem crescente; 

print("Programa para exibir números em ordem crescente")
n1 = float(input("Digite o valor do primeiro número:"))
n2 = float(input("Digite o valor do segundo número:"))
if (n1 > n2):
    print("Ordem crescente dos números é: {:.1f} - {:.1f}".format(n2, n1))
else:
    print("Ordem crescente dos números é: {:.1f} - {:.1f}".format(n1, n2))
