class Animal:
    def __init__(self, nome, especie, raca, cor, porte, idade):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.cor = cor
        self.porte = porte
        self.idade = idade

    def apresentacao(self):
        return f'''Foi incluido em nossa base de dados o pet:
                   -------------------------------------------------
                   Nome: {self.nome}
                   Especie: {self.especie}
                   Raca: {self.raca}
                   Cor: {self.cor}
                   Porte: {self.porte}
                   Idade: {self.idade}
                   --------------------------------------------------
    '''


dados_pet = Animal('Nego', 'Cachorro', 'Vira-Lata', 'Preto', 'Medio', 10)
print(dados_pet.apresentacao())