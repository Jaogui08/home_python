tentativas = 0
maxtentativas = 4

while tentativas < maxtentativas:
    user = input("\nInforme o seu usuário: ")

    if user == "jaogui":
        print("Usuário correto")
        break
    else:
        print("Usuário incorreto")
        tentativas += 1

if tentativas == maxtentativas:
    print("Limite de tentativas atingido, encerrando o programa")
    exit()

tentativas = 0

while tentativas < maxtentativas:
    senha = input("\nInforme a sua senha: ")

    if senha == "1234":
        print("Bem-vindo ao sistema SENAI")
        break
    else:
        print("Senha incorreta")
        tentativas += 1

if tentativas == maxtentativas:
    print("Limite de tentativas atingido, encerrando o programa")
    exit()