import sqlite3

conn = sqlite3.connect('rolleta_calçados.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS calçados(
    marca TEXT,
    preço REAL,
    qtde_estoque INTEGER 
)
""")
conn.commit()

try:
    marca = input("Marca do calçado: ")
    preço = float(input("preço: "))
    qtde_estoque = int(input("Quantidade: "))

    cursor.execute(
        "INSERT INTO calçados VALUES (?, ?, ?)",
        (marca, preço, qtde_estoque)
    )
    conn.commit()

except ValueError:
    print("ERRO! Tente novamente")
except sqlite3.Error as erro:
    print(f"Erro no SQLite: {erro}")
finally:
    conn.close()

