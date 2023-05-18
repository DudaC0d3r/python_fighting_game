def area(a, b):
    l = a * b
    print(f"A area de um terreno {a} x {b} é de {l}m². ")
    
print("controle de terrenos")
print("-" * 30)
larg = int(input("largura (m): "))
compri = float(input("comprimento (m)"))
area(larg, compri)