"""
    1) Identifique a estrutura de dados abaixo.
        R: Estrutura de dados DEQUE

    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).

        A: Nome da classe
        B: Uma função de somente leitura que informa se a fila está vazia (true ou false)
        C: É o vetor responsável por armazenar a lista
        D: Método que faz a remoção do início do Deque (posição 0)
        E: Método que consulta o início do Deque (posição 0)
        F: Método responsável pela remoção do final do Deque (utilizando a função pop)
        G: Método que insere H no final do Deque 
        H: Recebe o valor a ser inserido ou removido do Deque
        I: Método para consulta no final do Deque
        J: Método que insere K no início (posição 0) do Deque
        K: Recebe o valor a ser inserido ou removido do Deque

"""

class A:

    @property
    def b(self):
        return len(self.__c) == 0

    def __init__(self):
        self.__c = []    # Lista vazia

    def d(self):
        if self.b:
            raise Exception('ERRO')
        return self.__c.pop(0)

    def e(self):
        if self.b:
            raise Exception('ERRO')
        return self.__c[0]

    def __str__(self):
        return str(self.__c)

    def f(self):
        if self.b:
            raise Exception('ERRO')
        return self.__c.pop()

    def g(self, h):
        self.__c.append(h)

    def i(self):
        if self.b:
            raise Exception('ERRO')
        return self.__c[-1]

    def j(self, k):
        self.__c.insert(0, k)

