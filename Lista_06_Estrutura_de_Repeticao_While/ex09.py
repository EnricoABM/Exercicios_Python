'''
9) Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve
preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois
números. Esses números devem corresponder a posições na lista (caso contrário solicite um novo valor). Após inserir os dois números o 
programa deve exibir a soma dos elementos das duas posições da lista.

'''
l1 = []
rep = 0
while (rep < 25):
    l1.append(float(input("Digite um número: ")))
    rep += 1
p = int(input("Informe a primeira posição: ")) 
while (p < 1) or (p > 25):
    p = int(input("Informe a primeira posição novamente: "))

s = int(input("Informe a segunda posição: "))
while(s < 1) or (s > 25):
    s = int(input("Informe a segunda posição novamente: "))

soma = l1[p - 1] + l1[s - 1]
print(f"O valor da soma é {soma}")
