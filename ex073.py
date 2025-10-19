
times = ('cruzeiro', 'flamengo', 'red bull bragantino', 'bahia', 'palmeiras', 'botafogo', 'fluminense', 'atlético-MG', 'corinthians', 'ceará',
'mirassol', 'grêmio', 'santos', 'internacional', 'vasco', 'são paulo', 'vitória', 'juventude', 'fortaleza', 'sport')
print(f'TOP 20: {times}')
print('='*30)
print(f'Os 5 primeiros colocados: {times[:5]}')
print('='*30)
print(f'Os 4 últimos colocados: {times[-4:]}')
print('='*30)
print(f'Lista em ordem alfabética: {sorted(times)}')
print('='*30)
print(f'O grêmio está na {times.index('grêmio') + 1}ª posição')
