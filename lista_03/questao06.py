"""
Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes
nela.
"""

def conta_vogais(string):

    contagem = 0

    string = string.lower()

    for char in string:
        if char in "aeiou":
            contagem += 1

    return contagem

entrada = input("Digite uma string: ")
qtd_vogais = conta_vogais(entrada)

print(f"A quantidade de vogais na string é: {qtd_vogais}")
