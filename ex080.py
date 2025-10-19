"""valores = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for c, v in enumerate(valores):
            if v >= valor:
                valores.insert(c, valor)
                print(f'Adicionado na posição {c} da lista...')
                break
            elif c == len(valores) - 1:
                valores.append(valor)
                print('Adicionado ao final da lista...')
                break
print('=-'*20)
print(f'Os valores digitados em ordem foram {valores}')"""

valores = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valores[-1] <= valor:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for c, v in enumerate(valores):
            if v >= valor:
                valores.insert(c, valor)
                print(f'Adicionado na posição {c} da lista...')
                break
print('=-'*20)
print(f'Os valores digitados em ordem foram {valores}')
