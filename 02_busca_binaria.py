# ALGORITMO DE BUSCA BINÁRIA
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na
# lista.

from data.primos import primos
from data.lista_nomes import nomes
from time import time

# Contador de comparações
comps = 0

def busca_binaria(lista, val):

    # "global" indica que estamos usando a variável que foi
    # declarada fora da função
    global comps
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        meio = (ini + fim) // 2      # Meio da lista

        # 1º caso: o valor na posição do meio da lista
        # corresponde ao valor buscado; ENCONTRAMOS e
        # retornamos a posição encontrada (meio)
        if val == lista[meio]:
            comps += 1      # comps = comps + 1
            return meio

        # 2º caso: o valor de busca é MAIOR que o valor no
        # meio da lista
        elif val > lista[meio]:
            comps += 2
            ini = meio + 1

        # 3º o valor de busca é MENOR que o valor no meio
        # da lista
        else:
            comps += 2
            fim = meio - 1

    # val não existe em lista
    return -1

# Buscando números primos
# hora_ini = time()
# print(f"Posição de 8008: {busca_binaria(primos, 8008)}, comps: {comps}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 8008: {(hora_fim - hora_ini) * 1000}ms")

# hora_ini = time()
# print(f"Posição de 1487: {busca_binaria(primos, 1487)}, comps: {comps}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 1487: {(hora_fim - hora_ini) * 1000}ms")

# hora_ini = time()
# print(f"Posição de 7603: {busca_binaria(primos, 7603)}, comps: {comps}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 7603: {(hora_fim - hora_ini) * 1000}ms")

# hora_ini = time()
# print(f"Posição de 401: {busca_binaria(primos, 401)}, comps: {comps}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 401: {(hora_fim - hora_ini) * 1000}ms")

# hora_ini = time()
# print(f"Posição de 7: {busca_binaria(primos, 7)}, comps: {comps}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 7: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ORKUTILSON: {busca_binaria(nomes, 'ORKUTILSON')}, comps: {comps}")
hora_fim = time()
print(f"Tempo gasto para buscar ORKUTILSON: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}, comps: {comps}")
hora_fim = time()
print(f"Tempo gasto para buscar FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}, comps: {comps}")
hora_fim = time()
print(f"Tempo gasto para buscar ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de AARAO: {busca_binaria(nomes, 'AARAO')}, comps: {comps}")
hora_fim = time()
print(f"Tempo gasto para buscar AARAO: {(hora_fim - hora_ini) * 1000}ms")