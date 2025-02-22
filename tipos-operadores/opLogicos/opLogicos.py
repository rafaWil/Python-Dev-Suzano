"""
Exemplo de Comparacao 
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque) 
# >>> Resultado deve ser TRUE

print(saque <= limite)
# >>> Resultado deve ser FALSE
"""

# Operador E(AND)
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
# Deve retornar -> FALSE

# Operador Ou(OR)
saldo = 1000
saque = 200
limite = 100
print(saldo >= saque or saque <= limite)
# Deve retornar -> TRUE

# Operador de Negação NOT
saldo = 1000
saque = 200
limite = 100
print(not(saldo >= saque and saque <= limite))
# Deve retornar -> TRUE