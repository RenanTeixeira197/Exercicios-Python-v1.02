class Main:
    pass

print("Testando o projeto")

from clientes import cliente

from conta import Conta

c1= cliente("Ana", "123444-2222")
conta=Conta(c1.nome, 6565,0)

print(c1)
print(conta.titular, "Numero: ", conta.numero, "Seu Saldo: ", conta.saldo)