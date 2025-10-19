frase = input('Digite uma frase qualquer e eu direi se é um palíndromo: ').lower().replace(' ','')
fraseInv = frase[::-1]
if frase == fraseInv:
    print('Essa frase é um PALÍNDROMO!')
else:
    print('Essa frase NÃO é um PALÍNDROMO!')
