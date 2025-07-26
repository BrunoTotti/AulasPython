#operadores relacionais
#> (maior que)
print("5 > 2?",5 > 2)
#< (menor que)
print("6 < 3?",6 < 3)
# >= (maior ou igual)
print("6 >= 4?", 6 >= 4)
#<= (menor ou igual)
print("9 <= 10?" ,9 <= 10)
# == (igual)
print("9==9?", 9 == 9)
# != (diferente)
print("9 != 9?", 9 != 9)

print("_" * 80)

#operadores lógicos
# and (E) --> Eu preciso que todas aminhas operações retornem um número verdadeiro
print("5 == 5 and 10 == 9?", 5 == 5 and 10 == 9)
print("'Maria' == 'Maria' and 3 == '3'?", 'Maria' == 'Maria' and 3 == '3')

# or (ou) --> Eu precis oque pelo menos UMA das operações seja verdadeiro
print("'Maria' == 'João' or 5 != 10?", 'Maria' == 'João' or 5 != 10)
print("6 > 2 or 9 != 6?", 6 > 2 or 9 != 6)
print("9 > 15 ou 6 == 6?", 9 > 15 or 6 == 6)

print("_" * 80)

idadeMaria = 45
idadeJoao = 15

#condicionais: criam caminho no codigo conforme condição, ou seja, apenas uma coisa acontece dependendo da minha sentença
#SE a idade da Maria for maior que a idade do João

if idadeMaria > idadeJoao :
    #mostra que Maria é mais velha
    print("Maria é mais velha que o João")
#Senão vai mostrar que João é mais velho
else: 
    print("João é mais velho que a Maria")   

print("_" * 80)

print("Bem vindo ao curso de Python \n Para se inscrever os requisitos são:")
print("1 - Ter mais de 14 anos")
print("2 - Ter terminado o ensino fundamental 1")

nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade ?"))
fund = input("Você terminou o Ensino Fundamental 1? \n 1 - sim \n 2 - não") 

if idade > 14 and fund == '1':
    print(nome, 'sua matrícula foi realizada com sucesso!')
else: 
    print(nome, 'sua matrícula não pode ser realizada!')    