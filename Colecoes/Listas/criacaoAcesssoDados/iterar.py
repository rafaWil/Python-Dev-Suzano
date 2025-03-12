"""
    ITERAR 
    
    >> A forma mais comum para percorrer os dados de uma lista é utilizando o comando FOR.
"""

# Exemplo
carros = ["Porsche", "BMW", "Civic", "Ferrari"]

for c in carros:
    print(c)
    
# Funcao ENUMERATE para indicar o indice de cada valor
for indice, c in enumerate(carros):
    print(f"Indice: {indice}, Carro: {c}")