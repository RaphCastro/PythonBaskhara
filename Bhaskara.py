from math import sqrt

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
d = float((pow(b, 2) - 4 * a * c))
print(f'Delta={d}')
if d > 0:
    x1 = float(-b - (sqrt(d)) / (2 * a))
    x2 = float(-b + (sqrt(d)) / (2 * a))
    print(f'Os valores das raízes são: {x1} e {x2}.')
elif d < 0:
    print('Delta é negativo, logo não há raíz quadrada')
elif d == 0:
    x1 = float(-b - (sqrt(d)) / (2 * a))
    print(f'Ambas as raízes são iguais a {x1}.')
print(f'Formula de Bhaskara para A ({a}), B ({b}) e C ({c}), encerrada.')
