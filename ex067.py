while True:
    n = int(input('Quero ver a tabuada do: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-'*30)
print('Finalizando...')