# Será responsável apenar por exibir o tabuleiro atual na tela a cada jogada
def exibe_tabuleiro(tabuleiro_atualizado):
    print("-----------------")
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f"| {tabuleiro_atualizado[linha][coluna]} |", end=" ")
        print()
        print("-----------------")


# Pegamos a posição que será jogada e verificamos se essa posição já está ocupada
def pega_posicao_jogada(tabuleiro, icone):
    posicao_jogada = int(input(f"({icone}) Selecione a posição que quer jogar: "))

    # Se não tiver o número em nenhuma das 3 listas, então tem um icone no lugar, é uma posicao já ocupada
    if posicao_jogada not in tabuleiro[0] and posicao_jogada not in tabuleiro[1] and posicao_jogada not in \
            tabuleiro[2]:
        print("Posição já ocupada, Selecione uma lugar válido")
        pega_posicao_jogada(tabuleiro, icone)
    # Se o número tiver, então é onde o icone deve ocupar
    else:
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if tabuleiro[linha][coluna] == posicao_jogada:
                    tabuleiro[linha][coluna] = icone
                    break  # se não tiver o break vai rodar o loop desnecessariamente


# Todos os casos de vitória do jogo, são 8 no total
def verifica_ganhou(verifica_tab):
    ganhou = False

    # Verificando se fez uma sequencia pelas diagonais ( \ ) ou ( / )
    if verifica_tab[0][0] == verifica_tab[1][1] == verifica_tab[2][2] or \
       verifica_tab[0][2] == verifica_tab[1][1] == verifica_tab[2][0]:
        ganhou = True

    # Verificando se fez uma sequencia pelas linhas (horizontal) e pelas colunas (vertical)
    for lin_col in range(0, 3):
        if verifica_tab[lin_col][0] == verifica_tab[lin_col][1] == verifica_tab[lin_col][2] or \
           verifica_tab[0][lin_col] == verifica_tab[1][lin_col] == verifica_tab[2][lin_col]:
            ganhou = True

    return ganhou


def jogar():
    joga_segundo = "0"
    joga_primeiro = "x"
    pontuacao_0 = 0
    pontuacao_x = 0

    while True:
        tabuleiro = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]

        exibe_tabuleiro(tabuleiro)

        for rodada in range(1, 10):
            # Para saber qual o icone que deve jogar na rodada
            if rodada % 2 == 0:
                icone = joga_segundo  # na 1° partida 'O' Joga 2°
            else:
                icone = joga_primeiro  # na 1° partida 'x' Joga 1°

            pega_posicao_jogada(tabuleiro, icone)

            exibe_tabuleiro(tabuleiro)
            resultado = verifica_ganhou(tabuleiro)

            if resultado:
                print(f"Fim de jogo! - {icone} - ganhou")

                # Se o 'x' ganhar, apenas acresta a pontuação para ele, por padrão já é o 'x' que começa jogando
                if icone == "x":
                    pontuacao_x += 1
                # Se a 'O' Ganhar, ele deve começar jogando na próxima partida
                else:
                    pontuacao_0 += 1
                    joga_primeiro = icone
                    joga_segundo = "x"

                break

        opcao = str(input("Deseja jogar outra partida? [S/N]: ")).strip().upper()[:1]

        if opcao == "N":
            print(f"- x - ganhou {pontuacao_x}")
            print(f"- O - ganhou {pontuacao_0}")
            break


jogar()
