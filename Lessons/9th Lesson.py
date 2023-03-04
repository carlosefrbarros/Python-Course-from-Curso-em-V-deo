# 9ª Aula - Manipulando Strings

# frase = 'Curso em Video Python'

# print(frase) == 'Curso em Video Python'

# frase[9] == 'V'

# print(frase[9]) == 'V'

# print(frase[9:13]) == 'Vide'

# print(frase[9:21]) == 'Video Python'

# print(frase[9:21:2]) == 'VdoPto'

# print(frase[:5]) == 'Curso'

# print(frase[15:]) == 'Python'

# print(frase[9::3]) == 'VePh'

# len(frase) == 21

# frase.count('o') == 3

# frase.count('o', 0, 13) == 1

# frase.find('deo') == 11

# frase.find('Android') == -1

# 'Curso' in frase == True

# frase.replace('Python', 'Android') == 'Curso em Video Android'

# frase.upper() == 'CURSO EM VIDEO PYTHON'

# frase.lower() == 'curso em video python'

# frase.capitalize() == 'Curso em video python'

# frase.title() == 'Curso Em Video Python'

# frase2 = '   Aprenda Python  '

# frase2.strip() == 'Aprenda Python'

# frase.rstrip() == '   Aprenda Python'

# frase.lstrip() == 'Aprenda Python  '

# frase.split() == 'Curso', 'em', 'Video', 'Python'

# '-'.join(frase) == 'Curso-em-Video-Python'

frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])

# Exercício - 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite o seu nome completo: '))
# - O nome com todas as letras maiúsculas e minúsculas.
print(nome.upper())
print(nome.lower())
# - Quantas letras ao todo (sem condiderar espaços).
len(nome) - nome.count(' ')
# - Quantas letras tem o primeiro nome.
len((nome.split())[0])

# Exercício - 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = str(input('Digite um número: '))

print('Unidade: {}'.format(n[-1]))
print('Dezena: {}'.format(n[-2]))
print('Centena: {}'.format(n[-3]))
print('Milhar: {}'.format(n[-4]))

# Exercício - 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: '))
print(' O nome da cidade digitada começa com "Santo"? {}'.format(((cidade.split())[0]) == 'Santo'))

# Exercício - 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome completo: '))
print('O nome digitado tem Silva? {}' .format('Silva' in nome))

# Exercício - 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
print('Quantas vezes a letra "A" aparece? {}'.format(frase.count('A')))
print('Qual a primeira vez que a letra "A" aparece? {}'.format(frase.find('A')))
print('Qual a última vez que a letra "A" aparece? {}'.format())

# Exercício - 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: '))
print('Olá {} {}!'.format((nome.split())[0], (nome.split())[-1]))
