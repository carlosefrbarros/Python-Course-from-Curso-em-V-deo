# Exercício 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))
