import numpy as np


class Listasequencial:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if (valor == self.valores[i]):
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1


class Listasequencialordenada:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i], end=' ')

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1


class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    def visualizar(self):
        print('Tamanho da Fila..: ', self.capacidade)
        print('Início da fila...: ', self.inicio)
        print('Final da fila....: ', self.final)
        print('Variável Nu. El..:', self.numero_elementos)

    def listageral(self):
        for i in range(self.capacidade):
            print(self.valores[i])


class Pilha:

    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items = self.items + [item]

    def desempilhar(self):
        if not self.is_vazia():
            item_removido = self.items[-1]
            self.items = self.items[:-1]
            return item_removido
        else:
            print("A pilha está vazia. Não é possível desempilhar.")

    def topo(self):
        if not self.is_vazia():
            return self.items[-1]
        else:
            print("A pilha está vazia. Não há topo para visualizar.")

    def is_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        if not self.is_vazia():
            print("Itens da pilha:")
            for item in self.items:
                print(item)
        else:
            print("A pilha está vazia. Não há itens para imprimir.")