valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
print('=-'*21)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}... ', end='')
