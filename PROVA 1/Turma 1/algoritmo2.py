"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de busca sequencial
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    a: função de busca sequencial
    b: lista onde será feita a busca
    c: valor a ser buscado
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    RESPOSTA ~>
    A variável c corresponde ao valor de busca e,
    portanto, não poderia ser usada para controlar
    a posição do for. Uma nova variável (d, por exemplo),
    deveria ser usada no for e a linha seguinte deveria
    ser corrigda para:
    if b[d] == c: return d
"""

def a(b, c):
    for c in range(len(b)):
        if b[c] == c: return c
    return -1