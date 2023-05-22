"""
14) Elaborar um programa para auxiliar vendedores. O programa deve receber o valor total de uma 
compra e deve calcular e exibir: valor à vista (total a pagar com desconto de 10%) e o valor de cada 
parcela (parcelamento de 3x sem juros).

Entradas: Valor total da compra. (vTCom)
Saídas: Valor à vista e Valor parcelado. (vVis, vPar)
"""
vTCom = float(input("Informe o valor total da compra: "))
vVis = vTCom*0.90
vPar = vTCom/3
print("O valor total da compra é: {:.2f}\nO valor da compra à vista é: {:.2f}\nO valor da compra parcelada é de 3x de: {:.2f}".format(vTCom,vVis,vPar))