# Exercício 016 - Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira

import math

n = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))
