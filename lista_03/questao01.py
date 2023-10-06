"""
Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).
"""


def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)


media = calcular_media(notas)
resultado = verificar_aprovacao(media)
print(f"Média do aluno: {media:.2f}")
print(f"Situação do aluno: {resultado}")
