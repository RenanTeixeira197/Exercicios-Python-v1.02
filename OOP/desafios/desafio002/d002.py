#Desafio 02 - Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.


class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        return f'Produto: {self.nome} - R${self.preco:.2f}'
    


p1 = Produto('Notebook', 3500.00)
print(p1.etiqueta())    

p2 = Produto('Smartphone', 1500.00)
print(p2.etiqueta())