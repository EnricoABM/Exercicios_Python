"""
Elaborar um programa que calcule a aceleração de um corpo 
em movimento conhecendo-se as velocidades inicial e final, 
e o intervalo de tempo medido (a = (v2 –v1)/∆t). Exibir o 
resultado

Entradas: Velocidade final, Velocidade inicial e o Intervalo de tempo medido 
Saídas: Aceleração de um corpo 

Narrativa 
1 - Informe a velocidade inicial 
2 - Informe a velocidade final
3 - Informe o intervalo de tempo medido
4 - Calcule a aceleraçãp de um corpo
5 - Imprima a aceleração de um corpo
"""

vel1 = float(input("Digite o valor da velocidade inicial do corpo: "))
vel2 = float(input("Digite o valor da velocidade final do corpo: "))
t = float(input("Digite o intervalo de tempo:"))
a = (vel2 - vel1)/t
print("A aceleração deste corpo é de: {:.2f}".format(a))
