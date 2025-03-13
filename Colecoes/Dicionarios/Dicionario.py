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


# DICIONARIOS ANINHADOS
"""
    ==> Dicionarios podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como(strings e números)
"""
# Exemplo
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-0000"},
    "joao@gmail.com": {"nome":"João", "telefone":"1111-111"},
    "david@gmail.com": {"nome":"David", "telefone":"2222-2222"},
    "raquel@gmail.com": {"nome":"Raquel", "telefone":"4444-4444"},
}


# ITERAR
"""
    ==> A forma mais comum para percorrer os dados de um dicionário é utilizando o comando FOR
"""
# Exemplo
for chave, valor in contatos.items():
    print(f"Chave: {chave} - Valor: {valor}")