import sqlite3

banco = sqlite3.connect('casa_de_racao.db')
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS racoes (
    marca TEXT,
    valor REAL,
    quantidade INTEGER,
    lote INTEGER,
    data_validade TEXT
)
""")

try:
    marca = input("Marca: ")
    valor = float(input("Valor Atacado: "))
    quantidade = int(input("Quantidade: "))
    lote = int(input("Número do lote: "))
    data_validade = input("Data de validade (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO racoes VALUES (?, ?, ?, ?, ?)",
        (marca, valor, quantidade, lote, data_validade)
    )
    banco.commit()

except ValueError:
    print("ERRO! Tente novamente")
except sqlite3.Error as erro:
    print(f"Erro no SQLite: {erro}")
finally:
    banco.close()
