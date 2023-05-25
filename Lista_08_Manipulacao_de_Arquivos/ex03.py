'''
3) Desenvolva um programa que cadastra alunos:
-> O programa deve registrar nome, e-mail e curso do
aluno.
-> Cada novo registro deve ser armazenado em uma
nova linha.
-> O usuário deve ter as seguintes opções:
    Cadastrar novo aluno.
    Listar alunos cadastrados.
    Buscar aluno.
    Remover aluno.
'''
nome_arq = "alunos.txt"
# Menu
def menu():
    print("\nPainel de Alunos\n")
    print("1 - Cadastrar novo aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Saída\n")

# Cadastro
def registro():
    inicio = "on"
    while(inicio == "on"):    
        print("\nCadastro de um novo aluno\n")
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail: ")
        curso = input("Digite o curso: ")
        arquivo = open(nome_arq, "a")
        arquivo.write(f"{nome.title()} - {email} - {curso}\n")
        arquivo.close()
        continuar = input("Deseja voltar ao menu: (S - Sim/N - Não) ")
        if continuar.upper() == "S":
            inicio = "off" 

# Listar
def listar():
    inicio = "on"
    while(inicio == "on"): 
        print("\nLista de alunos cadastrados\n")
        arquivo = open(nome_arq, "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha)
        print()
        arquivo.close()
        continuar = input("Deseja voltar ao menu: (S - Sim/N - Não) ")
        if continuar.upper() == "S":
            inicio = "off"

# Busca
def buscar():
    inicio = "on"
    while(inicio == "on"): 
        arquivo = open(nome_arq, "r")
        nome_busca = input("Digite o nome que deseja buscar: ")
        linhas = arquivo.readlines()
        for linha in linhas:
            separacao = list(linha.split("-"))   
            for x in separacao[0::3]:
                if nome_busca.title() in x:
                    print("\nNome - E-mail - Curso")
                    print(linha)
        arquivo.close()
        continuar = input("Deseja voltar ao menu: (S - Sim/N - Não) ")
        if continuar.upper() == "S":
            inicio = "off"
# Remoção
def remover():
    inicio = "on"
    while(inicio == "on"): 
        nome_remover = input("Digite o nome do aluno que deseja remover: ")
        arquivo = open(nome_arq, "r")
        linhas = arquivo.readlines()
        for indice, conteudo in enumerate(linhas):
            separacao = list(conteudo.split("-"))
            for x in separacao[0::3]:
                if nome_remover.title() in x:
                    indice_remover = indice
        del linhas [indice_remover]
        arquivo.close()
        novo_arquivo = open(nome_arq, "w")
        novo_arquivo.writelines(linhas)
        novo_arquivo.close()
        continuar = input("Deseja voltar ao menu: (S - Sim/N - Não) ")
        if continuar.upper() == "S":
            inicio = "off"
# Variaveis

# Main 
iniciarMain = "on"
while(iniciarMain == "on"):
    menu()
    op = input("Digite uma opção: ")
    while(op != "1") and (op != "2") and (op != "3") and (op != "4") and (op != "5"):
        print("\nValor inválido")
        menu()
        op = input("Digite uma opção novamente: ")
    if (op == "1"):
        registro()
    elif (op == "2"):
        listar()
    elif (op == "3"):
        buscar()
    elif (op == "4"):
        remover()
    elif (op == "5"):
        iniciarMain = "off"
