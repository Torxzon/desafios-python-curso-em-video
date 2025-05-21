import random
n = random.randint(0,5)
u = int(input('Digite um numero entre 0 e 5: '))
if u == n:
    print('Você acertou, eu escolhi {} igual a vc'.format(n))
else:
    print('Eu venci, escolhi o numero {}'.format(n))