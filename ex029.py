vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Velocidade acima de 80Km/h, Você foi multado!')
    print(f'A multa irá custar R${(vel - 80) * 7:.2f}')
else:
    print('Velocidade dentro do limite, aproveite a viagem!')