# 1. Observe a lista de produtos abaixo.
#
# 2. Utilizando os recursos estudados durante o semestre, faça o necessário para
#    que seja possível efetuar uma busca binária na lista.
#
# 3. Por meio da busca binária, informe as posições dos seguintes itens:
#    - Laranja
#    - Bolacha
#    - Iogurte
#    - Leite condensado
#    - Pimenta do reino

"""
    Para o algoritmo de busca binária funcionar, precisamos antes ordenar a lista. (nesse caso, usei o Bubble Sort)
    
    Posição -1 = não existe na lista
"""

produtos = [
    'Farinha de trigo',
    'Arroz',
    'Macarrão',
    'Extrato de tomate',
    'Azeite de oliva',
    'Feijão',
    'Leite',
    'Ovos',
    'Iogurte',
    'Achocolatado',
    'Palmito',
    'Creme de leite',
    'Biscoito',
    'Pão de forma',
    'Margarina',
    'Alface',
    'Tomate',
    'Batata',
    'Frango',
    'Carne moída',
    'Café',
    'Alho',
    'Cebola',
    'Milho de pipoca',
    'Sal',
    'Açúcar',
    'Pimenta do reino',
    'Farinha de mandioca',
    'Fubá',
    'Queijo ralado',
    'Goiabada',
    'Sardinha',
    'Suco de uva',
    'Gelatina',
    'Maçã',
    'Banana',
    'Laranja',
    'Melancia',
    'Manga',
    'Cenoura'
]

def bubble_sort(lista):
    while True:

        trocou = False  

        for pos in range(len(lista) - 1):

            if lista[pos] > lista[pos + 1]:
                lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos]
                trocou = True
        if not trocou:
            break

bubble_sort(produtos)
print(produtos)

def busca_binaria(lista, val):
    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        meio = (ini + fim) // 2      # Meio da lista
        if val == lista[meio]:
            return meio
        elif val > lista[meio]:
         
            ini = meio + 1
        else:
        
            fim = meio - 1
    return -1


print(f"Posição de Laranja: {busca_binaria(produtos, 'Laranja')}")
print(f"Posição de Bolacha: {busca_binaria(produtos, 'Bolacha')}")
print(f"Posição de Iogurte: {busca_binaria(produtos, 'Iogurte')}")
print(f"Posição de Leite condensado: {busca_binaria(produtos, 'Leite condensado')}")
print(f"Posição de Pimenta do reino: {busca_binaria(produtos, 'Pimenta do reino')}")

