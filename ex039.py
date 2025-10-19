from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print(f'Você tem {idade} anos')
if idade < 18:
    print(f'Faltam {18 - idade} anos para o seu alistamento')
elif idade == 18:
    print('Está na hora do seu alistamento!')
else:
    print(f'Já se passaram {idade - 18} anos desde o seu alistamento')
