import moeda

p = float(input("Digite um preço: R$ "))
print(f"A metade de {p} é {moeda.metade}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10)}")
