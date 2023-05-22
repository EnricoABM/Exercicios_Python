'''
2) Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana
correspondente. O programa deve repetir até que o usuário digite um número fora desse
intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número
inválido”.

'''
print('''
1. Domingo
2. Segunda
3. Terça
4. Quarta
5. Quinta 
6. Sexta
7. Sábado
''')
Dia = int(input("Informe um número correspondente a um dia da semana, conforme a tabela acima: "))

Dias = ["0","Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

while (Dia > 0) and (Dia <= 7): 
    print(Dias[Dia])
    Dia = int(input("Informe outro número da tabela: "))

else:
    print("Número inválido")