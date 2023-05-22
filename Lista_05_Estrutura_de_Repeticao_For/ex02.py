"""
2) Elaborar um programa que lê 3 valores (A, B e C) e exibe qual é o maior entre eles. Esse 
programa deve-se repetir 20 vezes.
"""

for rep in range(0,20):
    print("Informe 3 valores diferentes")
    A = float(input("Informe o valor de A: "))
    B = float(input("Informe o valor de B: "))  
    C = float(input("Informe o valor de C: "))
    if (A > B) and (A > C):
        print("O maior valor é de A, com valor de: ", A)
    elif (B > C) and (B > A):
        print("O maior valor é de B, com valor de: ", B)
    elif (C > A) and (C > B):
        print("O maior valor é de C, com valor de: ", C)      
    else:
        print("Valor inválido")