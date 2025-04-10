"""
Herança múltipla em Python é um conceito da programação orientada a objetos onde uma classe pode herdar de duas ou mais classes ao mesmo tempo.

Ou seja, a classe "filha" (ou derivada) pode acessar os métodos e atributos de múltiplas superclasses.

"""
# Exemplo Prático
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass


# Heranca Multipla
class Ornitorrinco(Mamifero, Ave):
    pass

ornitorrinco = Ornitorrinco(2, "vermelho", "laranja")
print(ornitorrinco) 