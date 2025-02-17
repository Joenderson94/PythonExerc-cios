import random

import lista

a = input('digite o primeiro: ')
b = input('digite o segundo: ')
c = input('digite o terceiro: ')
d = input('digite o quarto: ')

lista = [a,b,c,d]


print('{} que irá apagar.'.format(random.choice(lista)))