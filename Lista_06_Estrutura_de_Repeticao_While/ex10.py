'''
10) Elaborar um programa que contem uma lista com 15 elementos. 
Essa lista deve ser preenchida pelo usuário, porém não deve conter valores repetidos. 
Exibir no final a lista.
'''

l1 = []
rep = 0

while (rep < 15):
    num = (float(input("Digite um número: ")))
    if (0 == l1.count(num)):
        l1.append(num)
    rep += 1
print(l1)
    
        



