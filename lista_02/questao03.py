"""
Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
chamado “calcular_area” que retorna a área do retângulo.
"""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

base_retangulo = 5
altura_retangulo = 10

retangulo = Retangulo(base_retangulo, altura_retangulo)
area_do_retangulo = retangulo.calcular_area()

print(f"A área do retângulo {base_retangulo} ")
print(f"A altura do retângulo {altura_retangulo} é: {area_do_retangulo}")
