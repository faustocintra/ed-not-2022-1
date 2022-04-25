"""
    1) Identifique o algoritmo abaixo.
    RESPOSTA ~> Algoritmo de ordenação Selection Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    RESPOSTA ~>
    a: função do algoritmo de ordenação
    b: a lista a ser ordenada
    c: função auxiliar que encontra o menor
    d: posição inicial do vetor
    e: posição final do vetor
    f: posição do menor valor
    g: posição de percurso no for (função auxiliar)
    h: posição de percurso no for (função principal)
    i: posição do menor retornada pela função auxiliar
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
    RESPOSTA ~>
    A função auxiliar c está retornando o valor errado.
    O correto seria
    return f

"""

def a(b):
    def c(d, e):
        f = d
        for g in range(d + 1, e + 1):
            if b[g] < b[f]:
                f = g
        return g
    for h in range(len(b) - 1):
        i = c(h + 1, len(b) - 1)
        if b[i] < b[h]:
            b[i], b[h] = b[h], b[i]