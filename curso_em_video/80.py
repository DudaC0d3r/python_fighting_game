numeros = list()
pares = list()
impares = ()
while True:
    numeros.append(int(input("Digite um numero:")))
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("-=" * 30)
print(f"A lista completa é {numeros}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")