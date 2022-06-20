"""
1. Todas as questões deste arquivo referem-se ao grafo representado
   na imagem "grafo.png".

2. Importe a classe Graph neste arquivo e implemente em código o grafo
   mostrado na imagem. Use print() para exibir o grafo.


3. Exclua o vértice cujo valor é "Etelvina". Use print() para exibir o grafo
   após a exclusão.
"""

# Resposta do exercício 2:
from lib.graph import Graph

relations = Graph(True)

# Adição de nós:
relations.add_vertex('Guiomar')
relations.add_vertex('Veneranda')
relations.add_vertex('Etelvina')
relations.add_vertex('Nereu')
relations.add_vertex('Quiteria')

# Adição das arestas:
relations.add_edge('Guiomar', 'Veneranda', 'amiga de')
relations.add_edge('Veneranda', 'Guimar', 'amiga de')
relations.add_edge('Guiomar', 'Nereu', 'madrinha de')
relations.add_edge('Nereu', 'Guiomar', 'afilhado de')
relations.add_edge('Nereu', 'Veneranda', 'apaixonado por')
relations.add_edge('Nereu', 'Etelvina', 'filho de') # Já exclui
relations.add_edge('Etelvina', 'Nereu', 'mãe de') #já exclui
relations.add_edge('Veneranda', 'Quiteria', 'deve dinheiro para')
relations.add_edge('Veneranda', 'Etelvina', 'trabalha para') #já exclui
relations.add_edge('Quiteria', 'Nereu', 'apaixonada por')

print('Grafo criado para a resposta do exercício 2')
print(relations)
print('-----------------------------')
print('\n')

# Resposta do exercício 3:
# É NECESSÁRIO REMOVER AS ARESTAS CONECTADAS AO VÉRTICE ANTES DE EXCLUIR
# O PRÓPRIO VÉRTICE
relations.remove_edge('Etelvina', 'Nereu', 'mãe de')
relations.remove_edge('Veneranda', 'Etelvina', 'trabalha para')
relations.remove_edge('Nereu', 'Etelvina', 'filho de')
relations.remove_vertex('Etelvina')

print('Grafo após a remoção de vértice para atender a resposta do exercício 3:')
print(relations)


