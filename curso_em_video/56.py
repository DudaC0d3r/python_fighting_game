maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input("Qual é o peso da {} pessoa?".format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("o maior peso é {}kg".format(maior)) 
print("o menor peso é {}kg".format(menor)) 