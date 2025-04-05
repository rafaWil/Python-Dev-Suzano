"""
===== HERANÇA ====

Em programação herança é a capacidade de uma classe filha derivar ou herdar as caraterísticas e comportamentos da classe pai(base).

==> É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

"""

# Herança Simples/Única ==> Exemplo

# Itens -> Classe PAI(VEICULO) -> Classes filhos(MOTOCICLETA) - (CARRO) - (CAMINHAO)

class Veiculo:
    # Atributos
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    # Comportamentos/Métodos
    def ligar_motor(self):
        print("Ligando o motor...")
        print("Motor ligado!")
        
    def desligar_motor(self):
        print("Desligando o motor...")
        print("Motor desligado!")
        
    def acelerando(self):
        print("Acelerando...")
    


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass
