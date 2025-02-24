# Oque são Estruturas de Repetição

# Estruturas de repetição são usadas para executar um bloco de código várias
# vezes. Elas são usadas para processar coleções de dados, como listas,
# tuplas, dicionários, conjuntos, etc.
# Existem dois tipos de estruturas de repetição em Python: for e while.
# O for é usado para iterar sobre uma coleção de dados, enquanto o while é
# usado para executar um bloco de código enquanto uma condição for verdadeira.

# FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    
print()
