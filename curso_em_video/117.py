def fatorial(n, show=True):
    """""
    -> calcule o fatorial de um numero.
    :parem n: o numero a ser calculado.
    :param show: (opcional) Mostrar ou nn a conta.
    :return: o valor do fatorial de um numero n.
    """""
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')             
        f *= c
    return f
    
print(fatorial(5, show=True))