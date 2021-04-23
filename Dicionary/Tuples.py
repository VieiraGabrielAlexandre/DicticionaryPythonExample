usuarios = {}

emails = ["teste@teste.com", "teste2@teste.com"]

tuple = list(enumerate(emails))

for chave in range(0, len(tuple)):
    print("Email: ", tuple[chave][1])
    usuarios[tuple[chave]] = [input("Digite o nome: "), input("Digite o nivel: ")]

for (chave, dado) in usuarios.items():
    print("Usuario:", chave[0])
    print("Email:", chave[1])
    print("Nome:", dado[0])
    print("Acesso:", dado[1])