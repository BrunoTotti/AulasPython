ingresso = input("Olá, você tem ingresso ?: ").lower()

#o ".lower()" transforma a string toda para letras minúsculas
#0 ".upper()" transforma a string toda para letras maiúsculas 
if ingresso == "sim":
    print("Pode entrar, aproveite o filme!")
else :
    print("Desculpe, você precisa de um ingresso para entrar.")  