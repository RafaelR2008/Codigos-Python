#Usando for
"""num = int(input('Digite um número e eu direi qual é o seu fatorial: '))
fatorial = 1
for i in range(2, num + 1):
    fatorial *= i
print(f'O fatorial de {num} é: {fatorial}')"""

#Usando while
num = int(input('Digite um número e eu direi qual é o seu fatorial: '))
fatorial = 1
i = 2
while i <= num:
    fatorial *= i
    i += 1
print(f'O fatorial de {num} é: {fatorial}')
