def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :para situ: valor opcional, indicando se deve ou nn adicionar a situação
    :print: mostra varias informacões sobre a situação da turma.
    """
    m = sum(nota) / len(nota)
    mx = max(nota)
    mn = min(nota)
    situ = ""
    mostra = "situaçao: "
    tot = len(nota)
    
    if m >= 5:
        situ = "rezoavel"
    elif m >= 7:
        situ = "boa"
    else:
        situ = "ruim"
        
    if sit == True:
        mostra = mostra + situ
    
    print("total: {}, maior: {}, menor: {}, media: {}, {}".format(tot, mx, mn, m, mostra))
        
    
notas(5.5, 9, 10, sit=True)
help(notas)
