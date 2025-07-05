v = 1

while v <= 3: #enquanto V for menor ou igual a 3, esses comandos vão se repetir, enquanto a condição for true
    print("O valor de V é ", v)
    v = v+1 #somo mais 1 ao valor de V para que esse loop não seja infinito, ja que le pode ser maior que 3

    print("_" * 50)

    '''
    Imagine que você esta criando um contador numérico e esse contador deve perguntar ao usuario em qual valor ele parar
    '''

parada = int(input("Digite o valor que deseha contar: "))
contador = 1

while contador <= parada:
    print(contador)
    contador = contador + 1

'''
Imagine que você ta criando uma aposta para ver quem vai ser o time que vai ganhar o mundial
'''   
time = input("Digite o nome do time que deseja apostar:").upper()

while time == 'PALMEIRAS':
    print("Palmeiras não tem mundial, escolha outro time!")
    time = input("Digite novamente ").upper()
else:
    print("Boa sorte na sua aposta!")    