"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de ordenação Merge Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    a: função do algoritmo de ordenação
    b: a lista a ser ordenada
    c: meio calculado da lista
    d: metade esquerda da lista
    e: metade direita da lista
    f: posição da lista à esquerda
    g: posição da lista à direita
    h: lista de resultado
    i: lista de sobra
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    RESPOSTA ~> O algoritmo não retorna o vetor de
    resultado (ordenado). Deveria ser acrescentada
    a seguinte linha no final da função:
    return h + i
"""

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = b[:c]
    e = b[c:]
    d = a(d)
    e = a(e)
    f = g = 0
    h = []
    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            h.append(d[f])
            f += 1
        else:
            h.append(e[g])
            g += 1
    i = []
    if f < g: i = d[f:]
    else: i = e[g:]