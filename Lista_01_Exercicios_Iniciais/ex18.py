"""
Elaborar um programa que leia o tempo de duração de um 
evento em uma fábrica expressa em segundos e mostre-o 
expresso em horas, minutos e segundos.

Entradas: Tempo de duração em segundos
Saídas: Horas, Minutos e Segundos

Narrativa
1 - Informe a duração do evento em segundos
2 - Calcule horas
3 - Calcule minutos
4 - Calcule segundos
5 - Imprima a duração na tela em horas, minutos e segundos
"""

dES = int(input("Informe a duração do evento em segundos: "))
horas = dES//3600
minutos = (dES-horas*3600)//60
seg = (dES-horas*3600-minutos*60)
print("O evento tem a duração de {} horas, {} minutos e {} segundos".format(horas,minutos,seg))