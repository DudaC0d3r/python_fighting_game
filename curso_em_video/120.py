def leiaint():
    while True:
        i = str(input("digite um numero inteiro: "))
        if i.isnumeric():
            for l in range(len(i)):
                if i[l] == ".":
                     print("erro! float tente novamente")
                if l + 1 == len(i):
                    
                    print("entrou")
                    return False
        else:
             print("erro! str tente novamente")
def leiafloat():
    while True:
        f = str(input())
leiaint()