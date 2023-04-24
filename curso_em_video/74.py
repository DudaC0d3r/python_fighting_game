from random import randint
#es1 = ("escolha o primeiro numero:")
#es2 = ("escolha o segundo numero:")
#es3 = ("escolha o terceiro numero:")
#es4 = ("escolha o quarto numero:")
#es5 = ("escolha o quinto numero:")
#escolha = [es1, es2, es3, es4, es5]
maior = 0
menor = 0
escolha = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)
print(escolha)
print(f"O maior valor sorteado foi {max(escolha)}")
print(f"O menor valor sorteado foi {min(escolha)}")