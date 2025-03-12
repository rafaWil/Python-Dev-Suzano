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