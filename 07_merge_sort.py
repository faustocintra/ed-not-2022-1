#   ALGORITMO DE ORDENAÇÃO MERGE SORT
#
#   No processo de ordenação, esse algoritmo "desmonta" o vetor original
#   contendo N elementos até obter N vetores de apenas um elemento cada um.
#   Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
#   dessa vez com os elementos já em ordem.

def merge_sort(lista):

    # print(f"Lista recebida: {lista}")

    # Só continua se o comprimento da lista for maior que 1
    if len(lista) <= 1: return lista

    # Encontra a posição do meio da lista
    meio = len(lista) // 2

    # Cópia da primeira metade do vetor
    sublista_esq = lista[:meio]
    # Cópia da segunda metade do vetor
    sublista_dir = lista[meio:]

    # Chamamos recursivamente a função para que ela continue
    # repartindo cada uma das sublistas em metades
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A JUNÇÃO DAS DUAS METADES DA LISTA, ORDENADAMENTE
    pos_esq = pos_dir = 0
    ordenada = []   # Lista vazia

    # Compara os elementos da sublista entre si e insere na
    # lista ordenada o que for menor
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        # O elemento que se encontra na posição da sublista esquerda
        # é menor que o que se encontra na posição da sublista direita
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    # Verificação da sobra
    sobra = []

    # Sobra à esquerda
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    # Sobra à direita
    else: sobra = sublista_dir[pos_dir:]

    # O resultado final é a concatenação da lista ordenada
    # com a sobra
    return ordenada + sobra

###############################################################

nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
resultado = merge_sort(nums)
print(resultado)