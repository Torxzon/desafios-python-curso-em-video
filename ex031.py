d = float(input('Digite a distancia de sua viagem: '))
if d <= 200:
    print('Sua passagem custará R$ {}'.format(d*0.5))
else:
    print('Sua passagem custará R$ {}'.format(d*0.45))