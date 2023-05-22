"""
10) Elaborar um programa que realize a divisão de um prêmio que será dividido entre três 
ganhadores de um concurso. Após o programa receber o valor do prêmio, deve calcular e exibir o 
valor que cada ganhador receberá. O primeiro ganhador receberá 47%, o segundo receberá 34% 
e o terceiro receberá o restante.

Entradas: Valor do prêmio. (vPrem)
Saídas: Prêmio do ganhador 1, Prêmio do ganhador 2 e Prêmio do ganhador 3. (pg1, pg2, pg3)
"""
vPrem = float(input("Informe o valor do prêmio do concurso: "))
pg1 = vPrem*0.47
pg2 = vPrem*0.34
pg3 = vPrem - (pg1 + pg2)
print("O valor do prêmio do concurso é: {:.2f}\nO primeiro ganhador receberá {:.2f}\nO segundo ganhador receberá {:.2f}\nO terceiro ganhador receberá {:.2f}\n".format(vPrem, pg1, pg2, pg3))