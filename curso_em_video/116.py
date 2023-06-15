def notas(*n, sit=False):
    '''
    -> Funçao para analizar notas e situaçoes de varios alunos.
    :parem n: o numero a ser calculado.
    :param sit: (opcional) indicando se deve ou nn adicionar a situaçao
    :return: dicionario com varias informaçoes sobre a situaçao da turma.
    '''
    
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'boa'
        elif r["media"] >= 5:
            r['situaçao'] = 'razoavel'
        else:
            r['situaçao'] = 'ruim'
    return r

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
    