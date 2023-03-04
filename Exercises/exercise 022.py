# Exercício - 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
# - O nome com todas as letras maiúsculas e minúsculas.
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# - Quantas letras ao todo (sem condiderar espaços).
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# - Quantas letras tem o primeiro nome.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
