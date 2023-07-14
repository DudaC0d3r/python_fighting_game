
def repete():
    print("=-==-=-==-=-==-=-==-=-==-=-==-=")
    sleep(1)
    print(f"    [ {n1} ] somar")
    print(f"    [ {n2} ] multiplicar")
    print(f"    [ {n3} ] maior")
    print(f"    [ {n4} ] novos números")
    print(f"    [ {n5} ] sair do programa")

from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5

print(f"    [ {n1} ] somar")
print(f"    [ {n2} ] multiplicar")
print(f"    [ {n3} ] maior")
print(f"    [ {n4} ] novos números")
print(f"    [ {n5} ] sair do programa")

while True:
    opcao = int(input("Qual é a sua opção? "))
    if opcao == n1:
        soma = num1 + num2
        print(f"A soma entre {num1} + {num2} é {soma}")
        repete()
    elif opcao == n2:
        produto = num1 * num2
        print(f"O resultado de {num1} x {num2} é {produto}")
        repete()
    elif opcao == n3:
        if num1 > num2:
            print(f"Entre {num1} e {num2} o maior valor é {num1}")
        elif num2 > num1:
            print(f"Entre {num1} e {num2} o maior valor é {num2}")
        repete()
    elif opcao == n4:
        print("Informe os números novamente:")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
        repete()
    elif opcao == n5:
        print("Finalizando...")
        print("=-==-=-==-=-==-=-==-=-==-=-==-=")
        sleep(1)
        print("Fim do programa. Volte sempre")
        break
    elif n1 > opcao > n5:
        print("Opção inválida. Tente novamente")
        repete()