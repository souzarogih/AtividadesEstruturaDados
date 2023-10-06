"""Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário."""

def calcular_fatorial(numero):
    if numero < 0:
        return "Não é possível adimitir fatorial de um números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

# Solicita ao usuário para inserir um número inteiro positivo
try:
    numero = int(input("Digite um número inteiro positivo: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro positivo válido.")
