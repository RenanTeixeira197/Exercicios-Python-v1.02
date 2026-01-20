class ContaBancaria():
    '''
    Docstring para ContaBancaria
    Cria uma conta bancária com atributos de titular e saldo.
    
    '''
    
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        
    def __str__(self):
        return f'A Conta {self.id} de {self.nome} tem {self.saldo} de Saldo'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de {valor:,.2f} realizado com sucesso!')
    
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente para saque!')
        else:
            self.saldo -= valor
            print(f'Saque de {valor:,.2f} realizado com sucesso!')
        
    
    

c1 = ContaBancaria(1, 'Riquelme', 10000)
c1.depositar(5000)
c1.sacar(200)


print(c1)