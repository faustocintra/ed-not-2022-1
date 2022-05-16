from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Inserção em lista vazia; a posição será ignorada
lista.insert(5, 'Epaminondas')
print(lista)

# Inserção no início da lista
lista.insert_head('Filisberto') # Equivale a: lista.insert(0, 'Filisberto')
print(lista)

# Inserção no final da lista
lista.insert_tail('Jeruza')     # Equivale a: lista.insert(lista.count, 'Jeruza')
print(lista)

# Inserção em posição intermediária
lista.insert(2, 'Laudicéia')
print(lista)
lista.insert(1, 'Drusila')
print(lista)