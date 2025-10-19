soma = 0
IDmaisVelho = -1
NMmaisVelho = ''
mulheresNV = 0
print('Atribua nome, idade e sexo para 4 pessoas')
for i in range(1, 5):
    print(f'Pessoa {i}:')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).upper().strip()
    soma += idade
    if sexo == 'M' and idade > IDmaisVelho:
        IDmaisVelho = idade
        NMmaisVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresNV += 1
media = soma / 4
print(f'A média da idade do grupo é: {media:.1f} anos.')
print(f'O nome do homem mais velho é: {NMmaisVelho}.')
print(f'A quantidade de mulheres com menos de 20 anos é: {mulheresNV}.')
