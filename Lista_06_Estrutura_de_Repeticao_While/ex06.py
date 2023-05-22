'''
6) Elaborar um programa que solicita um número (entre 10 a 15). Se o usuário digitar um número
diferente, o programa deve mostrar a mensagem “Entrada inválida” e solicitar um número
novamente. Se digitar correto o programa deve mostrar a raiz quadrada desse número e
termina.

'''

num = float(input("Digite um número entre 10 e 15: "))

while(num < 10) or (num > 15):
    print("Entrada inválida")
    num = float(input("Digite outro número: "))

print(f"A raiz quadrada de {num} é {num**0.5:.2f}")
