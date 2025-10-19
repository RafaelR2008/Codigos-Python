frase = input('Escreva uma frase: ').lower().strip()
print(f'Nessa frase aparece a letra "A" {frase.count('a')} vezes')
print(f'O primeiro "A" está na posição {frase.find('a') + 1}')
print(f'O último "A" está na posição {frase.rfind('a') + 1}')
