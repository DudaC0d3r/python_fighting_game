from time import sleep

def contador(i, f, p):
    print("-=" * 30)
    print(f"Contagem de {i} ate {f} de {p}")
    sleep(2.5)
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")

contador(1, 10, 1)
contador(10, 0 ,2)
print("-=" * 30)
print("Agora é sua vez de personalizar a contagem ")
ini = int(input("Inicio: "))
fim = int(input("fim:    "))
pas = int(input("Passo:  "))
contador(ini, fim, pas)