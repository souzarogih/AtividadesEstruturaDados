"""
Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
“calcular_media” que retorna a média das notas do aluno.
"""

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0  # Retorna 0 se não houver notas

aluno = Aluno("Pedro", [8.5, 9.0, 7.5, 6.0])
media_do_aluno = aluno.calcular_media()

print(f"Aluno {aluno.nome} tem média: {media_do_aluno:.2f}")
