n = int(input('1º número: '))
cont = 0
s = 0
i = 2
while n != 999:
    cont += 1
    s += n
    n = int(input(f'{i}º número: '))
    i += 1
print(f'Você digitou {cont} números')
print(f'A soma de todos os números digitados é: {s}')
