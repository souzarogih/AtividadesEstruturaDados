"""
Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
algoritmo de seleção.
"""


vetor = [12, 34, 120, 9, 25, 12, 22, 6, 11]

def ordenar_por_selecao(vetor):
    tam = len(vetor)

    for i in range(tam):
        indice_menor = i
        for j in range(i + 1, tam):
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j

        vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]


ordenar_por_selecao(vetor)

print("Vetor ordenado crescente:")
print(vetor)
