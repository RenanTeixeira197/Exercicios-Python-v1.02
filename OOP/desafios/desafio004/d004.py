#Desafio 04 - Crie a classe livro que vai simular a passagem de páginas de um livro. considerando também se o usuário chegou ao fim da leitura.


class Livro():
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.pagina_atual = 0
        
    def passar_pagina(self):
        if self.pagina_atual < self.total_paginas:
            self.pagina_atual += 1
            return f'Você passou para a página {self.pagina_atual}.'
        else:
            return 'Você já chegou ao fim do livro.'
    
    def voltar_pagina(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            return f'Você voltou para a página {self.pagina_atual}.'
        else:
            return 'Você já está na primeira página.'
    
    def status_leitura(self):
        if self.pagina_atual == self.total_paginas:
            return 'Parabéns! Você terminou de ler o livro.'
        else:
            return f'Você está na página {self.pagina_atual} de {self.total_paginas}.'
        
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1000)
print(livro1.status_leitura())
print(livro1.passar_pagina())
print(livro1.passar_pagina())
print(livro1.voltar_pagina())
print(livro1.status_leitura())
