pes = float(input('Digite o peso de uma pessoa: '))
alt = float(input('Digite a altura de uma pessoa: '))
imc = pes / alt ** 2
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Seu peso está ideal')
elif imc < 30:
    print('Você tem sobrepeso')
elif imc < 40:
    print('Você tem obesidade')
else:
    print('Você tem obesidade mórbida')

