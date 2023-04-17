from datetime import date
Ano_nascimento = int(input('Em que ano você nasceu? '))
Ano_atual = date.today().year
idade = Ano_atual - Ano_nascimento
if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f"""Você tem {idade} anos,
Logo sua categoria é: {categoria}!""")