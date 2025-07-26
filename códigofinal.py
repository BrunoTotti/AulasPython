jogos = []
participantes = []

print('\n\t\tSejam bem-vindos participantes. ')
totalJogos = int(input("\tDigite o número de jogos que terá no festival:  "))

print('\n\tCadastre abaixo os jogos participantes. ')

contJogos = 0
while contJogos < totalJogos:
    nomeJogo = input(f"\nNome do {contJogos + 1}º jogo (ou 'fim' para parar):  ")

    if nomeJogo.lower() == "fim" and contJogos > 0:
        print("\nCadastro encerrado antes do previsto.")
        break
    elif nomeJogo.lower() == "fim" and contJogos == 0:
        print("⚠ Você deve cadastrar pelo menos 1 jogo antes de parar!")
        continue

    jogos.append(nomeJogo)
    numJogadores = int(input("Quantos jogadores estão inscritos no jogo " + nomeJogo + "? "))
    participantes.append(numJogadores)
    contJogos += 1

print("\n\t\tInformação dos jogos cadastrados. \n")
for jogo in jogos:
    print("Jogo cadastrado: " + jogo)

print("__" * 25)

for jogo, numJogadores in zip(jogos, participantes):
    print(jogo + " tem " + str(numJogadores) + " jogadores.")

print("__" * 25)

totalJogadores = 0
contador = 0
while contador < len(participantes):
    totalJogadores += participantes[contador]
    contador += 1

print("Total de jogadores no festival: " + str(totalJogadores))

print("\n\t\tRepresentação dos jogadores: \n")
for jogo, numJogadores in zip(jogos, participantes):
    representacao = '🎮' * numJogadores
    print(jogo + ": " + representacao)

maiorJogo = jogos[0]
maiorQuant = participantes[0]

contador = 1
while contador < len(jogos):
    if participantes[contador] > maiorQuant:
        maiorQuant = participantes[contador]
        maiorJogo = jogos[contador]
    contador += 1

print("\nJogo com mais jogadores: " + maiorJogo + " (" + str(maiorQuant) + " jogadores)")

print("\n\n\t\tBoa sorte a todos!")