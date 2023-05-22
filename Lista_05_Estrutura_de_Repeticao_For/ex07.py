"""
7) Elaborar um programa que lê duas notas (P1 e P2). Caso a média seja maior igual a 5 deve 
exibir a mensagem “APROVADO”. Caso a média seja menor que 5 e maior igual a 3 deve exibir a 
mensagem “EXAME”. Caso contrário exibir a mensagem “REPROVADO”. Caso esteja de exame o 
programa deve solicitar a nota de exame e verificar se o aluno está aprovado ou não e exibir o 
resultado na tela. Esse programa deve-se repetir para 30 alunos.
"""
for rep in range(0,30):
    P1 = float(input("Informe a primeira nota: "))
    P2 = float(input("Informe a segunda nota: "))
    media = (P1 + P2*2)/3
    if (media >= 5):
        print("APROVADO")
    elif (media < 5) and (media >= 3):
        print("EXAME")
        P3 = float(input("Informe a nota do exame: "))
        mediaE = (media + P3)/2
        if (mediaE > 5):
            print("APROVADO")
        else:
            print("REPROVADO")
    else:
        print("REPROVADO") 