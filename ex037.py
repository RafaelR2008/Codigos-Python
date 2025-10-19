n = int(input('Digite um  úmero inteiro: '))
escolha = int(input('Escolha a base de conversão:\n1 - binário\n2 - octal\n3 - hexadecimal\n'))
if escolha == 1:
    print(f'O número {n} em base binária é: {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} em base octal é: {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} em base hexadecimal é: {hex(n)[2:]}')
else:
    print('Você não escolheu nenhuma das opções permitidas')