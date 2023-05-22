'''
1) Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada
temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na
tela. O programa termina quanto a temperatura inserida for menor que -5.

'''
C = float(input("Informe uma temperatura em graus Celsius: "))
while (C > -5):
    F = (C * 1.8) + 32
    K = 273.15 + C
    print(f"A conversão de {C:.2f} °C em Fahrenheit é {F:.2f} °F e em Kelvin é {K:.2f} °K")
    C = float(input("Informe uma temperatura em graus Celsius: "))
    
