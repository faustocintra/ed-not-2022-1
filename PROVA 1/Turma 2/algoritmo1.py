"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de ordenação Quick Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    z: função do algoritmo Quick Sort
    y: a lista a ser ordenada
    x: posição inicial da lista
    w: posição final da lista
    v: pivô
    u: divisor da lista
    t: variável de controle do for
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    RESPOSTA ~>
    A troca de valores entre as posições do divisor (u)
    e atual do for (t) está errada. A linha
    y[t], y[t + 1] = y[t + 1], y[t]
    deve ser corrigida para
    y[t], y[u] = y[u], y[t]
"""

def z(y, x = 0, w = None):
    if w is None: w = len(y) - 1
    if w <= x: return
    v = w
    u = x - 1
    for t in range(x, w):
        if y[t] < y[v]:
            u += 1
            if u != t:
                y[t], y[t + 1] = y[t + 1], y[t]
    u += 1
    if u != v and y[v] < y[u]:
        y[v], y[u] = y[u], y[v]
    z(y, x, u - 1)
    z(y, u + 1, w)