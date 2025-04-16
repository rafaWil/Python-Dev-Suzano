"""
MÉTODOS DE CLASSE

=> Estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.


"""
# Exemplo
class Pessoa:
    populacao = 0  # Atributo da classe, compartilhado entre todas as instâncias

    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    @classmethod
    def quantidade_pessoas(cls):  # cls representa a classe, não uma instância
        return f"Existem {cls.populacao} pessoas cadastradas."

# Criando algumas pessoas
p1 = Pessoa("Alice")
p2 = Pessoa("Bob")

# Chamando o método de classe
print(Pessoa.quantidade_pessoas())
print(p1.nome)
print(p2.nome)


"""
@classmethod: Decorador que transforma o método para receber a classe como primeiro parâmetro (convenção: cls).

cls.populacao: Acessa o atributo da classe, não de uma instância específica.

Pessoa.quantidade_pessoas(): Pode ser chamado direto pela classe, sem precisar de um objeto.
"""
