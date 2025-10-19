from datetime import date
q = 0
print('Digite o ano de nascimento de 7 pessoas')
for i in range(0,7):
    ano = int(input('Ano: '))
    idade = date.today().year - ano
    if idade >= 21:
        q += 1
print(f'Entre os anos digitados, {q} pessoas já são maior de idade, e as outras {7 - q} não')