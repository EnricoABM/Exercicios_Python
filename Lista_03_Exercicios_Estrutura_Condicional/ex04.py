#Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. 
#Caso o usuário digite um número fora desse intervalo, o algoritmo mostra uma mensagem informando “Número inválido”.

#Entradas: sequencia de 1 a 7;
#Saídas: dia da semana e mensagem de erro;

print("Programa que lê um número e exibe o dia semana correspondente")

dia = int(input("Digite um número entre 1 e 7:"))

if (dia == 1):
    print("Domingo")
elif(dia == 2):
    print("Segunda-Feira")
elif(dia == 3):
    print("Terça-Feira")
elif(dia == 4):
    print("Quarta-Feira")
elif(dia == 5):
    print("Quinta-Feira")
elif(dia == 6):
    print("Sexta-Feira")
elif(dia == 7):
    print("Sabado")
else:
    print("Número inválido")
