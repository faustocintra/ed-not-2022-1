# O fatorial de um número n inteiro > 1 pode ser definido,
# recursivamente, como:
# n! = n * (n - 1)!
# Já o fatorial de n = 1 é definido como
# 1! = 1

# Implementção ITERATIVA de um fatorial
def fatorial_iter(n):
    resultado = 1
    # range começa em n e vai descendo até 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

# Implementação RECURSIVA de um fatorial
def fatorial_rec(n):
    if n == 1 or n == 0: 
        return 1    # Condição de saída
    elif n > 1: 
        return n * fatorial_rec(n - 1)
    else: # Números negativos
        return None # Condição de saída

# Função de fatorial recursiva sem condição de saída, para
# provocar "stack overflow"
def fatorial_overflow(n):
    return n * fatorial_overflow(n - 1)

################################################

#print(f"6! é igual a {fatorial_iter(6)}")
#print(f"31! é igual a {fatorial_iter(31)}")

print(f"6! é igual a {fatorial_rec(6)}")
print(f"31! é igual a {fatorial_rec(31)}")

# Aumentando o limite máximo de recursão
import sys
sys.setrecursionlimit(1000)

print(f"--> 6! é igual a {fatorial_overflow(6)}")