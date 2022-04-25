"""
    ESTRUTURA DE DADOS PILHA (STACK)
    É uma estrutura de dados linear em que tanto
    a operação de inserção (push) quanto a operação
    de retirada (pop) acontecem no final (ou topo).
    Como consequência, o funcionamento da pilha
    pode ser definido como LIFO (Last In, First Out):
    o último a entrar é o primeiro a sair.
"""

# Usando uma pilha rudimentar para inverter um texto
#texto = 'PINDAMONHANGABA'
texto = 'SOCORRAM ME SUBI NO ONIBUS EM MARROCOS'

# Em Python, é possível fazer com que uma lista se
# comporte como uma pilha
pilha = []

# Colocando cada uma das letras do texto no 
# final da pilha
for letra in texto:
    pilha.append(letra)

print(pilha)

inverso = ''

# Enquanto houver elementos na pilha
while len(pilha) > 0:
    retirado = pilha.pop()
    inverso += retirado

print('Original:  ', texto)
print('Invertido: ', inverso)