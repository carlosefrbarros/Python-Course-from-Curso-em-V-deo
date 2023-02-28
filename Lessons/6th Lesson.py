# 6ª Aula - Tipos Primitivos

n1 = input('Digite um número:')
n2 = input('Digite mais um número:')

s = n1 + n2

print('A soma vale {}.'.format(s))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))

# int - integer - inteiros - 7; -4; 0; 9875
# float - float - flutuantes =~ reais - 4.5; 0.076; -15.223; 7.0
# bool - boolean - booleanos ou lógicos - True; False
# str - string - caractere - 'Olá'; '7.5'; 'True'; ''

n1 = input('Digite um valor: ')

print(type(n1))

n1 = int(input('Digite um valor: '))

print(type(n1))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))

print('A soma entre {} e {} vale {}.'.format(n1, n2, s))

n = input('Digite algo: ')

print(n.isnumeric())

# Exercício 003 - Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
print('A soma entre {} e {} vale {}.'.format(n1, n2, s))

# Exercício 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

