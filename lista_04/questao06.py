"""
Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
quantos números pares e quantos números ímpares existem no vetor ordenado.
"""

def contar_numeros_e_pares_impares(vetor):
    vetor.sort(reverse=True)

    pares = 0
    impares = 0

    for elemento in vetor:
        if elemento % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

vetor = [89 ,64, 25, 34, 120, 9, 25, 12, 22, 6, 11, 22, 45, 30, 17]

pares, impares = contar_numeros_e_pares_impares(vetor)
print("Vetor ordenado decrescente:", vetor)
print(f"Números pares é: {pares}")
print(f"Números ímpares é: {impares}")
