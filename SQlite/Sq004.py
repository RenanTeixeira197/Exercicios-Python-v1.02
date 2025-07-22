import sqlite3

banco = sqlite3.connect('primeiro_banco.db')


cursor = banco.cursor()

#cursor.execute("INSERT INTO pessoas VALUES('Solange',34,'nill_123@gmail.com')")

cursor.execute("UPDATE pessoas SET nome = 'Elisangela' WHERE idade = 34")


banco.commit()