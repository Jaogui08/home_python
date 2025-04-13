num = int(input("Informe o número para saber o fatorial: "))

fat = 1
i = num

while (i >= 1):
    fat = fat*i
    i-=1

print(f"\nO fatorial de {num} é igual a: {fat}")