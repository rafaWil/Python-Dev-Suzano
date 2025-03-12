# APPEND
    # é um método usado para adicionar um elemento ao final de uma lista.

# Exemplo
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # Resultado => [1, "Python", [40, 30, 20]]

# COPY
lista2 = [1, "Python", [40,30,20]]

# Não é a mesma lista
lista2.copy()
print(lista2) # Resultado => [1, "Python", [40, 30,20]] 

# Para se certificar de que sao listas diferentes, vemos pelo id
print(id(lista2)) 
print(id(lista.copy())) 