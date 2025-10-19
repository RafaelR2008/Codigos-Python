esc = ''
maior = menor = soma = cont = 0
while esc != 'N':
    n = int(input('Número: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    soma += n
    esc = input('Deseja continuar? [S/N] ').strip().upper()
    while 'N' != esc != 'S':
        print('Digite apenas S ou N')
        esc = input('Deseja continuar? [S/N] ').strip().upper()
media = soma / cont
print(f'O maior valor lido foi: {maior}')
print(f'O menor valor lido foi: {menor}')
print(f'A média de todos os valores lidos é: {media:.2f}')
