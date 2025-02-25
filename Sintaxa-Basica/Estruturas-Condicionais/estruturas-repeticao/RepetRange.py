# Função Range

"""
    Range é uma função built-in do Python, ela é usada para produzir uma sequencia de numeros inteiros
    a partir de um inicio(inclusivo) para um fim(exclusivo). Se usarmos range(i,j) será produzido:
    
    i, i+1, i+2, i+3,....j-1.
    Ela recebe 3 argumentos: STOP(Obrigatório), START(Opcional) e STEP OPCIONAL.
"""

# Utilizando range com FOR
for numero in range(0,11):
    print(numero, end=" ")
print("\n")
# Resultado 0 1 2 3 4 5 6 7 8 9 10

# Outro exemplo -> Tabuada de 5
for num in range(0, 51, 5):
    print(num, end=" ")