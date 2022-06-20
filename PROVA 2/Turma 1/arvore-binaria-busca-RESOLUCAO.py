"""
    1. Todas as questões deste arquivo referem-se à árvore binária de busca representada
        na imagem "abb.png".

    2. Caso seja necessário escrever algum código para responder às perguntas seguintes,
        importe a classe BinarySearchTree neste arquivo e faça os testes aqui.

    3. Qual a altura da subárvore à direita de 45?
       RESPOSTA ~> A altura é 6 (seis).

    4. Quais níveis da árvore estão completos, isto é, já contêm o número máximo de nodos
        permitidos?
       RESPOSTA ~> Níveis completos: 0, 1, 2 e 3.
    
    5. Qual a profundidade do nodo de valor 27, em relação à árvore como um todo?
       RESPOSTA ~> 4 (quatro).

    6. A árvore representada está equilibrada? Por quê? Justifique sua resposta.
       RESPOSTA ~> Não, porque a diferença de altura entre as subárvores esquerda e direita é
                   maior que 2 (dois).

    7. Como ficaria o percurso pré-ordem desta árvore?
       RESPOSTA ~> 45, 24, 9, 3, 0, 6, 15, 12, 18, 39, 36, 27, 33, 42, 72, 66, 60, 49, 
                   54, 51, 57, 63, 69, 84, 78, 75, 81, 96, 90, 87, 99.

    8. Se for removido o nodo raiz (de valor 45), qual(is) nodo(s) poderia(m) ocupar o seu lugar?
       Justifique sua resposta. 
       RESPOSTA ~> Poderia ser o 42, pois ele é o MAIOR valor da subárvore ESQUERDA, ou o 49, por 
                   ser o MENOR da subárvore DIREITA.   

"""