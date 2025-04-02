"""
Joao tem uma bicicleta e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde Joao informe: COR, MODELO, ANO e VALOR da bicicleta vendida. 
Uma bicicleta pode: BUZINAR, PARAR e CORRRE. 
Adicione esses comportamentos!
"""

# Criando uma classe representando BICICLETA
class Bicicleta:
    # Construtor
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor # SELF é uma referencia para o objeto
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    # Metodo Buzinar
    def buzinar(self):
        print("Plim Plim")
        
    # Metodo Parar
    def parar(self):
        print("Parando...")
        print("Bicicleta Parada!")
        
    # Correr
    def correr(self):
        print("Vrummm...")
    
# Instanciando com variavel
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Add metodos a variavel
b1.buzinar()
b1.parar()
b1.correr()

# Imprimindo seus atributos
print(b1.cor, b1.modelo, b1.ano, b1.valor)



# Criando outra Instancia
b2 = Bicicleta("azul", "caloi", 2025, 550)
b2.correr()

print(b2.cor, b2.modelo, b2.valor)