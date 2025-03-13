# CRIANDO TUPLAS
"""
    >> Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas
    são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe TUPLE, ou colocando valores separados por vírgula de parenteses.
"""

# Exemplo de Tuplas
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

# Exemplo de acesso a uma tupla
print(frutas[0])  # imprime: laranja
print(letras[0])  # imprime: p
print(numeros[1])  # imprime: 2
print(pais[0])  # imprime: Brasil