n = int(input('Digite quantos termos você quer da sequência de fibonacci: '))
fib = []
while len(fib) < n:
    if len(fib) == 0:
        fib.append(0)
    elif len(fib) == 1:
        fib.append(1)
    else:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
for i in range(0,n):
    print(f'{fib[i]} -> ', end='')
print('FIM')
