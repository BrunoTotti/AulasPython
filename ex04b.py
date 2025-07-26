
 #Atividade em Dupla 


KWH = float(input('Qual o KWH consumido no mês? \n'))

if KWH <= 100 :
    print('Consumo baixo. Parabéns pela economia!')
elif KWH <= 300 :
    print('Consumo médio. Fique atento.')
else :
    print('Alerta: Consumo alto. Tente reduzir!')


print('_' * 100 )

#Atividade 02 

porcentagem_1 = 0.1
porcentagem_2 = 0.05

valor = float(input('Qual o valor da sua compra?'))
cupom = input('Você possui cupom de desconto?')
if cupom == 'sim' and valor >= 100:
    print('Parabéns você ganhou um desconto de 10%\n')
    print('O valor da sua compra será de ', valor - (valor * porcentagem_1), 'reais')
elif cupom == 'sim' and valor < 100:
    print('Parabéns você ganhou um desconto de 5%\n')
    print('O valor da sua compra será de', valor - (valor * porcentagem_2), 'reais')
else :
    print('infelizmente você não tera desconto!')


print('_' * 100 )

#Atividade 03

idade = int(input('Qual a sua idade?\n'))
renda = float(input('Qual o valor da sua renda mensal?\n'))

if idade >= 18 and renda >= 2000:
    print('Você pode solicitar o financiamento.')
elif idade >= 18 and renda < 2000:
    print('Renda insuficiente!')
else :
    print('Você precisa ter pelo menos 18 anos')

print('_' * 100 )

#Atividade 04

produto = int(input('Qual a quantidade deste produto no estoque?\n'))

if produto < 1 :
    print('Produto esgotado')
elif produto <= 10:
    print('Estoque baixo. Reponha o quanto antes.')
else :
    print('Estoque em nível adequado.')

print('_' * 100 )

#Atividade 05

horas = int(input('Que horas são?\n'))

if horas >= 9 and horas <= 12:
    print('Reunião agendada para o período da manhã.')
elif horas >= 13 and horas <= 18:
    print('Reunião agendada para a tarde.')
else :
    print('Horário inválido. Reuniões só podem ser marcadas entre 9h e 18h.')



#Atividade em dupla
#Matheus Souza
#Bruno de Souza Farias