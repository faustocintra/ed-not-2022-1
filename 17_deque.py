from tkinter import E
from lib.deque import Deque

deque = Deque()

# Inserção de pessoas de prioridade normal
deque.insert_back('Deusdete')
deque.insert_back('Glaudemir')
deque.insert_back('Ivanilson')
deque.insert_back('Robledo')
deque.insert_back('Otaviano')

# Imprime o deque
print(deque)

# Inserção de uma pessoa prioritária
deque.insert_front('Berenice')

# Imprime o deque
print(deque)

# Remoção no final (desistência)
desistente = deque.remove_back()

print('Desistente: ', desistente)

# Imprime o deque
print(deque)

# Outra inserção prioritária
deque.insert_front('Laudeniza')

# Imprime o deque
print(deque)

# Remoção do início da lista
atendido = deque.remove_front()

print('Atendido: ', atendido)

# Imprime o deque
print(deque)

# Consultando o próximo a ser atendido
proximo = deque.peek_front()

# Consultando o último da fila
ultimo = deque.peek_back()

print('Próximo: ', proximo)
print('Último: ', ultimo)

# Imprime o deque
print(deque)

