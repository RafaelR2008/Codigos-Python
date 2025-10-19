turma = []
aluno = []
nota = []
while True:
    aluno.append(input('Nome: '))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    turma.append(aluno[:])
    aluno.clear()
    nota.clear()
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
print('-=' * 30)
print('No. NOME       MEDIA')
print('-'*30)
for i, c in enumerate(turma):
    print(f'{i + 1}.  {c[0]:12}{(c[1][0] + c[1][1])/2:.1f}')
print('-' * 40)
while True:
    esc = int(input('Mostrar notas de qual aluno? [999 para parar] '))
    while esc < 1 or esc > len(turma) and esc != 999:
        esc = int(input('Por favor, digite um número de aluno válido: '))
    if esc == 999:
        break
    print(f'Notas de {turma[esc - 1][0]} são {turma[esc - 1][1]}')
    print('-'*40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
