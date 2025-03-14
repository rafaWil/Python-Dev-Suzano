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


# ITEMS
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"}
}

print(contatos.items()) # Retornar a lista de itens encontrados


# KEYS
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"}
}

print(contatos.keys()) # Retorna apenas as chaves


# POP
contatos = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"}
}

print(contatos.pop("wilson@gmail.com"))


# POP ITEMS
contatos2 = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"}
}

print(contatos2.popitem()) # ("wilson@gmail.com": {"nome":"wilson", "telefone":"0000-000"})



# SET DEFAULT
contatos3 = {'nome': 'Wilson', 'telefone': '1111-2222'}

contatos3.setdefault('nome', 'Raquel') # "Wilson"
contatos3 # {'nome': 'Wilson', 'telefone': '1111-2222'}

contatos3.setdefault("idade", 22) # 22
contatos3 # {'nome': 'Wilson', 'telefone': '1111-2222', 'idade': 22}



# update
contatos4 = {
    "wilson@gmail.com": {"nome": "Wilson", "telefone": "2222-2222"}
}

contatos4.update({"wilson@gmail.com" : {"nome": "Rafael"}})
print(contatos4) # {"wilson@gmail.com": {"nome": "Rafael"}}


# VALUES
contatos5 = {
    "wilson@gmail.com": {"nome":"wilson", "telefone":"0000-0000"},
    "joao@gmail.com": {"nome":"João", "telefone":"1111-111"},
    "david@gmail.com": {"nome":"David", "telefone":"2222-2222"},
    "raquel@gmail.com": {"nome":"Raquel", "telefone":"4444-4444"},
}

print(contatos5.values())