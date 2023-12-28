# Fazendo a importação dos outros códigos
from JogodaVelha import JogoVelha
from JogoJokenpo import Jokenpo


def exibe_menu():
    print("=-=-=-= Menu de Jogos =-=-=-=")
    print("1 - Jokenpô\n"
          "2 - Jogo da velha\n"
          "0 - Sair")


def verifica_entrada_usuario():
    lista_opcoes = ("1", "2", "0")
    opcao = str(input("Escolha um jogo: ")).strip()[:1]

    if opcao in lista_opcoes:
        return opcao
    else:
        print("Digite um valor válido! Tente novamente")
        # se a opção for invalida vai chamar a própria função novamente
        return verifica_entrada_usuario()


def escolhendo_jogo():
    exibe_menu()
    escolha_usuario = verifica_entrada_usuario()

    # Iniciando o jogo a partir da opção que foi escolhida
    if escolha_usuario == "1":
        Jokenpo.jogar()
        return escolhendo_jogo()
    elif escolha_usuario == "2":
        JogoVelha.jogar()
        return escolhendo_jogo()
    elif escolha_usuario == "0":
        return


escolhendo_jogo()
