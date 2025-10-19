mais18 = homens = mulheresNV = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [F/M] ').strip().upper()
    while 'F' != sexo != 'M':
        sexo = input('Escreva apenas F para feminino e M para masculino: ').strip().upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresNV += 1
    print('-'*30)
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Escreva apenas S para sim ou N para não: ').strip().upper()
    if esc == 'N':
        print(f'{'FIM DO PROGRAMA':=^30}')
        break
print(f'Você cadastrou ao todo {mais18} pessoas com mais de 18 anos.')
print(f'Temos ao todo {homens} homens cadastrados.')
print(f'E há {mulheresNV} mulheres com menos de 20 anos.')
