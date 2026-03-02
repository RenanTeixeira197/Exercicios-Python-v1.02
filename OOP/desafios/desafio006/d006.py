#Sistema de Gestão de Bibliotecas - Pequeno- Módulo de Empréstimo de Livros


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"Livro({self.titulo!r}, {self.autor!r})"


class Biblioteca:
    def __init__(self):
        # Livros disponíveis para empréstimo
        self.livros_disponiveis = []
        # Livros emprestados
        self.livros_emprestados = []

    def __str__(self):
        disponiveis = [l.titulo for l in self.livros_disponiveis]
        emprestados = [l.titulo for l in self.livros_emprestados]
        return (
            f"Livros disponiveis: {disponiveis}\n"
            f"Livros emprestados: {emprestados}"
        )

    def adicionar_livro(self, livro):
        self.livros_disponiveis.append(livro)
        return f'Livro "{livro.titulo}" adicionado a biblioteca.'

    def emprestar_livro(self, titulo):
        for livro in list(self.livros_disponiveis):
            if livro.titulo == titulo:
                self.livros_disponiveis.remove(livro)
                self.livros_emprestados.append(livro)
                return f'Livro "{titulo}" emprestado com sucesso.'
        return f'Livro "{titulo}" nao encontrado na biblioteca ou indisponivel para emprestimo.'

    def devolver_livro(self, titulo):
        for livro in list(self.livros_emprestados):
            if livro.titulo == titulo:
                self.livros_emprestados.remove(livro)
                self.livros_disponiveis.append(livro)
                return f'Livro "{titulo}" devolvido com sucesso.'
        return f'Livro "{titulo}" não encontrado na lista de empréstimos.'
        
# Exemplo de uso

biblioteca = Biblioteca()

livro1 = Livro("O Pequeno Principe", "Antoine de Saint-Exupéry")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("Curso Intensivo de MySQL", "Rick Silva")
livro4 = Livro("Coraline", "Neil Gaiman")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

#print(biblioteca.adicionar_livro(livro1))
#print(biblioteca.adicionar_livro(livro2))
#print(biblioteca.adicionar_livro(livro3))
#print(biblioteca.adicionar_livro(livro4))

#Livros Disponíveis:
print(biblioteca)

#Livro emprestado:
print(biblioteca.emprestar_livro("Dom Quixote"))
print(biblioteca)

#Livro que já havia sido emprstado e sofreu uma segunda tentativa de emprestimo:
print(biblioteca.emprestar_livro("Dom Quixote"))

#Livro que não consta na biblioteca

print(biblioteca.emprestar_livro("Star Wars"))
print(biblioteca)

#Livro Devolvido:

print(biblioteca.devolver_livro("Dom Quixote"))
print(biblioteca)



