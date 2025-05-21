v = int(input('Digite a velocidade: '))
if v >= 80:
    v = v - 80
    print('Você foi mutado em R$ {}'.format(v*7,00))
else:
    print('Continue assim')