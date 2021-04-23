def perguntar():
    return input("O que deseja realizar ?\n" +
                 "<I> - Para INSERIR um usuario\n" +
                 "<P> - Para PESQUISAR um usuario\n" +
                 "<E> - Para EXCLUIR um usuario\n" +
                 "<L> - Para LISTA um usuario: \n").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = {
        "nome": input("Digite o nome: "),
        "data": input("Digite a ultima data de acesso: "),
        "acesso": input("Qual a ultima estacao acessada: ")
    }

    return dicionario

def pesquisar(dicionario):
    search = input("Digite o nome a ser pesquisado: ")

    for elemento in dicionario:
        if search == dicionario[elemento]["nome"]:
            print(dicionario[elemento])

def excluir(dicionario):
    exclui = input("Digite o login para excluir: ").upper()

    for elemento in dicionario:
        if exclui == elemento:
            dicionario.pop(elemento)
            print("Removido")