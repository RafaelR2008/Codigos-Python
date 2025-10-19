c = {'branco':'\033[m',  'preto':'\033[30m',  'vermelho':'\033[31m',  'verde':'\033[32m',  'amarelo':'\033[33m',
       'azul':'\033[34m','roxo':'\033[35m',  'aclaro':'\033[36m',  'cinza':'\033[37m',  'padrao':'\033[90m',}

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos ele vai pagar? '))
print(f'{c['aclaro']}PRESTAÇÃO MENSAL SERÁ DE: R${val/(anos*12):.2f}{c['branco']}')
if val/(anos*12) > sal*0.3:
       print(f'Empréstimo {c['vermelho']}NEGADO{c['branco']}, parcela excede {'\033[4;33m'}30%{c['branco']} do salário')
print('Tenha um bom dia!')
