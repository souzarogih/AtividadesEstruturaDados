"""
Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
métodos “depositar” e “sacar” para manipular o saldo.
"""

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("O depósito não pode ser zero reais.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso. Seu saldo atual é: R${self.saldo}")
            else:
                print("Seu saldo é insuficiente para realizar o saque desejado.")
        else:
            print("O valor do saque deve ser maior que zero.")

conta = ContaBancaria("Higor")
conta.depositar(100)
conta.depositar(800)
conta.sacar(500)
conta.sacar(55)
