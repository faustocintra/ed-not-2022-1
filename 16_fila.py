from lib.queue import Queue

fila = Queue()

fila.enqueue('Mariovaldo')
fila.enqueue('Belarmina')
fila.enqueue('Valdisney')

# Imprime a fila
print(fila)

# Atende o primeiro da fila
atendido = fila.dequeue()
print('Atendido: ', atendido)

# Verifica quem será o próximo a ser atendido
proximo = fila.peek()
print('Próximo: ', proximo)

# Imprime a fila
print(fila)

# Novas pessoas entram na fila
fila.enqueue('Gercina')
fila.enqueue('Ladislau')

# Imprime a fila
print(fila)