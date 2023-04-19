frase = str(input("digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("temos um paindromo")
else:
    print("A frase digitada nn é um palidromo")