lista=[]
lpar =[]
limpar=[]

while True:
    lista.append(int(input('Digite o numero: ')))
    res = input('Deseja continuar? N/S ')
    if res in 'Nn':
        break

for n in lista:
    if n%2 == 0:
        lpar.append(n)
    else:
        limpar.append(n)
lista.sort()
lpar.sort()
limpar.sort()
print(f'A lista completa é: {lista} ')
print(f'A lista de pares: {lpar} ')
print(f'a lista de impar: {limpar}')