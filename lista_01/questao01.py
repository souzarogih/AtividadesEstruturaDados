'''
Faça um programa que calcule a média de três números inseridos pelo usuário.
'''

import statistics as s

cont = 1
notas = list()

while (cont <= 3):
       nota = float(input(f'Insira a {cont}ª nota: '))
       notas.append(nota)
       print(f'Incluindo nota {notas}')
       cont += 1

print("A média das notas é: ", s.mean(notas))
