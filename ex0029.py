vel = float( input('qual a velocidade em km/h?'))
multa = 0
if vel > 80:
   multa = (vel - 80)*7
   print('valor da multa: R${:.2f}'.format(multa))
else :
    print('Tenha um bom dia! continue assim!!')
