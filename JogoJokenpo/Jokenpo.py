import random
import os

def mostra_menu():
    print("======== Jokenpô ========\n"
          "Pe - Pedra\n"
          "Pa - Papel\n"
          "Te - Tesoura\n"
          "Ex - Sair")
    print("-------------------------")


def pega_escolha_usuario_computador(opcoes):
    # O computador não pode sortear Ex, então criamos um novo dicionário onde Ex não existe
    opcoes_sem_ex = {key: valor for key, valor in opcoes.items() if key != "Ex"}
    escolha_computador = random.choice(list(opcoes_sem_ex.values()))

    # Verificação e tratamento de entrada digitada pelo usuário
    while True:
        escolha_usuario = str(input("Faça sua jogada: ")).strip().title()[:2]
        if not escolha_usuario.isalpha() or escolha_usuario not in opcoes.keys():
            print("Erro! Entrada inválida.")
            print("-------------------------")
        else:
            break

    escolha_usario_computador = (escolha_computador, escolha_usuario)

    return escolha_usario_computador


def mostra_resultado():
    print("-------------------------")
    print("======= Resultado =======")
    print("-------------------------")


def verifica_partida(escolha_usario_computador, opcoes, placar):
    # escolha_usario_computador é uma tupla onde o 1° valor é a escolha do usuário, 2° valor é a escolha do computador
    escolha_computador = escolha_usario_computador[0]
    escolha_usuario = escolha_usario_computador[1]

    mostra_resultado()

    print(f"Você: {opcoes[escolha_usuario]}\n"
          f"PC: {escolha_computador}")

    # Saindo do jogo
    if escolha_usuario == "Ex":
        print("Fim de Jogo!")
        mostra_placar(placar)
    # Empatando o jogo
    elif escolha_usuario == escolha_computador:
        placar["Empates"] += 1
        print(" -> Deu Empate!")
    # Todos os casos de vitória
    elif (opcoes[escolha_usuario] == "Pedra" and escolha_computador == "Tesoura") or \
            (opcoes[escolha_usuario] == "Papel" and escolha_computador == "Pedra") or \
            (opcoes[escolha_usuario] == "Tesoura" and escolha_computador == "Papel"):
        placar["Vitorias"] += 1
        print(" -> Você Ganhou!")
    # Se não der nenhum, então perdeu
    else:
        placar["Derrotas"] += 1
        print(" -> Você Perdeu!")

    placar["Partidas"] += 1


def mostra_placar(placar):
    print("===== Placar do jogo =====\n"
          f"Rodadas Jogadas: {placar['Partidas']}\n"
          f"Vitórias: {placar['Vitorias']}\n"
          f"Empates: {placar['Empates']}\n"
          f"Derrotas: {placar['Derrotas']}\n"
          f"=========================")


def jogar():
    os.system('cls')

    # Configurações globais do jogo
    opcoes_de_jogo = {
        "Pe": "Pedra",
        "Pa": "Papel",
        "Te": "Tesoura",
        "Ex": "Sair"
    }
    placar_inicial = {
        "Partidas": 0,
        "Vitorias": 0,
        "Empates": 0,
        "Derrotas": 0
    }

    # Rodando o jogo
    while True:
        mostra_menu()
        escolha_usuario_computador = pega_escolha_usuario_computador(opcoes_de_jogo)

        verifica_partida(escolha_usuario_computador, opcoes_de_jogo, placar_inicial)

        if escolha_usuario_computador[1] == "Ex":
            break
