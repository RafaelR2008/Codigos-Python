print(f'{'\033[37m'}-=-'*20)
print(f'{'\033[36m'}{'ANALISADOR DE TRIÂNGULOS V2.0':^60}{'\033[m'}')
print(f'{'\033[37m'}-=-'*20+'\033[m')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('Não é possível formar um triângulo com esssas medidas')
else:
    print('É possível formar um triângulo com essas medidas')
    if r1 == r2 == r3:
        print('O triângulo será EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('O triângulo será ESCALENO')
    else:
        print('O triângulo será ISÓSCELES')
