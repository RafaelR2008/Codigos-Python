from math import hypot
cat1 = float(input('Digite um valor para um cateto de um triângulo: '))
cat2 = float(input('Digite o valor para o outro cateto: '))
hip = hypot(cat1, cat2)
print(f'A medida da hipotenusa de um triângulo cujo catetos medem {cat1} e {cat2} é: {hip:.2f}')
