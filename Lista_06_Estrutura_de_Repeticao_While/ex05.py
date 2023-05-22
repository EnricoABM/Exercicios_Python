'''
5) Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2
deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até
N.

'''

num = int(input("Digite um número inteiro maior que 2: "))

while(num < 2):
    num = int(input("Digite outro número: "))
x = 2
while(x <= num):
    print(f"Quadrado de {x} = {x**2}")
    print(f"Cubo de {x} = {x**3}")
    print()
    x += 1

