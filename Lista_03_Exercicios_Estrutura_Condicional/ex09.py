'''
Elaborar um programa que calcule o que deve ser pago
por um produto, considerando o preço normal de etiqueta
e a escolha da condição de pagamento. Utilize os códigos
da tabela a seguir para ler qual a condição de pagamento
escolhida e efetuar o cálculo adequado.

Código para condição de pagamento:
1. À vista em dinheiro ou cheque, recebe 10% de desconto
2. À vista no cartão de crédito, recebe 15% de desconto
3. Em duas vezes, preço normal de etiqueta sem juros
4. Em duas vezes, preço normal de etiqueta mais juros de 10%
'''

print("Progrma para verificar condição de pagamento")

preco = float(input("Digite o preço do produto: "))
cond = int(input('''
Digite '1' para pagamento à vista em dinheiro ou cheque, recebe '10%' de desconto
Digite '2' para pagamento à vista no cartão de crédito, recebe '15%' de desconto
Digite '3' para pagamento em duas vezes, preço normal de etiqueta sem juros
Digite '4' para pagamento em três vezes, preço normal de etiqueta mais juros de '10%' 
Selecione a opção desejada: '''))
if (cond >= 1) and (cond <= 4):
    if (cond == 1): 
        preco = preco * 0.9
    elif (cond == 2):
        preco = preco * 0.85
    elif (cond == 3):
        preco = preco * 1 
    elif (cond == 4):
        preco = preco * 1.1
    print("O preço final do preoduto é: R$ %.2f" % preco)
else:
    print("Valor inválido")
