import random

print("Bem-vindo ao dado virtual em Python, siga as instruções abaixo:")

while True:
    esc = int(input("\n1 - jogar dado / 2 - encerrar "))

    if esc == 1:
        facedado = random.randint(1,6)
        print(f"O lado jogado foi: {facedado}")
    elif esc == 2:
        print("Fechando o sistema..")
        break
    else:
        print("Número inválido")