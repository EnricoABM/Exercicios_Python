"""
10) Elaborar um programa que contem uma lista com 5 elementos. O usuário deve preencher essa 
lista. Exibir no final os valores inseridos pelo usuário, porém os valores negativos (caso existirem) 
devem ser substituídos por zero (0).
"""

l1 = []
for inp in range(0,5):
    l1.append(float(input("Informe um número: ")))
print(l1)
for neg in l1:
    if neg < 0:
        l1[l1.index(neg)] = 0
print(l1)