"""
Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.
"""

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("Digite um número maior que O pois o fatorial de 0 é 1.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")
