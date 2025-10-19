from time import sleep
def miniHelp(f):
    print('\033[45m~' * (len(f) + 36))
    print(f"  Acessando o manual do comando '{f}'")
    print('~' * (len(f) + 36))
    sleep(1)
    print('\033[7;40m', end='')
    help(f)
    print('\033[m', end='')
    sleep(1)

while True:
    print('\033[41m~'*27)
    print('  SISTEMA DE AJUDA PyHELP')
    print('~'*27)
    sleep(1)
    func = input('\033[mFunção ou biblioteca > ').lower().strip()
    if func == 'fim':
        break
    miniHelp(func)
print('\033[44m~' * 13)
print('  ATÉ LOGO!')
print('~' * 13)
