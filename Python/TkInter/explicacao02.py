import tkinter as tk

janela = tk.Tk()
janela.title("Widgets Básicos")
janela.geometry("400x200")

# Label - texto na tela
label = tk.Label(janela, text="Digite seu nome:")
label.pack()  # pack() posiciona o widget na janela

# Entry - campo de texto
entrada = tk.Entry(janela)
entrada.pack()

# Função que será chamada ao clicar no botão
def botão_clicado():
    nome = entrada.get()  # pega o texto digitado
    label_resultado.config(text=f"Olá, {nome}!")

# Botão
botao = tk.Button(janela, text="Clique aqui", command=botão_clicado)
botao.pack()

# Label que mostrará o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
