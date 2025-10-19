expressao = input('Digite a expressão: ')
expressao = expressao.replace(' ','')
contESQ = 0
contDIR = 0
inval = 0
for i, c in enumerate(expressao):
    if c == '(':
        contESQ += 1
        if i == len(expressao) - 1 or expressao[i + 1] in '+-*/%':
            inval += 1
    elif c == ')':
        contDIR += 1
        if contESQ < contDIR or expressao[i - 1] in '+-*/%(':
            inval += 1
if contESQ == contDIR and inval == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
