"""
8) Elaborar um programa que contem uma lista com 6 elementos. O usuário deve preencher essa 
lista. Após o usuário inserir todos os valores o programa deve exibir cada valor com sua posição 
na lista. 
"""

l1 = []
for inp in range(0,6):
    l1.append(input("Informe um elemento: "))
print()
for x in range(0,6):
    print("Posição: {} Elemento: {}".format(x, l1[x]))