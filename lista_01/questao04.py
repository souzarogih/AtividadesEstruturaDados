'''
Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.
'''

lista_numeros = [
    1,
    2,
    3,
    4,
    5,
]

maior = lista_numeros[0]
menor = lista_numeros[0]

for numero in lista_numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'Maior: {maior} e menor: {menor}')
