#Desafio 03 - Crie a classse chamada Churrasco, onde seja possível informar, quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa. Considere 400g por pessoa e preço: 82,40/kg.


class Churrasco():
    def __init__(self, num_pessoas):
        self.num_pessoas = num_pessoas
        self.custo_por_kg = 82.40
        self.carne_por_pessoa = 0.4  # 400g em kg
        
    def calcular_carne_total(self):
        return self.num_pessoas * self.carne_por_pessoa
    
    def calcular_custo_total(self):
        carne_total = self.calcular_carne_total()
        return carne_total * self.custo_por_kg
    
    def calcular_preco_por_pessoa(self):
        custo_total = self.calcular_custo_total()
        return custo_total / self.num_pessoas
    

num_pessoas = 10
churrasco = Churrasco(num_pessoas)
carne_total = churrasco.calcular_carne_total()
custo_total = churrasco.calcular_custo_total()
preco_por_pessoa = churrasco.calcular_preco_por_pessoa()
print(f'Numero de pessoas: {num_pessoas}')
print(f'Carne total necessaria: {carne_total:.2f} kg')
print(f'Custo total do churrasco: R$ {custo_total:.2f}')
print(f'Preco por pessoa: R$ {preco_por_pessoa:.2f}')
