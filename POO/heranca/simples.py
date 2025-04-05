"""
===== HERANÇA ====

Em programação herança é a capacidade de uma classe filha derivar ou herdar as caraterísticas e comportamentos da classe pai(base).

==> É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

"""

# Herança Simples/Única ==> Exemplo

# Itens -> Classe PAI(VEICULO) -> Classes filhos(MOTOCICLETA) - (CARRO) - (CAMINHAO)

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    
        


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass
