from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
print(f'O seno de {ang}º é: {sin(radians(ang)):.2f}')
print(f'O cosseno de {ang}º é: {cos(radians(ang)):.2f}')
print(f'A tangente de {ang}º é: {tan(radians(ang)):.2f}')
