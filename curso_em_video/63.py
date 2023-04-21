print("Grador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= 10:
        print("{} ->".format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos vc quer mostrar a mais? "))
print("Progressão fializada com {} termos mostrados.".format(total))