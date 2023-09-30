import random

contador_de_partidas = 0
vitorias = 0
derrotas = 0
empates = 0

while True:
    opcoes = {
        "Pe": "Pedra",
        "Pa": "Papel",
        "Te": "Tesoura"
    }

    escolha_computador = random.choice(list(opcoes.values()))

    print("======== Jokenpô ========\n"
          "Pe - Pedra\n"
          "Pa - Papel\n"
          "Te - Tesoura\n"
          "Ex - Sair")
    print("-------------------------")

    while True:
        escolha_usuario = str(input("Faça sua jogada: ")).strip().title()[:2]
        if not escolha_usuario.isalpha() or escolha_usuario not in opcoes.keys():
            print("Erro! Entrada inválida.")
            print("-------------------------")
        else:
            break

    print("-------------------------")
    print("======= Resultado =======")

    # Pedra
    if escolha_usuario == "Pe":
        if escolha_computador == "Pedra":
            empates += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Empate!")
        elif escolha_computador == "Papel":
            derrotas += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Perdeu!")
        elif escolha_computador == "Tesoura":
            vitorias += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Ganhou!")

    # Papel
    elif escolha_usuario == "Pa":
        if escolha_computador == "Pedra":
            vitorias += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Ganhou!")
        elif escolha_computador == "Papel":
            empates += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Empate!")
        elif escolha_computador == "Tesoura":
            derrotas += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Perdeu!")

    # Tesoura
    elif escolha_usuario == "Te":
        if escolha_computador == "Pedra":
            derrotas += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Perdeu!")
        elif escolha_computador == "Papel":
            vitorias += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Ganhou!")
        elif escolha_computador == "Tesoura":
            empates += 1
            print(f"Você: {opcoes[escolha_usuario]}\n"
                  f"PC: {escolha_computador}\n-> Empate!")

    # Saindo do jogo
    elif escolha_usuario == "Ex":
        print("Fim de Jogo!")
        print("===== Placar do jogo =====\n"
              f"Rodadas Jogadas: {contador_de_partidas}\n"
              f"Vitórias: {vitorias}\n"
              f"Empates: {empates}\n"
              f"Derrotas: {derrotas}\n"
              f"=========================")

        break

    print("-------------------------")
    contador_de_partidas += 1

