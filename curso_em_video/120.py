def leiaint():
    while True:
        i = str(input("digite um numero inteiro: "))
        if i.isnumeric():
            for l in range(len(i)):
                if i[l] == ".":
                     print("erro! float tente novamente")
                if l + 1 == len(i):
                    
                    print("o numero inteiro digtado foi {}".format(i))
                    return False
        else:
             print("erro! str tente novamente")
             
             
def leiafloat():
    while True:
        f = float(input("digite um real: "))
        if f.isnumeric():
            for q in range(len(f)):
                if f[q] == ".":
                    print("erro! float tente novamente")
                if q + 1 == len(f):
                    
                    print("o numero real digitado foi {}".format(f))
                    return False
        else:
            print("erro! float tente novamente")

leiaint()
