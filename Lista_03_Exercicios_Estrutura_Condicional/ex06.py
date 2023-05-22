#Elaborar um programa que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

#Entradas: nome, sexo, estadoCivil
#Saídas: tempoCasada

print("Programa que informa se a pessoa é casada e o tempo de casada")
nome = input("Informe o nome da pessoa: ")
sexo = input("Informe se o sexo da pessoa é 'F' ou 'M': ")
estadoCivil = input("Informe se o estado civil da pessoa é 'SOLTEIRA' ou 'CASADA': ")

if (sexo == "F"):
    if (estadoCivil == "CASADA"):
        tempoCasada = input("Informe o tempo de casada em anos: ")