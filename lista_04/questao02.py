"""
Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
serve como chave para realizar a ordenação crescente ou decrescente.
"""

vetor = [21, 105, 64, 25, 12, 55, 12, 22, 11, 31]

def ordenar_vetor(vetor, cresce=True):
    if cresce:
        vetor.sort()
    else:
        vetor.sort(reverse=True)

ordenar_vetor(vetor)
print("Vetor ordenado de forma crescente:")
print(vetor)

ordenar_vetor(vetor, cresce=False)
print("Vetor ordenado de forma decrescente:")
print(vetor)
