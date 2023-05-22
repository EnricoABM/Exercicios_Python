"""
Elaborar um programa que dados o tamanho de um arquivo 
(em bits), bem como a velocidade da conexão (em bits por 
segundo), informe o tempo necessário para o download do 
arquivo.

Entradas: Tamanho do arquivo e velocidade da conexão
Saidas: Tempo de download

Narrativa
1 - Informar o tamanho do arquivo
2 - Informar a velocidade da conexão
3 - Calcular o tempo de download
4 - Imprimir o tempo de downnload
"""

tamanho = int(input("Digite o tamanho do arquivo em bits:"))
velocidade = int(input("Digite a velocidade da conexão em bits por segundo:"))
tempo = tamanho/velocidade
print("O tempo aproximado para o download deste arquivo é de ",tempo)