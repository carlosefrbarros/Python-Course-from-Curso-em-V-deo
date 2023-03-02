# 7ª Aula - Operadores Aritméticos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2
print('A soma vale {}.'.format(s))

# + --> adição
# - --> subtração
# * --> multiplicação
# / --> divisão
# ** --> potência
# // --> divisão inteira
# % --> módulo ou resto da divisão

# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 2
# 5%2 == 1

# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

# 5+3*2 == 11
# 3*5+4**2 == 31
# 3*(5+4)**2 == 243

# 4**3 == pow(4,3)
# 81**(1/2) == 9.0
# 'Oi'+'Olá' == 'OiOlá'
# 'Oi'*5 == 'OiOiOiOiOi'

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.3}'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))

# Exercício 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))
print('O número digitado foi {}, seu antecessor é o {} e o seu sucessor é o {}.'.format(n, n-1, n+1))

# Exercício 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n, n*2, n*3, n**(1/2)))

# Exercício 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A primeira nota é {:.1f}, a segunda nota é {:.1f} e a média entre as notas é {:.1f}.'.format(n1, n2, (n1+n2)/2))

# Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite um valor em metros: '))
print('O valor em metros é {}, em centímetros é {} e em milímetros é {}.'.format(n, n*100, n*1000))

# Exercício 009 - Faça um programa que leia um número qualquer e mostre na tela a sua tabudada

n = int(input('Digite um número: '))
print('1 x {} = {}'.format(n, n*1))
print('2 x {} = {}'.format(n, n*2))
print('3 x {} = {}'.format(n, n*3))
print('4 x {} = {}'.format(n, n*4))
print('5 x {} = {}'.format(n, n*5))
print('6 x {} = {}'.format(n, n*6))
print('7 x {} = {}'.format(n, n*7))
print('8 x {} = {}'.format(n, n*8))
print('9 x {} = {}'.format(n, n*9))
print('10 x {} = {}'.format(n, n*10))

# Exercício 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar, considere USD 1,00 = BRL 3,27

n = float(input('Quanto reais você tem na carteira? '))
print('Você tem {:.2f} reais, o que com um câmbio de 3,27 BRL para 1 USD, permite adquirir {:.2f} dólares.'.format(n, (n/3.27)))

# Exercício 011 - Faça um programa que leia a largura e a altura de uma parede em metros e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))
print('A parede tem largura {}m e altura {}m, logo tem uma área de {}m² e já que um litro de tinta pinta 2m², para pintar essa parede serão necessários {} litro(s) de tinta'.format(l, a, l*a, (l*a)/2))

# Exercício 012 - Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Qual o preço do produto? '))
print('O preço normal é {}, depois do desconto de 5%, o novo preço é {:.2f}'.format(n, n*0.95))

# Exercício 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

n = float(input('Qual o seu salário? '))
print('O seu salário é {}, depois do aumento de 15%, seu novo valor é {}.'.format(n, n*1.15))
