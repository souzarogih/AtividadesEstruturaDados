"""
Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
método chamado “calcular_perimetro” que retorna o perímetro do triângulo.
"""

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro

lados = {"lado1": 5.0, "lado2": 4.0, "lado3": 3.0}

triangulo = Triangulo(lados['lado1'], lados['lado2'], lados['lado3'])
perimetro_do_tri = triangulo.calcular_perimetro()

print(f"O perímetro do triângulo é: {perimetro_do_tri}")
