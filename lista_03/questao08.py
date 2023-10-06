"""
Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa,
dependendo da escolha do usuário.
"""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Escolha o tipo de conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"Temperatura em Fahrenheit é: {resultado:.2f} °F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"Temperatura em Celsius é: {resultado:.2f} °C")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2 para a conversão.")
