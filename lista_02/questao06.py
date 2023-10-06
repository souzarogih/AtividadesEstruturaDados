"""
Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).
"""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        total = self.preco * self.quantidade
        return total


produto = Produto("MacBook", 250.0, 3)
total_do_produto = produto.calcular_total()

print(f"O total do produto '{produto.nome}' é: R${total_do_produto}")
