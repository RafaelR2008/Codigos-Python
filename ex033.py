n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
n3 = int(input('Digite o terceiro número: '))
if n3 >= maior:
    maior = n3
if n3 <= menor:
    menor = n3
print(f'Maior: {maior}\nMenor: {menor}')
