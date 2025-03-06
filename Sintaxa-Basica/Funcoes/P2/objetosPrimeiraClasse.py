"""
    Em Python tudo é objeto, dessa forma funçoes tambem sao objetos o que os torna objetos de primeira classe.
    Com isso podemos atribuir funcoes a variaveis, passa-las como parametro para funcoes, usa-las como valores em estruturas
    de dados e usar como valor de retorno para uma funcao.
"""

# Exemplo
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
