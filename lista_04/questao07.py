"""Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor."""

vetor = [25, 34, 120, 9, 25, 12]
# vetor = []

def terceiro_maior_numero(vetor):
    vetor_sem_duplicatas = list(set(vetor))

    if len(vetor_sem_duplicatas) < 3:
        return "Não há terceiro maior número no vetor informado."
    else:
        vetor_sem_duplicatas.sort(reverse=True)
        return f"O terceiro maior número no vetor é: {vetor_sem_duplicatas[2]}"


result = terceiro_maior_numero(vetor)
print(result)
