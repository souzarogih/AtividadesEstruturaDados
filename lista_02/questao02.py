"""
 Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes”
 que retorna uma string com as informações do livro
"""


class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f'Detalhes do livro[ titulo: {self.titulo} autor: {self.autor}]'


livro = Livro(titulo="A procura da luz no fim do túnel", autor='Higor Souza')
resposta = Livro.detalhes(livro)
print(resposta)
