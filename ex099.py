from time import sleep
def maior(*nums):
    print('=-'*20)
    print('Analizando os valores passados...')
    maiornum = 0
    for i, n in enumerate(nums):
        sleep(0.5)
        print(n, end=' ')
        if i == 0 or n > maiornum:
            maiornum = n
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maiornum}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
