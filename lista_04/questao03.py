"""
Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.
"""
vetor = [634, 29, 12, 55, 122, 232, 11, 31]

def encontrar_maximo(vetor):
    if len(vetor) == 0:
        return None

    maximo = vetor[0]

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

    return maximo

def encontrar_minimo(vetor):
    if len(vetor) == 0:
        return None

    minimo = vetor[0]

    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return minimo




maximo = encontrar_maximo(vetor)
print(f"O elemento máximo no vetor é: {maximo}")

minimo = encontrar_minimo(vetor)
print(f"O elemento mínimo no vetor é: {minimo}")
