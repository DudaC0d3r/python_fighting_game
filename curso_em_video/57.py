somaidade = 0
mediaidade = 0
nomevelho = ''
totmulher = 0
maioridadehomen = 0
for p in range(1, 5):
    print(" ------- {}ª pessoa ------".format(p))
    nome = str(input("nome:")).strip()
    idad = int(input("idade: "))
    sexo = str(input(" sexo [M/F]: ")).strip()
    somaidade += idad
    if p == 1 and sexo in "Mm":
        maioridadehomen = idad
        nomevelho = nome
    if sexo in "Mm" and idad > maioridadehomen:
        maioridadehomen = idad
        nomevelho = nome
    if sexo in "Ff" and idad < 20:
        totmulher += 1
mediaidade = somaidade / 4
print("A media de idade do grupo é de {} anos".format(mediaidade))
print("O homen mais velho tem {} anos e se chama {}".format(maioridadehomen, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher))