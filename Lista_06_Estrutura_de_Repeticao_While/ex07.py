'''
7) Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o
código do item pedido, a quantidade e somar para calcular o valor a ser pago. O programa
termina quando o código for 0 (zero). O cardápio da lanchonete é o seguinte:
'''
#Código     Especificação       Preço unitário
#100        Cachorro quente     3.50
#101        Bauru Simples       3.80
#102        Bauru c/ ovo        4.50
#103        Hamburguer          4.70
#104        Cheeseburguer       5.30
#105        Refrigerante        4.00

cod = int(input("Informe o código do item pedido: "))

while (cod != 0):
    qnt = int(input("Informe a quantidade do item pedido: "))
    if cod == 100:
        vPago = qnt*3.50
    elif cod == 101:
        vPago = qnt*3.80
    elif cod == 102:
        vPago = qnt*4.5
    elif cod == 103:
        vPago = qnt*4.7
    elif cod == 104:
        vPago = qnt*5.3
    elif cod == 105:
        vPago = qnt*4
    
    print("O valor a ser pago é: R$", vPago)
    cod = int(input("Informe o código do item pedido: "))

