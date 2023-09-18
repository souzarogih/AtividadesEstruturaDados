'''
Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.
'''

while 1==1:
    numero = float(input('Digite o número: '))
    resto = numero % 2
    if resto == 0:
        print('Número é par!\n')
    elif resto == 1:
        print('Número é impar!\n')
    else:
        print('Número não identificado!\n')
