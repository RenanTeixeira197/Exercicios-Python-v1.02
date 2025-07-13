import tkinter as tk

janela = tk.Tk()
janela.title("Hello, World")
janela.geometry("400x200")

label = tk.Label(janela, text="Digite algo")
label.pack()

entrada = tk.Entry()
entrada.pack()


def clique():
    nome = entrada.get()
    label.config(text= f"O {nome} foi inserido com sucesso!")

Botao = tk.Button(janela, text="Clique Aqui",command=clique)
Botao.pack()

entrada02 = tk.Entry()
entrada02.pack()

def outro_clique():
    time = entrada02.get()
    label.config(text= f"Você torce para o {time}!")

Botao02 = tk.Button(janela, text="Pode Clicar!", command=outro_clique)
Botao02.pack()

janela.mainloop()