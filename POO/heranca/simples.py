"""
===== HERANÇA ====

Em programação herança é a capacidade de uma classe filha derivar ou herdar as caraterísticas e comportamentos da classe pai(base).

==> É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

"""

# Herança Simples/Única ==> Exemplo

# Itens -> Classe PAI(VEICULO) -> Classes filhos(MOTOCICLETA) - (CARRO) - (CAMINHAO)

class Veiculo:
    # Atributos
    def __init__(self, cor, placa, numero_rodas, modelo):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.modelo = modelo
        
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
    def __init__(self, carregado, cor, placa, numero_rodas, modelo):
        super().__init__(cor, placa, numero_rodas, modelo)
        self.carregado = carregado
    
    # Metodo
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Instancias de objetos das classes e seus atributos e metodos
moto = Motocicleta("preta", "abc-1234", 2, "Fazer")
print(moto.modelo, moto.placa, moto.cor)
moto.ligar_motor()
moto.acelerando()

print("\n")

carro = Carro("branca", "cba-4321", 4, "Porsche")
print(carro.modelo, carro.placa, carro.cor)
carro.ligar_motor()
carro.acelerando()

print("\n")

caminhao = Caminhao(False, "cinza", "wzy-0000", 12, "Mercedez")
print(caminhao.modelo, caminhao.placa, caminhao.cor)
caminhao.esta_carregado()
caminhao.ligar_motor()
caminhao.acelerando()