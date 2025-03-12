"""
    ACESSO DIRETO
    
    >> A lista é uma sequencia, portanto podemos acessar seus dados utilizando indices. Contamos o indice de determinada sequencia a partir de zero.
"""

# Exemplo com lista de frutas
frutas = ['maçã', 'banana', 'laranja', 'morango']
print(frutas[0])  # Acessa a primeira posição da lista (maçã)
print(frutas[3])  # Acessa a quarta posição da lista (morango)

print(frutas[-1]) # Acessa a última posição da lista (morango)


# Exemplo lista aninhadas
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [5, 6, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"