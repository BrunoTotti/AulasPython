pergunta = input("Você é estudante?\n").lower()

match pergunta:
    case "sim":
        print("Que bom, continue assim!")
    case "não":
        print("Sempre é tempo para aprender algo!")    
    case _:
        print("Não entendi!")
