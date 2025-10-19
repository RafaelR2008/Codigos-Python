num = int(input('Digite um número inteiro: '))
print(f'A tabuada de {num} é:')
for i in range(1,11):
    print(f'{num} x {i:2} = {num * i}')
