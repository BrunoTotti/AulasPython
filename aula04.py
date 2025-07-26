#Quando temos mais de duas cerificações a serem feitas, usamos as condicionais compostas
# (elif) elas servem oara criar novas condições no código, ou seja, novos "caminhos".

#Exemplo:
#Calculadora de frete:
#Crie um programa que pergunte a distância para entrega em quilômetros.
#Se for até 10km, o frete custa R$ 5.
#Se for entre 10.1 e 30km, custa R$ 10.
#Acima de 30km, o frete é R$20.
#exiba o valor do frete de acordo com a distância

km = float(input("Qual a distância em km?: "))

if km <= 10:
    print("Esse frete custa R$ 5,00!")
elif km <= 30:
    print("Esse frete custa R$ 10,00!")
else:
    print("Esse frete custa R$ 20,00!")        
