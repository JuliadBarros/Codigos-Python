import os
from time import sleep


def exibe_menu():
    os.system('cls')
    print("\n===== Agenda telefonica =====")
    print("ad - Adicionar  contato\n"
          "ap - Apagar contato\n"
          "vc - Ver todos os contatos\n"
          "ps - Pesquisar por um contato\n"
          "ex - Sair")
    print("-----------------------------")


def adiciona_contato():
    print("====== Novo contato ======")

    # Adicionando os dados a um dicionário
    nome = str(input("Nome do contato: ")).strip()
    tel = int(input("Telefone: "))
    email = str(input("E-mail: ")).strip()

    contato = {
        'Nome': nome,
        'Telefone': tel,
        'E-mail': email
    }

    # Colocando esse dicionário em uma lista, onde terá todos os contatos salvos futuramente
    todos_contatos.append(contato)

    print("\n>>> Contato salvo!\n")
    sleep(1)

    # Salvar um novo contato ou voltar para o menu
    while True:
        print("ad - Adicionar um novo contato\n"
              "vl - Voltar para menu")
        print("------------------------------")

        opcao = str(input("Selecione: ")).strip()

        if opcao == "ad":
            # limpar terminal antes de chamar a função adiciona_contato() novamente
            os.system('cls')
            return adiciona_contato()
        elif opcao == "vl":
            break
        else:
            print("Opção inválida!")


def apaga_contato(contatos):
    print("====== Excluir contato ======")

    # Verificando se tem algum contato salvo na lista, se não tiver, não temos como excluir o contato
    if not contatos:
        print("\nSem contatos salvo!\n")

        return

    nome_excluir = str(input("Digite o nome do contato que deseja excluir: ")).strip().lower()

    for i, contato in enumerate(contatos):
        if nome_excluir == contato['Nome'].lower():
            print(f"\n>>> {contato['Nome']} foi excluído dos contatos !\n")

            del contatos[i]
            sleep(1)
            
            break
    else:
        print("\n>>> Contato não encontrado!\n")


def exibe_lista_contatos(contatos):
    # Se não adcionar nenhum contato 1°, não terá contatos para exibir
    if not contatos:
        print("\nSem contatos salvo!\n")

    for contador in range(0, len(contatos)):
        print(f"===== Contato {contador+1} =====")
        print(f"Nome: {contatos[contador]['Nome']}")
        print(f"Telefone: {contatos[contador]['Telefone']}")
        print(f"E-mail: {contatos[contador]['E-mail']}")
        print("--------------------")


# Ficou bem parecido com a função de excluir contato, seguindo a mesma lógica
def pesquisar_contato(contatos):
    print("====== Pesquisar contato ======")

    # Verificando se tem algum contato salvo na lista, se não tiver, não temos como pesquisar o contato
    if not contatos:
        print("\nSem contatos salvo!\n")

        return

    procura_nome = str(input("Digite o nome do contato que deseja procurar: ")).strip()
    contato_encontrado = False

    # Vai percorrer por cada contato (com o nome, telefone e email)
    for contato in contatos:
        if procura_nome.lower() == contato['Nome'].lower():
            print(f"\n>>>Contato encontrado!\n"
                  f"\nNome: {contato['Nome']}\n"
                  f"Telefone: {contato['Telefone']}\n"
                  f"E-mail: {contato['E-mail']}")

            contato_encontrado = True
            break

    # Se contato_encontrado for falso
    if not contato_encontrado:
        print("\n>>>Contato não existe!\n")

    sleep(1)


todos_contatos = []

while True:
    exibe_menu()

    escolha_menu = str(input("Selecione: "))
    print("-----------------------------")
    print(escolha_menu)

    # Verificando o que o usuário quer fazer
    if escolha_menu == "ad":
        adiciona_contato()
    elif escolha_menu == "ap":
        apaga_contato(todos_contatos)
    elif escolha_menu == "vc":
        exibe_lista_contatos(todos_contatos)
    elif escolha_menu == "ps":
        pesquisar_contato(todos_contatos)
    elif escolha_menu == "ex":
        break
    else:
        print("\nOpção inválida! Tente novamente\n")
