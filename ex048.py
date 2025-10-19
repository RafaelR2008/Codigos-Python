s = 0
for i in range(1,501,2):
    if i % 3 == 0:
        s += i
print(f'A soma de todos os números ímpares entre 1 e 500 que são múltiplos de 3 é: {s}')
