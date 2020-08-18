import math


def calcular(delt, a, b, param):
    if param == 1:
        x1 = (-b + math.sqrt(delt))/(2 * a)
        return x1, 0
    else:
        xa = (-b + math.sqrt(delt)) / (2 * a)
        xb = (-b - math.sqrt(delt)) / (2 * a)
        return xa, xb


valor_a = float(input('Digite o valor do indice a:'))
arg = True
while arg:
    if valor_a == 0:
        print('Com zero no indice A, não podemos ter uma equação do 2ºGrau.')
        arg = False
    else:
        valor_b = float(input('Digite o valor do indice b:'))
        valor_c = float(input('Digite o valor do indice c:'))
        delta = (valor_b**2)-(4*valor_a*valor_c)
        if delta < 0:
            print('Delta < 0, logo não possui raizes reais.')
            arg = False
        elif delta == 0:
            raiz = calcular(delta, valor_a, valor_b, 1)
            print('Possui uma raiz real =', raiz[0])
            arg = False
        else:
            raiz = calcular(delta, valor_a, valor_b, 2)
            print('Possui duas raizes reais.\nx1 = {}\nx2 = {}'.format(raiz[0], raiz[1]))
            arg = False
