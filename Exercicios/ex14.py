"""
Elaborar um programa que leia uma temperatura em graus 
Celsius e deve converter em graus Fahrenheit. A fórmula 
de conversão é: F = (9*C+160)/5, sendo F a temperatura em 
Fahrenheit e C a temperatura em Celsius. Exibir a 
temperatura em Fahrenheit

Entradas: Temperatura em graus Celsius 
Saídas: Temperatura em Graus Fahrenheit

Narrativa
1 - Informe a temperatura em graus Celsius 
2 - Calcule a temperatura em graus Fahrenheit
3 - Imprima a temperatura em graus Fahrenheit 
"""

temperaturaC = float(input("Digite a temperatura em graus Celsius: "))
temperaturaF = (9*temperaturaC+160)/5
print("A conversão de graus Celsius em graus Fahrenheit resultou em: {:.2f} graus Fahrenheit".format(temperaturaF))