import sqlite3

conn = sqlite3.connect('tera_byte.db')
cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS aluno(
   nome TEXT,
   cpf  TEXT,
   email TEXT,
   curso TEXT
)
""")
conn.commit()

try:
   nome = input("Nome do aluno: ")
   cpf = input("CPF (apenas números): ")
   if not cpf.isdigit() or len(cpf) != 11:
      raise ValueError("CPF inválido. Deve ter 11 dígitos numéricos.")
   
   email = input("Email: ")
   curso = input("Curso escolhido: ")

   cursor.execute(
      "INSERT INTO aluno VALUES(?, ?, ?, ?)",
      (nome, cpf, email, curso)
   )
   conn.commit()
   print("Aluno cadastrado com sucesso!")

except ValueError as ve:
   print(f"ERRO! {ve}")
except sqlite3.Error as erro:
   print(f'Erro no banco de dados: {erro}')
finally:
   conn.close()
