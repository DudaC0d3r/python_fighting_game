def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[o;31mERRO! digite um numero inteiro valido. \033[m")
        if ok:
            break
    return valor

n = leiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}")