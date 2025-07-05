# Exercício 1 – Chat do atendimento automático

opcao = input("O que deseja fazer? \n1-Fazer Pedido \n2-Ver o cardápio\n3-Falar com atendente") 
match opcao:
    case "1":
        print("Faça o pedido!")
    case "2": 
        print("Escolha algo do cardápio")
    case "3":
        print("Entre em contato com o atendente")  
    case _:
        print("Opção Inválida")    

# Exercício 2 – Café na medida certa

tempo = int(input("Qual a temperatura atual ?"))
if tempo < 18:
   print("O que você acha de um cappuccino quente?")
elif tempo <= 28:
    print("Café gelado")
else:
    print("Água mesmo!")

# Exercício 3 – Playlist do humor
          
humor = input("Como você esta se sentindo? ").lower()
match humor:
    case "feliz":
        print("O que você acha de ouvir Sunflower - Post Malone")
    case "triste":
        print("What was i made for? - Billie Eillish")
    case "cansado":
        print("Dealer - Lana Del Rey")
    case "animado":
        print("Demolisher - Slaughter to Prevail")  
    case _:
        print("Não conheço essa emoção!")
          

# Exercício 4 – Bilhete do transporte

idade = int(input("Sistema de bilhete eletrônico: Qual a sua idade ? "))

if idade <= 5:
    print("Gratuito")
elif idade <= 59:
    print ("Paga R$4,40")
else:
    print("Gratuito - 60+ ")

# Exercício 5 – Pedido no terminal do fast food

combo = input("Qual combo você deseja ? \n C1 - Hambúrguer + batata \n C2 - Nuggets + suco \n C3 - Vegano + água \n").upper()
match combo:
    case "C1":
        print("Hambúrguer Artesanal 200g + Batata Rústica 200g")
    case "C2":
        print("Nuggets 10 unidades + Suco Natural 300ml")
    case "C3":
        print("Hambúrguer Vegano de Falafel  + Água Mineral 300ml")
    case _:
        print("Opção inválida!")

# Exercício 6 – Verificando o celular do colega

bateria = int(input("Qual o percentual da sua bateria ? "))
if bateria < 20:
    print("Colocar no carregador agora!")
elif bateria <= 50:
    print("Dá pra usar mais um pouco!")
elif bateria <=100:
    print("Tá tranquilo!")
else:
    print("Opção inválida!")
