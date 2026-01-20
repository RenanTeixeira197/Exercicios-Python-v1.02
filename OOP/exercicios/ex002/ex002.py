class Gafanhoto:
    '''
    Declaracao de Classe
    
    '''
    def __init__(self, n = "", i = 0): #Método Construtor
        #Atributos de Instância
        self.nome = n
        self.idade = i
 
    #Metodos de Instância
    
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos.")

#Declaração de Objetos
g1 = Gafanhoto("Ana", 20)
g1.aniversario()
print(g1.mensagem())

print(Gafanhoto.__doc__)

print(g1.__dict__) #Imprime o dicionário de atributos do objeto
print(g1.__getstate__() ) #Imprime o estado do objeto
print(g1.__class__) #Imprime a classe do objeto

g2 = Gafanhoto("Breno", 22)
print(g2.__getstate__())