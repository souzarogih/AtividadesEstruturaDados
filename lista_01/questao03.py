'''
Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.
'''


def exibe_numeros_pares(numero):
    for i in range(0, numero + 1, 2):
        print(i)


numero = int(input("Digite um número: "))
exibe_numeros_pares(numero)
