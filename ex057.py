g = input('Qual é o seu sexo? [M/F]: ').upper().strip()[0]
while 'M' != g != 'F':
    print('Por favor, digite um caractere válido')
    g = input('Qual é o seu sexo? [M/F]: ').upper().strip()
print(f'Você é do sexo {g}')
