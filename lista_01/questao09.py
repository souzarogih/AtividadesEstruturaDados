"""
Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.
"""

nomes = ['Lopes', 'Luiz', 'Lucas', 'Arthu', 'Melo', 'Carlos', 'Felipe']
nome_com_a = list()

for nome in nomes:
    if nome.__contains__('a') or nome.__contains__('A'):
        nome_com_a.append(nome)

print(nome_com_a)

