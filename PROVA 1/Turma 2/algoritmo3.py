"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de busca binária
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    z: função de busca binária
    y: lista onde onde será feita a busca
    x: valor a ser buscado
    w: posição inicial da lista
    u: posição final da lista
    t: meio calculado da lista
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    RESPOSTA:
    Todas as referências a y[u] devem ser substituídas
    por y[t]
"""

def z(y, x):
    w = 0  
    u = len(y) - 1 
    while w <= u:
        t = (w + u) // 2 
        if x == y[u]:
            return t
        elif x > y[u]:
            w = t + 1
        else:
            u = t - 1
    return -1