print("Bruno")
print("33 anos")
print("São Paulo")

print("_" * 80)

nome = "Bruno"
idade = 33
altura = 1.70
sabado = True

print("_" * 80)

print(type(nome))
print(type(idade))
print(type(altura))
print(type(sabado))

print("_" * 80)

print("Digite o seu filme favorito")
filme = input()
print("Seu filme favorito é: ", filme)

print("_" * 80)

print("Qual a sua cor favorita ?")
cor = input()
if cor == "azul":
    print("Que bom gosto!")
elif cor == "vermelho":
    print("Cor vibrante!")
else :
    print("Cor incomum!")        

print("_" * 80)

nome = input("Qual o seu nome?")
ano = int(input("Qual o seu ano de nascimento ?"))

if ano >= 2009:
    print("Ainda não pode votar!")
else: 
    print("Pode votar!")   