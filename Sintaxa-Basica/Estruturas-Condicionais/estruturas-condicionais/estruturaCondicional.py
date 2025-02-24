# Oque são?
# Permite o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas.

# Exemplo com IF
saldo = 2000.0
saque = float(input("Informe o valor de saque: "))

if  saldo >= saque:
    print("Realizando Saque...")

if saldo <= saque:
    print("Saldo Insuficiente!")