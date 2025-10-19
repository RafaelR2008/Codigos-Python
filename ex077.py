palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro', 'escola', 'celular', 'paralelepipedo', 'pneumoultramicroscopicossilicovulcanoconiotico')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
