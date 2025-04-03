# Metodo CONSTRUTOR
"""
O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.

"""

# Método DESTRUTOR
"""
O método destrutor sempre é executado quando uma instância(objeto) é destruída. Destrutores em Python não são tão necessário quanto em C++ porque o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__.

"""

# Exemplo
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância da classe.")
        
    def falar(self):
        print("AuAu")
        
    
c = Cachorro("Romeu", "laranjado")
c.falar()       