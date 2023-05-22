"""
9) Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve 
copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista B. 
"""

lista_A = []
lista_B = []

for rep in range(0,15):
    lista_A.append(float(input("Informe um número: ")))
X = float(input("Informe o valor de X: "))

for comp in lista_A:
    if (comp > X):
        lista_B.append(comp)
print("lista B")
print(lista_B)
