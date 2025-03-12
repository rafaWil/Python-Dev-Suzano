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



# COUNT
lista3 = ["Porsche", "BMW", "Camaro", "BMW", "Civic"]
print(lista3.count("BMW")) # Resultado => 2
print(lista3.count("Civic")) # Resultado => 1
print(lista3.count("Ferrari")) # Resultado => 0
# O método count() é usado para contar o número de vezes que um elemento aparece em uma lista



# EXTEND
lista4 = ["Js", "C++", "Java"]
print(lista4)

lista4.extend(["Python", "Ruby"])
print(lista4) # Resultado => ['Js', 'C++', 'Java', 'Python, 'Ruby]



# INDEX
lista5 = ["oi", "ola", "bye", "good"]

print(lista5.index("bye")) # Resultado => 2


# POP
lista6 = ["oi", "ola", "bye", "good"]
print(lista6.pop()) # Resultado => "good"
print(lista6) # Resultado => ['oi', 'ola', 'bye']
# O método pop() é usado para remover o último elemento de uma lista e retorná-lo.


# REMOVE
lista7 = ["oi", "ola", "bye", "good"]
print(lista7.remove("bye")) # Resultado => None
print(lista7) # Resultado => ['oi', 'ola', 'good']
# O método remove() é usado para remover o primeiro elemento de uma lista que seja igual ao argument


# REVERSE
lista8 = ["oi", "ola", "bye", "good"]
print(lista8.reverse()) # Resultado => None
print(lista8) # Resultado => ['good', 'bye', 'ola', 'oi']
# O método reverse() é usado para inverter a ordem dos elementos de uma lista.



# SORT
lista9 = ["oi", "ola", "bye", "good"]
print(lista9.sort()) # Resultado => None
print(lista9) # Resultado => ['bye', 'good', 'oi', 'ola']
# O método sort() é usado para ordenar os elementos de uma lista em ordem alfabetica


# LEN
lista10 = ["oi", "ola", "bye", "good"]
print(len(lista10)) # Resultado => 4
# O método len() é usado para calcular o número de elementos de uma lista.


# SORTED
lista11 = ["oi", "ola", "bye", "good"]
print(sorted(lista11)) # Resultado => ['bye', 'good', 'oi', 'ola']