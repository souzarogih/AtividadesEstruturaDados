"""
Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos
especificado pelo usuário.
"""

def seq_fibonacci(numero_de_termos):
    fibonacci = [0, 1]

    while len(fibonacci) < numero_de_termos:
        proximo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_termo)

    return fibonacci

try:
    n = int(input("Digite o número de termos desejado para a sequência de Fibonacci: "))

    if n <= 0:
        print("Por favor, insira um número de termos válido (maior que zero).")
    else:
        result = seq_fibonacci(n)

        print(f"A sequência de Fibonacci com {n} termos é:")
        print(result)
except ValueError:
    print("Por favor, insira um número inteiro válido.")
