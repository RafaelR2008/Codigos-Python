numbers = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'A tupla gerada foi: {numbers}')
print(f'O número 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O primeiro 3 digitado está na posição {numbers.index(3) + 1}')
else:
    print('O número 3 não foi digitado nenhuma vez')
pares = 0
for v in numbers:
    if v % 2 == 0:
        pares += 1
if pares > 0:
    print('Os números pares digitados foram:', end=' ')
    for v in numbers:
        if v % 2 == 0:
            print(v, end=' ')
else:
    print('Nenhum valor par foi digitado')
