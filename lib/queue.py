"""
    ESTRUTURA DE DADOS FILA (QUEUE)
    É uma estrutura de dados linear em que 
    a operação de inserção (enqueue) acontece no final
    (ou cauda) da estrutura e a operação de remoção (dequeue) ocorre no início (ou cabeça).
    Como consequência, o funcionamento da fila
    pode ser definido como FIFO (First In, First Out):
    o primeiro a entrar é o primeiro a sair.
"""
class Queue:

    """ Método construtor """
    def __init__(self):
        # Inicializa uma lista vazia
        self.__data = []

    """
        Método para inserção
        Nome padronizado: enqueue()
    """
    def enqueue(self, val):
        self.__data.append(val)

    """
        Método para remoção
        Nome padronizado: dequeue()
    """
    def dequeue(self):
        if self.is_empty:
            raise Exception('ERRO: impossível remover de uma fila vazia')
        
        # Remove o primeiro elemento da fila
        return self.__data.pop(0)

    """
        Método que consulta o valor na cabeça da fila, sem retirá-lo de lá
        Nome padronizado: peek()
    """
    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cabeça de uma fila vazia')
        # Retorna o primeiro elemento da lista
        return self.__data[0]

    """
        Método que permite imprimir a fila
        Esse é um método especial do Python: __str__
    """
    def __str__(self):
        return str(self.__data)

    """
        Propriedade somente-leitura que informa se a fila está 
        vazia (True) ou não (False)
    """
    @property
    def is_empty(self):
        return len(self.__data) == 0