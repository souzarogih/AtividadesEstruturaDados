"""
Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.
"""
def calcular_soma_digitos(num):
    soma = 0
    while num > 0:
        digito = num % 10
        soma += digito
        num //= 10
    return soma


try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        resultado = calcular_soma_digitos(numero)
        print(f"A soma dos dígitos de {numero} é: {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
