import sqlite3
try:
  
  banco = sqlite3.connect('primeiro_banco.db')
  
  cursor = banco.cursor()

  cursor.execute("DELETE from pessoas WHERE idade = 30")

  banco.commit()
  banco.close()
  print("Os dados foram removidos com sucesso!!")

except sqlite3.Error as erro:
  print("ERRO! Os dados nao foram exluídos", erro)