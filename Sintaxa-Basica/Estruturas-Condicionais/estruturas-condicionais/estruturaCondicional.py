# Oque são?
# Permite o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas.

# Bibliotecas OS e SYS
import os
import sys

# Exemplo com IF
saldo = 2000.0
saque = float(input("Informe o valor de saque: "))

if  saldo >= saque:
    print("Realizando Saque...")

if saldo < saque:
    print("Saldo Insuficiente!")
    
# Exemplo com IF ELSE
saldo = 2000.0
saque = float(input("Informe o valor de saque: "))

if  saldo >= saque:
    print("Realizando Saque...")
else:
    print("Saldo Insuficiente!")
    
# Exemplo com IF ELIF ELSE
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    print("Realizando saque no valor de ", valor, "...")
elif opcao == 2:
    print("Exibindo Extrato...")
else:
    sys.exit("Opcao Invalida!")