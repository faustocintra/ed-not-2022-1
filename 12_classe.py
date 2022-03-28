# Classe é uma estrutura que representa conjuntamente
# dados e algoritmos. Uma classe é como uma "forma de bolo"
# com a qual se pode criar diferentes "bolos" (objetos),
# variando os "ingredientes" (dados) e o "modo de fazer"
# (algoritmos). Apesar dessa variação, os objetos criados
# a partir da classe sempre terão o formato determinado por
# esta.

from math import pi

class FormaGeometrica:

    # Uma classe pode ter, dentro de si, tanto dados quanto
    # funções (estas representando os algoritmos). Uma função
    # especial, denominada __init__, é chamada sempre que um
    # novo objeto é criado a partir da classe, sendo conhecida
    # como CONSTRUTOR.
    # Quando estão dentro de uma classe, as funções passam a
    # ser chamadas MÉTODOS, e *sempre* têm self como primeiro
    # parâmetro, representando o próprio objeto.
    
    def __init__(self, base, altura, tipo):

        # Recebemos os parâmetros no construtor e
        # armazenamos dentro do objeto que está sendo
        # criado
        self.base = base
        self.altura = altura
        self.tipo = tipo

######################################################

# Criando objetos a partir da classe
forma1 = FormaGeometrica(12, 7, "R")    # Isso chama __init__()
forma2 = FormaGeometrica(7.5, 8.2, "T")

print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}")
print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}")
