"""
Elaborar um programa que calcule o consumo médio de um
automóvel (medido em km/l), dado que são conhecidos
a distância total percorrida e o volume de combustível 
consumido para percorrê-la (medido em litros)

Entradas: Distância percorrida e volume de combustível consumido
Saídas: Consumo médio de um automóvel

1 - Informar o distância percorrida (d)
2 - Informar o volume de combustível consumido (v)
3 - Calcular o consumo médio de um automóvel (media)
4 - Imprimir o consumo médio de um automóvel
"""

d = float(input("Informe a distância percorrida em Km:"))
v = float(input("Informe o volume de combustível consumido em L:"))
media = d/v
print("A média consumo nesta viagem foi de {:.2f} Km/L".format(media))