from random import randint
numbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram:', end=' ')
for n in numbers:
    print(n, end=' ')
print(f'\nO maior valor gerado foi: {max(numbers)}')
print(f'O menor valor gerado foi: {min(numbers)}')
