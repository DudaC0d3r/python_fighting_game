numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("O valor adicionado com sucesso... ")
    else:
        print("O valor duplicado! nn vou adicionar... ")
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print("-=" * 30)
numeros.sort()
print(f"Voce digitou os valores {numeros}")       