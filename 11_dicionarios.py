# Um dicionário é uma estrutura de dados fornecida pela linguagem Python
# capaz de armazenar múltiplos valores em uma única variável, por meio
# de pares de chave-valor.

pessoa = {
    # "nome" é a chave
    # "Gervásio Gomes Garcia" é o valor
    "nome": "Gervásio Gomes Garcia",
    "sexo": "M",
    "idade": 69,
    "peso": 76,
    "altura": 1.77
}

# Acessando os valores armazenados no dicionário
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Calculando o Índice de Massa Corpórea (IMC)
imc = pessoa["peso"] / pessoa["altura"] ** 2

print(f"IMC: {imc}")

########################################################

# Formas geométricas representadas na forma de dicionário

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"     # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse
}

forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "R"     # Retângulo
}

# Forma geométrica completamente anômala
forma5 = {
    "base": "batata",
    "altura": "jabuticaba",
    "tipo": "T"     # Triângulo
}

# Inserindo as formas em uma lista para percorrer com for
lista_formas = [forma1, forma2, forma3, forma4, forma5]

# Função que calcula a área de uma forma de acordo com a base, a altura e o tipo

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":    # Retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":  # Triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":  # Elipse
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else:   # Forma desconhecida
        # Gera um erro
        raise Exception("ERRO: tipo de forma não reconhecido.")

# Calculando a área das formas da lista

for i in range(0, len(lista_formas)):
    print("-" * 30)
    print(f"Calculando área da forma{i + 1}:")
    print(f"Tipo: {lista_formas[i]['tipo']}; base: {lista_formas[i]['base']}; altura: {lista_formas[i]['altura']}; ÁREA: {calcular_area(lista_formas[i])}")