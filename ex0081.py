lista = []
while True:
    n=int( input('Digite o numero: '))
    lista.append(n)
    res = input('deseja continuar? S/N')
    if res in 'Nn':
        break
lista.sort(reverse=True)
print(f'{lista}')
print(f'a lista possui {len(lista)} números')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 NÃO está na lista!')