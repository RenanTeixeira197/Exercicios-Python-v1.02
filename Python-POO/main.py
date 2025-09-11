class Main:
    pass

print("Testando o projeto")

from clientes import cliente

from conta import Conta

c1= cliente("Ana", "123444-2222")
conta=Conta(c1.get_nome(), 6565,0)

conta.deposita(1000)
conta.saque(50)
conta.extrato()

print(c1)
print(conta.titular, "Numero: ", conta.numero, "Seu Saldo: ", conta.saldo)