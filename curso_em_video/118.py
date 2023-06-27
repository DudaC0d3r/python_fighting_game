def ficha(jogo="desconhecido", gol=0):
    print(f"O jogador {jogo} fez {gol} gol(s) no campeonato. ") 
    
j = str(input("Nome do jogador:"))
g = str(input("Numero de Gols: "))
if g.isnumeric() and len(j) > 0:
    ficha(j, g)
else:
    ficha()