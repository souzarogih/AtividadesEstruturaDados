"""
Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
do funcionário.
"""

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            print(f"O salário de {self.nome} foi aumentado em {percentual_aumento}%.")
            print(f"Novo salário de {self.nome}: R${self.salario:.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")


funcionario = Funcionario("João", 3500.0, "Auxiliar")
funcionario.aumentar_salario(10)
