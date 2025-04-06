print("Bem-vindo a calculadora em python\n")

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

print("Agora escolha a operação para ser feita:")
print("1 para soma")
print("2 para subtração")
print("3 para multiplicação")
print("4 para divisão")

op = float(input("Digite a operação desejada: "))

if op == 1:
    result = n1+n2
    print(f"O resultado é: {result}")
elif op == 2:
    result = n1-n2
    print(f"O resultado é: {result}")
elif op == 3:
    result = n1*n2
    print(f"O resultado é: {result}")
elif op == 4:
    if n2 != 0:
        result = n1/n2
        print(f"O resultado é: {result}")
    else:
        print("Divisão por zero não é permitido")
else:
    print("Opção inválida, tente novamente")