"""
Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
e peso.
"""

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Valores inválidos. Peso e altura devem ser maiores que zero."

    imc = peso / (altura ** 2)

    return imc


try:
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    resultado_imc = calcular_imc(peso, altura)

    print(f"Resultado do IMC é: {resultado_imc:.2f}")
except ValueError:
    print("Insira valores válidos para peso e altura.")
