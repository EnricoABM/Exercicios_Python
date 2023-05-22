"""
1) Elaborar um programa que lê dois valores. Ele deve apresentar a soma desses valores e indicar 
qual é o maior valor entre eles. Esse programa deve-se repetir 5 vezes.
"""

for rep in range(0,5):
    l1 = []
    for inp in range(0,2):
        l1.append(float(input("Digite um número: ")))
    print("A soma dos dois números é: {}".format(sum(l1)))
    print("O maior número é: {}".format(max(l1)))