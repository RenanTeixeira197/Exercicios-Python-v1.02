import sqlite3

banco = sqlite3.connect('livros.db')
cursor = banco.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS livro (nome TEXT, ano INTEGER, preco INTEGER, volumes INTEGER)')

try:
    nome = input("Nome do Livro: ")
    ano = int(input("Ano de lançamento: "))
    preco = int(input("Valor(R$): "))
    volumes = int(input("Volumes: "))

    cursor.execute(
        "INSERT INTO livro VALUES (?, ?, ?, ?)",
        (nome, ano, preco, volumes)
    )
    banco.commit()

except ValueError:
    print("Para de fazer gambiarra jumento!!")
except sqlite3.Error as erro:
    print(f"Erro no SQLite: {erro}")
finally:
    banco.close()
