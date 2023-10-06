"""
Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
chamado “falar” que imprime uma mensagem com o nome da pessoa.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando.")

pessoa = Pessoa("José", 30)
pessoa.falar()
