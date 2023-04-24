num = (int(input("digite um numero:")),
      int(input("digite outro numero:")), 
      int(input("digite outro numero:")), 
      int(input("digite outro numero:")), 
      int(input("digite outronumero:")))
print(f"Vc digitou os valores {num}")
print(f"O valor 9 aparceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 aparceu na {num.index(3)+1}ª posição")
else:
    print(f"o valor 3 nn foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram ")
for n in num:
    if n % 2 == 0:
        print(n, end=' ')