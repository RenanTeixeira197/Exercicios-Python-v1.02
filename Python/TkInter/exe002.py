import tkinter as tk

janela = tk.Tk()
janela.title("Passo02")
janela.geometry("800x400")

label = tk.Label(janela, text="Informe algo:")
label.pack()

entrada = tk.Entry(janela)
entrada.pack()

def click():
    nome = entrada.get()
    label.config(text=f"Olá {nome}!")

Botao = tk.Button(janela, text="Clique Aqui", command=click)
Botao.pack()

label_resultado = tk.Label(janela, text="")
label.pack()


janela.mainloop()