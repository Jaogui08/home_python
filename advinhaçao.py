import random

numsecret = random.randint(1,30)

print("Bem-vindo ao jogo da advinhação, tente advinhar o número entre 1 a 30")

while True:
    tentativa = int(input("\nDigite o seu palpite: "))

    if (tentativa<numsecret):
        print("Muito baixo, tente novamente")
    elif (tentativa>numsecret):
        print("Muito alto, tente novamente")
    else:
        print("Parabéns, você acertou")
        break