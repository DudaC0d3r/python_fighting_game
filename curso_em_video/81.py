expre = str(input("Digite uma expressão: "))
pilha = []
for exp in expre:
    if exp == "(":
        pilha.append("(")
    elif exp == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("expressão valida! ")
else:
    print(" sua expressão esta errada! ")