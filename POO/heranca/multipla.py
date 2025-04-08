"""
Herança múltipla em Python é um conceito da programação orientada a objetos onde uma classe pode herdar de duas ou mais classes ao mesmo tempo.

Ou seja, a classe "filha" (ou derivada) pode acessar os métodos e atributos de múltiplas superclasses.

"""
# Exemplo Prático
class Animal:
    pass

class Mamifero(Animal):
    pass

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Avee(Animal):
    pass

# Heranca Multipla
class Ornitorrinco(Mamifero, Ave):
    pass