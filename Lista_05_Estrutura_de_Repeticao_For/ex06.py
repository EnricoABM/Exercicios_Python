"""
6) Elaborar um programa que o usuário tenha que digitar 10 números inteiros. No final, o programa 
deve exibir quantos números são múltiplos de 3, quantos números são menores que 45 e maiores 
que 55, qual é o menor número entre eles e qual a média
"""
l1 = []
mul3 = []
me45 = []
ma55 = []

for rep in range(0,10):
    l1.append(int(input("Informe um número inteiro: ")))    

for x in l1:
    if (x % 3 == 0):
        mul3.append(x)
    if (x  < 45):
        me45.append(x)
    if (x > 55):
        ma55.append(x)

media = sum(l1)/len(l1)

print('''
Números multiplos de 3: {} números
Números menores que 45: {} números
Números maiores que 55: {} números
Menor número entre eles: {}
Média: {}
'''.format(len(mul3), len(me45), len(ma55), min(l1), media))
