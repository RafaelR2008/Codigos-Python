from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print(f'Você tem {idade} anos')
if idade <= 9:
    print('Sua categoria: MIRIM')
elif idade <= 14:
    print('Sua categoria: INFANTIL')
elif idade <= 19:
    print('Sua categoria: JUNIOR')
elif idade <= 25:
    print('Sua categoria: SÊNIOR')
else:
    print('Sua categoria: MASTER')
