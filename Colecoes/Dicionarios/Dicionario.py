# DICIONARIOS

"""
    ==> Um dicionario é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave: valor separada por vírgulas.
""" 

# Exemplo
pessoa = {
    "nome": "Wilson",
    "idade": 22,
}
# Adicionando chave a um dicionario
pessoa["telefone"] = "3333-3333" # pessoa = {"nome": "Wilson", "idade": 22, "telefone": "3333-3333"} 

# Usando dict e passando dois parametros
ex2_pessoa = dict(nome = "Wilson", idade = 22)


print(pessoa)
print(ex2_pessoa) 