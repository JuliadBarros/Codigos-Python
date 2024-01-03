import re


def validar_telefone(telefone):
    # Usando uma expressão regular para verificar o formato do telefone
    padrao = re.compile(r'\(\d{2}\) \d \d{4}-\d{4}')

    # Verificando se o telefone corresponde ao padrão
    if padrao.match(telefone):
        return True
    else:
        return False


# Exemplo de uso
while True:
    telefone_usuario = input("Digite o telefone (no formato (xx) x xxxx-xxxx): ")

    if validar_telefone(telefone_usuario):
        print("Telefone válido! Obrigado.")
        break
    else:
        print("Telefone inválido. Por favor, tente novamente.")
