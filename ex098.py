from time import sleep
def contador(inicio, fim, step):
    print('=-'*20)
    if step == 0:
        step = 1
    elif inicio > fim:
        step = abs(step)
    print(f'Contagem de {inicio} até {fim} de {step} em {step}:')
    sleep(1)
    for c in range(inicio, fim + 1 if inicio < fim else fim - 1, step if inicio < fim else step * -1):
        print(f'{c}', end=' ')
        sleep(0.2)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('=-'*20)
print('Agora é a sua vez de personalizar a contagem!')
comeco = int(input('Inicio: '))
final = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(comeco, final, passo)
