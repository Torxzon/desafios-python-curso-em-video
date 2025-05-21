from math import hypot

c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = hypot(c1, c2)
print('O valor da hipotenusa do triangulo de cateto oposto {} e cateto ajacente {} é {:.2f}.'.format(c1, c2, h))