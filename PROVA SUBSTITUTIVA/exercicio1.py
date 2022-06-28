# 1. Em um escritório, há uma impressora compartilhada. No início do expediente,
#    Claudionor, Bartira, Idalécio e Risoleta enviaram a ela trabalhos de 
#    impressão.
# 
# 2. No entanto, antes que o trabalho de Claudionor pudesse ser impresso, Marizete e
#    Norberto enviaram seus trabalhos de impressão com prioridade, para que ficassem
#    prontos antes dos impressos dos colegas.
# 
# 3. Quando 4 trabalhos de impressão já haviam sido concluídos, Risoleta percebeu
#    que havia enviado o arquivo errado, e cancelou seu trabalho de impressão.
# 
# 4. Enquanto a impressora ainda processava os pedidos, ela recebeu mais dois pedidos:
#    o de Verena, sem prioridade, e o de Eurides, com prioridade.
# 
# 5. Utilize a estrutura de dados apropriada para representar a situação relatada. 

from tkinter import E
from deque import Deque

deque = Deque()

# Inserção do início do expediente
deque.insert_back('Claudionor')
deque.insert_back('Bartira')
deque.insert_back('Idalécio')
deque.insert_back('Risoleta')
print("Fila de impressão no início do expediente:",deque)

# Inserção de duas pessoas prioritárias
deque.insert_front('Marizete')
deque.insert_front('Norberto')
print("Inserção de duas prioridades:",deque)

# 4 impressões feitas
atendido = deque.remove_front()
print("Impresso:", atendido)
atendido = deque.remove_front()
print("Impresso:", atendido)
atendido = deque.remove_front()
print("Impresso:", atendido)
atendido = deque.remove_front()
print("Impresso:", atendido)

# Cancelou a impressão
desistente = deque.remove_back()
print('Cancelou impressão: ', desistente)
print("Impressões na fila: ",deque)

# Duas inserções, uma com e outra sem prioridade
deque.insert_back('Verena')
deque.insert_front('Eurides')
print("Adição de Verena sem prioridade, e Eurides com prioridade:",deque)

# Consultando o próximo a ser atendido
proximo = deque.peek_front()

# Consultando o último da fila
ultimo = deque.peek_back()

print('Próximo: ', proximo)
print('Último: ', ultimo)
