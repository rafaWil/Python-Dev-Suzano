"""
=>> Atributos do Objeto

Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância
são diferentes para cada objeto(cada objeto tem uma cópia), já os atributos de classe são compartilhadas entre
os objetos.

"""

# Exemplo 
class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
wil = Estudante("Wilson", 23456)
kel = Estudante("Raquel", 12345)

print(wil)
print(kel)