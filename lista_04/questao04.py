"""
Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
"""
def calc_seg_maior_number(vetor):
    if len(vetor) < 2:
        return "Não existe um segundo menor número no vetor informado."

    vetor_sem_duplicatas = list(set(vetor))

    vetor_sem_duplicatas.sort()

    return vetor_sem_duplicatas[1]

vetor = [32, 16, 25, 22, 5, 78, 256, 64, 25, 12, 22, 11, 17, 10, 56]

segundo_menor = calc_seg_maior_number(vetor)
print(f"O segundo menor número no vetor informado é : {segundo_menor}")
