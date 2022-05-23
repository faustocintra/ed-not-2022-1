"""
    ESTRUTURA DE DADOS GRAFO
    É uma estrutura de dados não-linear, formada por vértices
    (ou nodos) e arestas. Tem como principal finalidade
    representar as relações entre os vértices, por meio das
    arestas. Tem várias aplicações, como a representação de
    redes de computadores, mapas e caminhos e redes sociais.
"""
class Graph:

    """ Método construtor """
    def __init__(self, is_directed = False):
        self.__is_directed = is_directed # O grafo é direcionado?
        self.__data = {}    # Dicionário vazio

    """
        Método que adiciona um vértice
    """
    def add_vertex(self, val):
        # Verifica se o vértice já existe no dicionário.
        # Só cria o vértice se não existir ainda.
        if not val in self.__data:
            self.__data[val] = set() # Conjunto vazio

    """
        Método que adiciona uma aresta entre dois vértices
    """
    def add_edge(self, origin, dest, rel = None):
        # Cria os vértices de origem e destino,
        # caso não existam ainda
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Coloca a descrição da relação em maiúsculas,
        # se ela tiver sido passada
        if not rel is None: rel = rel.upper()

        # Monta a aresta
        edge1 = (dest, rel)  # Isto é uma tupla

        # Adiciona a relação origem->destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, adiciona a relação
        # origem<-destino
        if not self.__is_directed:
            edge2 = (origin, rel)   # Tupla
            self.__data[dest].add(edge2)

    """
        Método que representa o grafo como string
    """
    def __str__(self):
        output = str(self.__data)
        output += ', is_directed: ' + str(self.__is_directed)
        return output

##################################################

familia = Graph(True)   # Grafo será direcionado
print(familia)

familia.add_vertex('Ariovaldo')
familia.add_vertex('Clementina')
familia.add_vertex('Aristeu')
familia.add_vertex('Clementina') # Tentativa de inserção repetida

print(familia)

familia.add_edge('Ariovaldo', 'Clementina', 'casado com')
familia.add_edge('Ariovaldo', 'Aristeu', 'pai')
familia.add_edge('Clementina', 'Ariovaldo', 'casada com')
familia.add_edge('Clementina', 'Cleusa', 'mãe')
familia.add_edge('Cleusa', 'Clementina', 'filha')

print('-----------------------')
print(familia)

# Não direcionado, equivale a cidades = Graph(false)
cidades = Graph()

cidades.add_edge('Franca', 'Claraval')
cidades.add_edge('Franca', 'Cristais Paulista', 'Rod. Candido Portinari')

print('-----------------------')
print(cidades)

