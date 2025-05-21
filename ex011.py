import math

altura = float(input('Qual é a altura da sua parede? '))
largura = float(input('Qual é a largura da sua parede? '))
area = altura * largura
tinta = math.ceil(area/2)
print('Você precisará aproximadamente de {} litros de tinta'.format(tinta))
