import tkinter as tk
from tkinter import messagebox
import csv
import os

# Lista para armazenar os cômodos e áreas
comodos = []
area_total = 0

# Função para adicionar cômodo
def calcular_area():
    global area_total
    try:
        nome = entrada_nome.get().strip().title()
        largura = float(entrada_largura.get())
        comprimento = float(entrada_comprimento.get())
        area = largura * comprimento

        comodos.append((nome, largura, comprimento, area))
        area_total += area
        lista_comodos.insert(tk.END, f"{nome}: {area:.2f} m²")

        entrada_nome.delete(0, tk.END)
        entrada_largura.delete(0, tk.END)
        entrada_comprimento.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos!")

# Função para finalizar e mostrar total
def finalizar():
    messagebox.showinfo("Área Total", f"Área total do imóvel: {area_total:.2f} m²")

# Função para remover um cômodo selecionado
def remover():
    global area_total
    try:
        indice = lista_comodos.curselection()[0]
        nome, larg, comp, area = comodos.pop(indice)
        area_total -= area
        lista_comodos.delete(indice)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um cômodo para remover.")

# Função para salvar como .csv
def salvar_csv():
    if not comodos:
        messagebox.showwarning("Aviso", "Nenhum cômodo para salvar.")
        return

    with open("relatorio_area.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Cômodo", "Largura (m)", "Comprimento (m)", "Área (m²)"])
        for nome, larg, comp, area in comodos:
            writer.writerow([nome, larg, comp, area])
        writer.writerow(["TOTAL", "", "", area_total])

    messagebox.showinfo("Sucesso", "Relatório CSV salvo com sucesso!")

# Interface
janela = tk.Tk()
janela.title("Calculadora de Área em m²")

# Entradas
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Nome do cômodo:").grid(row=0, column=0, padx=5, sticky="e")
entrada_nome = tk.Entry(frame_entrada, width=30)
entrada_nome.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Largura (m):").grid(row=1, column=0, padx=5, sticky="e")
entrada_largura = tk.Entry(frame_entrada)
entrada_largura.grid(row=1, column=1, padx=5)

tk.Label(frame_entrada, text="Comprimento (m):").grid(row=2, column=0, padx=5, sticky="e")
entrada_comprimento = tk.Entry(frame_entrada)
entrada_comprimento.grid(row=2, column=1, padx=5)

# Botões de controle
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_adicionar = tk.Button(frame_botoes, text="Adicionar Cômodo", command=calcular_area)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover Selecionado", command=remover)
btn_remover.grid(row=0, column=1, padx=5)

btn_salvar = tk.Button(frame_botoes, text="Salvar CSV", command=salvar_csv)
btn_salvar.grid(row=0, column=2, padx=5)

btn_finalizar = tk.Button(frame_botoes, text="Finalizar e Ver Total", command=finalizar, bg="green", fg="white")
btn_finalizar.grid(row=0, column=3, padx=5)

# Lista de cômodos
tk.Label(janela, text="Cômodos adicionados:").pack()
lista_comodos = tk.Listbox(janela, width=50)
lista_comodos.pack(pady=5)

# Iniciar interface
janela.mainloop()
