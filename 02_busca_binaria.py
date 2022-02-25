# ALGORITMO DE BUSCA BINÁRIA
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na
# lista.

def busca_binaria(lista, val):
    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        meio = (ini + fim) // 2      # Meio da lista

        # 1º caso: o valor na posição do meio da lista
        # corresponde ao valor buscado; ENCONTRAMOS e
        # retornamos a posição encontrada (meio)
        if val == lista[meio]:
            return meio

        # 2º caso: o valor de busca é MAIOR que o valor no
        # meio da lista
        elif val > lista[meio]:
            ini = meio + 1

        # 3º o valor de busca é MENOR que o valor no meio
        # da lista
        else:
            fim = meio - 1