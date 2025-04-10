saldo = 1000.0

while True:
    senha = input("\nBem-vindo ao caixa eletronico, digite sua senha para continuar: ")

    if senha == "1234":
        print("Senha correta")
        break
    else:
        print("Senha inválida, tente novamente")

while True:
    print("\n1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        print(f"Seu saldo atualmente é de: R${saldo:.2f}")

    elif opc == "2":
        try:
            deposito = float(input("Escolha o valor para depositar: "))
            if deposito <= 0:
                print("Quantia selecionada inválida")
            else:
                saldo += deposito
                print("Depósito realizado com sucesso")
                print(f"Novo saldo: R${saldo:.2f}")
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opc == "3":
        try:
            saque = float(input("Informe o valor para sacar: "))
            if saque > saldo or saque <= 0:
                print("Quantia selecionada inválida")
            else:
                saldo -= saque
                print("Saque realizado com sucesso")
                print(f"Novo saldo: R${saldo:.2f}")
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opc == "4":
        print("Fechando o sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")