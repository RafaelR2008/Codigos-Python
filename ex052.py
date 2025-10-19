r = 0
num = int(input('Digite um número e eu direi se ele é primo: '))
for i in range(1,num+1):
    if num % i == 0:
        r += 1
        print(f'{'\033[32m'}{i}{'\033[m'}', end=' ')
    else:
        print(f'{'\033[31m'}{i}{'\033[m'}', end=' ')
print(f'{'\033[m'}\nO número {num} é divisível por {r} números')
if r == 2:
    print(f'Logo, ele é PRIMO')
else:
    print(f'Logo, ele NÃO É PRIMO')
