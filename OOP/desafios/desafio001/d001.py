#Desafio 01 - Crie a classe funcionário, onde podemos cadastrar, nome, setor e cargo. Crie também um método que permita o funcionário se apresentar.


class funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self):
        return f'Olá, meu nome é {self.nome}, trabalho no setor de {self.setor} e meu cargo é {self.cargo}.'
    
    

c1 = funcionario('Riquelme', 'TI', 'Analista de Sistemas')
print(c1.apresentacao())

c2 = funcionario('Maria', 'RH', 'Gerente de Recursos Humanos')
print(c2.apresentacao())
