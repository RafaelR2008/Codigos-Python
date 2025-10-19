escolha = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while escolha != 5:
    escolha = int(input('''O que você vai fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''))
    if escolha == 1:
        print(f'A soma entre {n1} mais {n2} é igual a: {n1 + n2}')
    elif escolha == 2:
        print(f'O produto entre {n1} vezes {n2} é igual a: {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que o número {n1}')
        else:
            print('Ambos números digitados possuem o mesmo valor')
    elif escolha == 4:
        print('Escolha os números novamente')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif escolha == 5:
        print('Até a próxima!')
    else:
        print('Por favor, digite uma opção válida')
