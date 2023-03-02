# 8ª Aula - Utilizando Módulos

# import x as z

# from x import y

# from x import y as z

#import math

#from math import sqrt
#from math import floor, ceil

import math

n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz de {} é igual a {:.2f}.'.format(n, raiz))

from math import sqrt

raiz = sqrt(n)

import random

num = random.random

print(num)

# Exercício 016 - Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira

import math

n = float(input('Digite um número: '))

print('A parte inteira de {} é {}'.format(n, math.trunc(n)))

# Exercício 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.sqrt(math.pow(co) + math.pow(ca))

print('O cateto oposto mede {}, o cateto adjacente {}, logo, a hipotenusa mede {}'.format(co, ca, h))

# Exercício 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('Dado o ângulo {}, seu seno é {}, seu cosseno é {} e a sua tangente é {}'.format(angulo, seno, cosseno, tangente))

# Exercício 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))

sorteado = random.sample([a, b, c, d], k=1)

print('O aluno sorteado é {}'.format(sorteado))

# Exercício 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de seus alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))

turma = [a, b, c, d]

turma_nova = random.shuffle(turma)

# Exercício 021 - Faça um programa em Python que abra e reproduza um áudio de um arquivo em MP3
