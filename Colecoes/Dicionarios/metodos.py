# CLEAR
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-0000"},
    "joao@gmail.com": {"nome":"João", "telefone":"1111-111"},
    "david@gmail.com": {"nome":"David", "telefone":"2222-2222"},
    "raquel@gmail.com": {"nome":"Raquel", "telefone":"4444-4444"},
}

contatos.clear()
contatos # {} Apagando todos os valores


# COPY
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-0000"},
    "joao@gmail.com": {"nome":"João", "telefone":"1111-111"},
    "david@gmail.com": {"nome":"David", "telefone":"2222-2222"},
    "raquel@gmail.com": {"nome":"Raquel", "telefone":"4444-4444"},
}
contatos_copia = contatos.copy()


# FROMKEYS
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

# Outra situação
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# EXEMPLO
carro = dict.fromkeys(["modelo_escape", "modelo_motor"], "esportivo")
print(carro)



# GET
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"}
}

# contatos["chave"] # KeyError

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {}
print(contatos.get("wilson@gmail.com", {})) # {"wilson@gmail.com": {"nome": "wilson", "telefone": "0000-0000"}