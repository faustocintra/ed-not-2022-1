from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

arvore.insert(37)
arvore.insert(20)
arvore.insert(51)
arvore.insert(3)
arvore.insert(43)
arvore.insert(0)
arvore.insert(72)
arvore.insert(11)
arvore.insert(40)
arvore.insert(8)
arvore.insert(66)
arvore.insert(19)
arvore.insert(75)
arvore.insert(82)

print('Em-ordem:')
arvore.in_order_traversal()
print('-----------------------------------------------------------')

print('Pré-ordem:')
arvore.pre_order_traversal()
print('-----------------------------------------------------------')

print('Pós-ordem:')
arvore.post_order_traversal()
print('-----------------------------------------------------------')

# Testes de existência de valores na árvore
existe43 = arvore.exists(43)
existe35 = arvore.exists(35)
existe0 = arvore.exists(0)
print(f'Existe 43? {existe43}; existe 35? {existe35}; existe 0? {existe0}')

# Valor mínimo da árvore
minimo = arvore.min_node()
print(f'[Mínimo da árvore] Valor: {minimo[0].data}, profundidade: {minimo[1]} ')

# Valor máximo da árvore
maximo = arvore.max_node()
print(f'[Máximo da árvore] Valor: {maximo[0].data}, profundidade: {maximo[1]} ')