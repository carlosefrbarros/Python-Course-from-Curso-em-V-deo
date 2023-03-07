# 10ª Aula - Condições (Parte 1)

"""
if condition:
    bloco True
else:
    bloco False
"""

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

n1 = float(input('Digite a primeira note: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# Exercício 028 - Escreva um programa que faça o computador "pensar" um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Exercício 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custa R$ 7,00 por cada km acima do limite.

velocidade = int(input('Qual a velocidade do carro em km/h? '))

if velocidade <= 80:
    print('Você está dentro do limite de velocidade.')
else:
    multa = (velocidade - 80) * 7
    print('Você estava {}km/h acima do limite de velocidade, sua multa é de {}.'.format((velocidade-80), multa))

# Exercício 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

n = int(input('Digite um número: '))

if n % 2 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))

# Exercício 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.

distancia = int(input('Qual a distãncia da viagem em Km? '))

if distancia <= 200:
    print('O custo da viagem é {}'.format(distancia * 0.5))
else:
    print('O custo da viagem é {}'.format(distancia * 0.45))

# Exercício 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Exercício 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Exercício 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os salários inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual o salário do funcionário? '))

if salario <= 1250:
    print('O novo salário do funcionário é {}.'.format(salario * 1.15))
else:
    print('O novo salário do funcionário é {}'.format(salario * 1.1))

# Exercício 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 > (r2 + r3):
    print('Não é possível montar um triângulo, pois a reta r1 é maior do que a soma de r2 e r3.')
else:
    if r2 > (r1 + r3):
        print('Não é possível montar um triângulo, pois a reta r2 é maior do que a soma de r1 e r3.')
    else:
        if r3 > (r1 + r2):
            print('Não é possível montar um triângulo, pois a reta r3 é maior do que a soma de r1 e r2.')
        else:
            print('É possível montar um triângulo com os valores dados de r1, r2 e r3.')
