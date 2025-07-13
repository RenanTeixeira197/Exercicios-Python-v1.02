import tkinter as tk

janela = tk.Tk()
janela.title("Usando grid()")
janela.geometry("400x200")

# Label
label = tk.Label(janela, text="Digite seu nome:")
label.grid(row=0, column=0)

# Entry
entrada = tk.Entry(janela)
entrada.grid(row=0, column=1)

# Função do botão
def botão_clicado():
    nome = entrada.get()
    label_resultado.config(text=f"Olá, {nome}!")

# Botão
botao = tk.Button(janela, text="Clique aqui", command=botão_clicado)
botao.grid(row=1, column=0, columnspan=2)

# Label resultado
label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=2, column=0, columnspan=2)

janela.mainloop()
