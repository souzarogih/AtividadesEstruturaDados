"""
Crie uma função que verifica se um número é primo ou não.
"""

def is_primo(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

try:
    numero = int(input("Digite um número inteiro para verificar se é primo: "))
    if is_primo(numero):
        print(f"{numero} é número primo.")
    else:
        print(f"{numero} não é número primo.")
except ValueError:
    print("Por favor, insira um número inteiro.")
