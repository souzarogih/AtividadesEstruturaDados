"""
Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base
na escolha do usuário.
"""

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    return x / y

# Solicita ao usuário para escolher a operação
print("Escolha a operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão")

opcao = int(input("Qual operação deseja selecionar? "))

if opcao < 1 or opcao > 4:
    print("Opção inválida. Por favor, escolha uma opção válida de 1 a 4.")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        result = adicao(num1, num2)
        operacao = "adição"
    elif opcao == 2:
        result = subtracao(num1, num2)
        operacao = "subtração"
    elif opcao == 3:
        result = multiplicacao(num1, num2)
        operacao = "multiplicação"
    else:
        result = divisao(num1, num2)
        operacao = "divisão"

    print(f"O resultado da {operacao} é: {result}")
