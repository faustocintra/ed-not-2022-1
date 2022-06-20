"""
    1. Observe a classe Nodo listada logo abaixo.

    2. Responda: para qual ou quais estruturas esse nodo pode ser utilizado?
       RESPOSTA ~> A classe Node, conforme mostrada abaixo, poderia ser utilizada com as
                   estruturas lista duplamente encadeade (DoublyLinkedList) e árvore
                   binária de busca (BinarySearchTree);

    3. Qual seria o propósito dos atributos __a, __b e __c?
       RESPOSTA ~> O atributo __a, para ambas as estruturas, representa a informação de
                   usuário armazenada no nodo.
                   O atributo __b seria o prev para DoublyLinkedList ou o left para 
                   BinarySearchTree.
                   O atributo __c seria o next para DoublyLinkedList ou o right para
                   BinarySearchTree.

"""

class Node:
    def __init__(self, x):
        self.__a = x
        self.__b = None
        self.__c = None
