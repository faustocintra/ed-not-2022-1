"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de ordenação Bubble Sort
        
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    z: função do algoritmo de ordenação
    y: lista a ser ordenada
    x: controla se houve ou não trocas
    w: variável de controle do for

    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    A linha
    y[w], y[w + 1] = x[w], x[w + 1]
    deve ser corrigida para
    y[w], y[w + 1] = y[w], y[w + 1]
"""

def z(y):
    while True:
        x = False
        for w in range(len(y) - 1):
            if y[w] > y[w + 1]:
                y[w], y[w + 1] = x[w], x[w + 1]
                x = True
        if not x:
            break