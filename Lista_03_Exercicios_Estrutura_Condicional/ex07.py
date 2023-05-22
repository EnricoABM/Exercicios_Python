'''
Faça um algoritmo que leia dois valores inteiros A e B se os 
valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. 
Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C 
e mostrar seu conteúdo na tela.
'''

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if (a == b):
    c = a + b
else: 
    c = a * b
    
print("O valor de c é igual à: ", c)