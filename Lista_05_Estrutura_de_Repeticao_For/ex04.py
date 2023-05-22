"""
4) Elabore um programa que leia um nº inteiro e mostre uma mensagem indicando se este número 
é múltiplo de 3 e se é positivo ou negativo. Esse programa deve-se repetir 10 vezes.
"""

for rep in range(0,10):
    num = int(input("Informe um número inteiro: "))
    if (num % 3 == 0) and (num > 0):
        print("Este número positivo é múltiplo de 3")
    elif (num % 3 == 0) and (num < 0):
        print("Este número negativo é múltiplo de 3")
    elif (num % 3 != 0) and (num > 0):
        print("O número positivo não é múltiplo de 3")
    elif (num % 3 != 0) and (num < 0): 
        print("O número negativo não é múltiplo de 3")