# CRIANDO SETS
"""
    >> Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
"""

# Exemplo
set([1, 2, 3, 1, 3, 4]) # {1,2,3,4}

set("abacaxi")  # {"b", "a", "c", "x", "i"}


# ACESSANDO OS DADOS
"""
    >> Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.
"""

# METODOS DA CLASSE SET
# 1. add() - Adiciona um elemento ao conjunto
# 2. discard() - Remove um elemento do conjunto, caso ele exista
# 3. pop() - Remove um elemento do conjunto, caso ele exista, e retorna
# 4. remove() - Remove um elemento do conjunto, caso ele exista
# 5. union() - Retorna um conjunto com todos os elementos dos conjuntos
# 6. intersection() - Retorna um conjunto com os elementos em comum entre os conjuntos
# 7. difference() - Retorna um conjunto com os elementos que estão em um conjunto e não 
# 8. symmetric_difference() - Retorna um conjunto com os elementos que estão em um conjunto 
# 9. isdisjoint() - Verifica se dois conjuntos são disjuntos
# 10. issuperset() - Verifica se um conjunto é superset de outro conjunto
# 11. issubset() - Verifica se um conjunto é subset de outro conjunto
# 12. copy() - Retorna uma cópia do conjunto
# 13. clear() - Remove todos os elementos do conjunto
# 14. len() - Retorna o tamanho do conjunto
# 15. update() - Atualiza o conjunto com os elementos de outro conjunto
# 16. union() - Retorna um conjunto com todos os elementos dos conjuntos
# 18. difference() - Retorna um conjunto com os elementos que estão em um conjunto e não
