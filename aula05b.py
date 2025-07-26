pokemon = int(input("Escolha o seu pokemon: \n1-Charmander \n2-Pikachu\n3-Bulbasaur\n"))

match pokemon:
    case 1:
        print("Você escolheu um pokemon do tipo Fogo! 🔥")
    case 2:
        print("Você escolheu um pokemon do tipo Elétrico! ✨")    
    case 3:
        print("Você escolheu um pokemon do tipo Planta! 🌱")    
    case 4:
        print("Você não tem esse pokemon ainda! 😅")     