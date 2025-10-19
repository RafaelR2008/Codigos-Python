r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3
if soma1 <= r3 or soma2 <= r2 or soma3 <= r1:
    print('Não é possível formar um triângulo com esssas medidas')
else:
    print('É possível formar um triângulo com essas medidas')
