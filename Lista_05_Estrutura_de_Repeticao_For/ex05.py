"""
5) Elaborar um programa que solicita 15 temperaturas em graus Celsius. Para cada temperatura 
inserida, o programa deve convertê-la em graus Fahrenheit e mostra-la na tela.
"""
for rep in range(0,15):
    C = float(input("Informe a temperatura em graus Celsius: "))
    F = (C * 1.8) + 32
    print("A temperatura em graus Celsius {:.2f}°C convertida em graus Fahrenheit é: {:.2f}°F".format(C,F))
