# Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0
 
    #Metodos de Instância
    
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos.")

#Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Ana"
g1.idade = 20
g1.aniversario()
print(g1.mensagem())