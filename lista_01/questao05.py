"""
Faça um programa que leia uma lista de números e retorne a média dos números pares.
"""
lista_original = [1,2,3,4,5,6,7,8,9,10]


def verifica_par(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False


def calc_media(lista):
    soma = int()
    for numero in lista:
        soma = soma + numero

    return soma / lista.__len__()


def ler_numeros(lista):
    pares = list()

    for number in lista:
        if verifica_par(number):
            pares.append(number)

    return calc_media(pares)


res = ler_numeros(lista_original)
print(res)

