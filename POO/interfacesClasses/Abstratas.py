"""
Criando Classes ABSTRATAS com o módulo ABC
//ABC

==> Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod.

""" 
# Exemplo
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")
        
    def desligar(self):
        print("TV desligada")
        
controle = ControleTV()
controle.ligar()  # TV ligada
controle.desligar()  # TV desligada

