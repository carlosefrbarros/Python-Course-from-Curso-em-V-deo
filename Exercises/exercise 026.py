# Exercício - 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
print('Quantas vezes a letra "A" aparece? {}'.format(frase.count('A')))
print('Qual a primeira vez que a letra "A" aparece? {}'.format(frase.find('A')+1))
print('Qual a última vez que a letra "A" aparece? {}'.format(frase.rfind('A')+1))
