def leiaInt(txt):
    while True:
        i = str(input(txt)).strip()
        if i.isnumeric():
            return int(i)
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar do número {n}')
