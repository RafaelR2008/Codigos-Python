nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média foi {media:.1f}')
if media < 5:
    print('Você está REPROVADO!')
elif media >= 7:
    print('Você está APROVADO!')
else:
    print('Você está de RECUPERAÇÃO!')
