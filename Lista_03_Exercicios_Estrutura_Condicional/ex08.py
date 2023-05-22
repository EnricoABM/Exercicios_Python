'''
O IMC – Indice de Massa Corporal é um critério da
Organização Mundial de Saúde para dar uma indicação
sobre a condição de peso de uma pessoa adulta. A fórmula
é IMC = peso / ( altura )ˆ2. Elaborar um programa que
leia o peso e a altura de um adulto e mostre sua condição
de acordo com a tabela abaixo
---------------------------------------------
|       IMC em adultos Condição             |
|-------------------------------------------|
|   Abaixo de 18,5   |  Abaixo do peso      |
|   Entre 18,5 e 25  |  Peso normal         |
|   Entre 25 e 30    |  Acima do peso       |
|   Acima de 30      |  Obeso               |
---------------------------------------------
'''

print("Calculadora de IMC")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso/(altura**2)
cond = ""
if (imc < 18.5):
    cond = "Abaixo do peso"
elif (imc >= 18.5) and (imc < 25):
    cond = "Peso normal"
elif (imc >= 25) and (imc < 30):
    cond = "Acima do peso"
elif (imc > 30):
    cond = "Obeso"
print("Segundo o IMC está pessoa é:", cond)
