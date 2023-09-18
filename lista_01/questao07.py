"""
 Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.
"""

limite = int(input("Digite um valor para identificar a sequência de Fibonacci: "))

a, b = 0, 1

while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

print()
