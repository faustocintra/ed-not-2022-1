"""
    1. Veja, na imagem "torres-hanoi.png", como funciona o jogo das Torres de Hanoi.

    2. Cada uma das torres do jogo se comporta como uma pilha. Importe a classe
        apropriada e crie três pilhas, representando as três torres.

    3. Use os valores 1, 2 e 3 para representar os discos. Empilhe-os na primeira
        torre.

    4. Desempilhe um dos discos da primeira torre e empilhe-o na terceira.

    5. Desempilhe o disco remanescente da primeira torre e coloque-o na segunda.

    6. Desempilhe o disco da terceira torre e coloque-o sobre o disco da segunda torre.

    7. Desempilhe o disco da primeira torre e coloque-o na terceira torre.

    8. Desempilhe um dos discos da segunda torre e coloque-o na primeira torre.

    9. Desempilhe o disco da segunda torre e coloque-o sobre o disco da terceira torre.

    10.Finalmente, desempilhe o disco da primeira torre e coloque-o na terceira torre.

    11.Use a função print() para exibir as três pilhas. As duas primeiras devem estar
        vazias e a terceira deve conter os três discos, na ordem (3 na base, 1 no topo).
"""

from lib.stack import Stack

torre_a = Stack()
torre_b = Stack()
torre_c = Stack()

# RESPOSTA 3
torre_a.push(3)
torre_a.push(2)
torre_a.push(1)

print(50 * '-')
print('Torre A:', torre_a)
print('Torre B:', torre_b)
print('Torre C:', torre_c)

# RESPOSTA 4
torre_c.push(torre_a.pop())

# RESPOSTA 5
torre_b.push(torre_a.pop())

# RESPOSTA 6
torre_b.push(torre_c.pop())

# RESPOSTA 7
torre_c.push(torre_a.pop())

# RESPOSTA 8
torre_a.push(torre_b.pop())

# RESPOSTA 9
torre_c.push(torre_b.pop())

# RESPOSTA 10
torre_c.push(torre_a.pop())

print(50 * '-')
print('Torre A:', torre_a)
print('Torre B:', torre_b)
print('Torre C:', torre_c)