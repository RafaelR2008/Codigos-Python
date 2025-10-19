pessoas = []
mulheres = []
soma = media = 0
while True:
    dados = {}
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while 'F' != dados['Sexo'] != 'M':
        dados['Sexo'] = input('Escreva apenas F para feminino e M para masculino: ').strip().upper()
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    soma += dados['Idade']
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
media = soma / len(pessoas)
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for p in mulheres:
    print(f'[{p}]', end=' ')
print('\nLista das pessoas que estão acima da média:')
for p in pessoas:
    if p['Idade'] >= media:
        print(f'    nome = {p["Nome"]}; sexo = {p["Sexo"]}; idade = {p["Idade"]}')
print('<< ENCERRANDO >>')
