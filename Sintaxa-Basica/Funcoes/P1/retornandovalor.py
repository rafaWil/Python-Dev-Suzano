"""
    RETORNANDO VALORES
    
    Para retornar um valor, utilizamos a palavra reservada RETURN.    
    Toda funcao Python retorna NONE por padrao. Diferente de outras linguagens de programaçao,
    em Python uma funcao pode retornar mais de um valor.
"""

# EXEMPLO

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
antecessor, sucessor = retorna_antecessor_e_sucessor(10) # (9, 11)

print(antecessor, sucessor)