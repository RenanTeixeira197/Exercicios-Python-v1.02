lista = []

for i in range(2):

    while True:
        cadastrar_contatos = {
            'nome': "",
            'telefone': 0,
            'email': "",
        }
        try:
            cadastrar_contatos['nome'] = input("Nome:")
            cadastrar_contatos['telefone'] = int(input("Telefone: "))
            break
        except ValueError:
            print("Telefone Inválido! Digite apenas números.")
           
    cadastrar_contatos['email'] = input("E-mail: ")
    lista.append(cadastrar_contatos)


for i, contatos in enumerate(lista):
    print("Dados de cadastro na posição", i)
    print("Nome:", contatos['nome'])
    print("Telefone:", contatos['telefone'])
    print("Email:", contatos['email'])


    