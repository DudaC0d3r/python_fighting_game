print("{:=^40}".format(" LOJAS GUANABARA "))
preço = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão ''')
opçao = int(input("Qual é a opção?: "))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print("Sua compra sera pacelada em 2x de R${: .2f} SEM JUROS".format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparç = int(input("Quantas parcelas?"))
    parcela = total / totparç 
    print("Sua compra sera pacelada em {}x de R${: .2f} COM JUROS".format(totparç, parcela))
print("sua compra de R${: .2f} vai custar R${: .2f} no final. ".format(preço, total))