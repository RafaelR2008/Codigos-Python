from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - ano
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
