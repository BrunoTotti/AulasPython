#para criar uma variável não podemos começar com números 
# ou caracteres especiais. além disso palavras compostas 
# não podem ser separadas com espaço, para isso devemos 
# usar escrever usando letras maiúsculas (nomeComleto) 
# ou underline (nome_completo)
#
#Para armazenar um valor em uma variável, usamos o 
# simbolo de igualdade (=) 

nome = "Bruno" #tipo dessa variável é String
idade = 33 # tipo dessa variável é int 
altura = 1.70 #tipo dessa variável é float
sabado = True #tipo dessa variável é boolean

print("Nome: ", nome)
print(type(nome)) #aqui estou exibindo o tipo da variável nome

print("Idade: ", idade)
print(type(idade)) #aqui estou exibindo o tipo da variável idade

print("Altura: ", altura)
print(type(altura)) #aqui estou exibindo o tipo da variável altura

print("Sábado: ", sabado)
print(type(sabado)) #aqui estpu exibindo o tipo da variável sabado

#se fizermos uma retribuição ou seja, tentar guardar outro nome usando 
#o identificador de uma variável ja existente
#o valor guradado é peridido para que o outro seja armazenado
#isso significa que uma varável só pode armazenar um unico dado por vez
#mas se quisermos guardar um dado sem perder o anterior, basta criar 
#um novo identificador

nome1 = "Maria"
print("Nome: ", nome1)

#para entrada de dados nós utilizamos o comando input(), essa entrada
#precisa ser armazenada em uma variável para conseguirmos usar esse
#valor no nosso código
sentimento = input("Como você esta hoje? ")

print("Hoje você esta: ", sentimento)

nome_pessoa = input("Qual o seu nome? ")
#para saber a quantidade de caracteres em uma string 
#função len() 
quant_letras = len(nome_pessoa)
print('Seu nome tem', quant_letras, 'letras!')

anoAtual = 2025
idadeAtual = int(input("Qual ano você nasceu?: "))

resultadoIdade = (anoAtual - idadeAtual)
print("Você tem: ", resultadoIdade, "anos!")
