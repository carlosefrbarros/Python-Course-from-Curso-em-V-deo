# Exercício - 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Olá {} {}!'.format((nome.split())[0], (nome.split())[-1]))
