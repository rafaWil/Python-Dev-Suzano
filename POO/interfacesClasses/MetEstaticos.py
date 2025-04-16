"""
MÉTODOS ESTÁTICOS

=> Não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. 
Este também não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.


DIFERENÇAS

==> Um método de CLASSE recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.

==> Um método de CLASSE pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.


QUANDO DEVEMOS UTILIZAR UM DOS MÉTODOS

==> Geralmente usamos o método de classe para criar métodos de fábrica.

==> Geralmente usamos métodos estáticos para criar funções utilitárias.


"""
# Exemplo
class Calculadora:
    
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def eh_par(numero):
        return numero % 2 == 0

# Usando os métodos estáticos
print(Calculadora.somar(10, 5))        # Saída: 15
print(Calculadora.eh_par(8))           # Saída: True
print(Calculadora.eh_par(7))           # Saída: False


"""
@staticmethod: Transforma a função em um método estático, que não recebe self (instância) nem cls (classe) como primeiro parâmetro.

Ele não acessa nenhum atributo ou método da classe. Apenas executa sua lógica como uma função normal, mas organizada dentro da classe.

Faz sentido estar dentro da classe Calculadora porque são operações que têm relação lógica com ela, mas não dependem de estado interno.

""" 