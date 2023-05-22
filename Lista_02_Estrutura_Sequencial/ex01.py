"""
1) Elaborar um programa que receba um número que representa um comprimento em polegadas, 
converta e exiba o comprimento em milímetros, considerando que 1 polegada equivale a 25,4 
milímetros.

Entradas: Comprimento em polegadas. (comPol)
Saídas: Comprimento em milímetros. (comMil)

"""

comPol = float(input("Informe o comprimento em polegadas: "))
comMil = comPol*25.4
print("O comprimento em polegadas equivale a {:.2f} milímetros".format(comMil))