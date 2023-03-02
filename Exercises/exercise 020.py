# Exercício 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de seus alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))

turma = [a, b, c, d]

random.shuffle(turma)

print('A ordem de apresentação será ')
print(turma)
