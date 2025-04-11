"""
Modificadores de Acesso

=> Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos
e métodos da classe. Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada.

PÚBLICO => Pode ser acessado de fora da classe.
PRIVADO => Só pode ser acessasdo pela classe.

Todos os recursos são públicos, a menos que o nome inicie com UNDERLINE. Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por UNDERLINE, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.

"""

# Exemplo
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        #...
        self._saldo += valor
    
    def sacar(self, valor):
        #...
        self._saldo -= valor
        
    def mostrar_saldo(self):
        # ...
        return self._saldo
    
# Instanciando
conta = Conta("001", 100)
conta.depositar(20) # Vai somar 20 a mais no saldo da conta
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())