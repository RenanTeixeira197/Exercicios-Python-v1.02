import sqlite3

banco = sqlite3.connect('tarefas.db')


class ListaDeTarefas(object):
    def __init__(self):
        self.cursor = banco.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEREGER PRIMARY KEY, tarefa TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS concluida (id INTEREGER PRIMARY KEY, tarefa TEXT)')
    
    def adicionar_tarefa(self, tarefa):
        self.cursor.execute('INSERT INTO tarefas (tarefa) VALUES (?)', (tarefa,))
        banco.commit()
    
    def listar_tarefas(self):
        self.cursor.execute('SELECT * FROM tarefas')
        return self.cursor.fetchall()
    
    def concluir_tarefa(self, tarefa_id):
        self.cursor.execute('SELECT * FROM tarefas WHERE id = ?', (tarefa_id,))
        tarefa = self.cursor.fetchone()
        if tarefa:
            self.cursor.execute('INSERT INTO concluida (id, tarefa) VALUES (?, ?)', (tarefa[0], tarefa[1]))
            self.cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
            banco.commit()
        else:
            print("Tarefa não encontrada.")
    def listar_concluidas(self):
        self.cursor.execute('SELECT * FROM concluida')
        return self.cursor.fetchall()
    
    def fechar(self):
        self.cursor.close()
        banco.close()
    
# Exemplo de uso
if __name__ == "__main__":
    lista = ListaDeTarefas()
    lista.adicionar_tarefa("Estudar Python")
    lista.adicionar_tarefa("Fazer compras")
    
    print("Tarefas pendentes:")
    for tarefa in lista.listar_tarefas():
        print(tarefa)
    
    lista.concluir_tarefa(1)
    
    print("\nTarefas concluídas:")
    for tarefa in lista.listar_concluidas():
        print(tarefa)
    
    lista.fechar()