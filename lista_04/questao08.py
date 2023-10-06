"""
Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do
meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um
número ímpar de elementos.
"""

def mediana(vetor):
    vetor.sort()
    meio = len(vetor) // 2

    return vetor[meio]


mediana_valor = mediana([21, 105, 64, 25, 12, 55, 12, 22, 11, 31])
print(f"A mediana do vetor é: {mediana_valor}")
