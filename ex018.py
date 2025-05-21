import math

ang = int(input('Digite um angulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O seno do ângulo {}º é: {:.2f} \nO Cosseno desse ângulo é: {:.2f} \nA tangente é: {:.2f}'. format(ang, seno, cosseno, tangente))