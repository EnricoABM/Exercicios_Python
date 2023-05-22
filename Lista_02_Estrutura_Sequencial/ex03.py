"""
3) Elaborar um programa que leia um valor de temperatura em graus Celsius, calcule e exiba a
temperatura equivalente em Kelvin, sabendo que: K = C + 273.

Entradas: Temperatura em graus Celsius. (tempCel)
Saídas: Temperatura em Kelvin. (tempKel)
"""

tempCel = int(input("Informe a temperatura em graus Celsius: "))
tempKel = tempCel + 273
print("A temperatura em graus Celsius equivale a {} Kelvin".format(tempKel))