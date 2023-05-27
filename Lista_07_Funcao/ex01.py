'''
Criar um programa que contenha as seguintes funções:
'''

'''
1) Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro e devolve o seu dobro.
'''
def ex01(numero):
    result = numero*2
    return result

'''
2) Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.
'''

def ex02(numero):
    if numero < 0:
        result = -1
    elif numero > 0:
        result = 1
    else:
        result = 0
    return result

'''
3) Elaborar uma função que retorna o cálculo do volume de uma esfera. Sendo que o raio é passado por parâmetro.
'''

def ex03(raio):
    volume = (4/3) * 3.14 * raio**3
    return volume

'''
4) Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro. Logo em seguida a função deve exibir um menu com 4 opções: 
a) Soma 
b) Subtrair
c) Multiplicar
d) Dividir
e) Raiz quadrada do primeiro número.
Quando o usuário selecionar a operação desejada, a função deve exibir o resultado na tela.
'''

def ex04(num1, num2):
    print("a) Soma\nb) Subtrair\nc) Multiplicar\nd Dividir\ne) Raiz quadrada do primeiro número")
    op = input("Informe qual opção deseja: ")
    op = op.lower()
    if op == "a":
        result = num1 + num2
    elif op == "b":
        result = num1 - num2
    elif op == "c":
        result = num1 * num2
    elif op == "d":
        result = num1 / num2
    elif op == "e":
        result = num1**0.5
    else:
        result = "Valor inválido"
    print(result)

'''
5) Elaborar uma função (sem retorno) que ao receber um número deve converte em Fahrenheit e exibe o resultado na tela. A fórmula de conversão é: F = (9*C+160) / 5.
'''

def ex05(temp):
    F = (9*temp+160)/5
    print(F)

'''
6) Elaborar uma função (com retorno) que ao receber um número deve converte em Kelvin e exibe o resultado na tela. A fórmula de conversão é: K=C+273,15.
'''
def ex06(temp):
    K = temp + 273.15
    return print(K)

'''
7) Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo. A função quando chamada retorna 1 indicando que o número é primo e 0 caso contrário.
'''

def ex07(num):
    mults = 0
    for n in range(1,num+1):
        if num%n == 0:
            mults += 1
        if mults == 2:
            primo = 1
        else:
            primo = 0       
    return primo
print(ex07(21))