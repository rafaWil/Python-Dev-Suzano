# Exemplo
class Passaro:
    def voar(self):
        pass
    
class Pardal(Passaro):
    def voar(self):
        print("O pardal voa")
        
class Avestruz(Passaro):
    def voar(self):
        print("O avestruz não voa")
        
def plano_de_voo(passaro):
    passaro.voar()
    
plano_de_voo(Pardal())
plano_de_voo(Avestruz())