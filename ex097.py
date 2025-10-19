def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))

frase = input('Digite uma frase: ')
escreva(frase)
