lista = []

for i in range(2):
    while True:
        cadastro_livros = {
            'titulo': "",
            'autor': "",
            'editora': "",
            'edição': 0,
            'ano': 0,
        }
        try:
            cadastro_livros['titulo'] = input("Título do Livro: ")
            cadastro_livros['autor'] = input("Autor: ")
            cadastro_livros['editora'] = input("Editora: ")
            cadastro_livros['edição'] = int(input("Edição: "))
            cadastro_livros['ano'] = int(input("Ano: "))
            lista.append(cadastro_livros)
            break  # Sai do while se tudo estiver correto
        except ValueError:
            print("Dados Inválidos! Tente novamente.")

for i, livro in enumerate(lista):
    print(f"\nDados Cadastrados na posição {i}")
    print("Título:", livro['titulo'])
    print("Autor:", livro['autor'])
    print("Editora:", livro['editora'])
    print("Edição:", livro['edição'])
    print("Ano:", livro['ano'])