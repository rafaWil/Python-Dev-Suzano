"""
Herança múltipla em Python é um conceito da programação orientada a objetos onde uma classe pode herdar de duas ou mais classes ao mesmo tempo.

Ou seja, a classe "filha" (ou derivada) pode acessar os métodos e atributos de múltiplas superclasses.

"""
# Exemplo Prático
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

class Mamifero(Animal):
    def __init__(self, nro_patas, pelagem):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, nro_patas, cor_pena):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)

class Gato(Mamifero):
    pass


# Heranca Multipla
class Ornitorrinco(Mamifero, Ave):
    pass


