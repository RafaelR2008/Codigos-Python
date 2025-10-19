while True:
    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}')
    esc = input('Deseja continuar? [S/N]: ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Digite apenas S para sim ou N para não. Deseja continuar? [S/N]: ').strip().upper()
    if esc == 'N':
        break
print('Finalizando...')
