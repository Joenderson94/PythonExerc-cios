nome = str(input('Digite o nome completo: ')).strip()
print('Seu nome em maiusculo: {}'.format(nome.upper()))

print('Seu nome em minusculo: {}'.format(nome.lower()))

print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))


print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))