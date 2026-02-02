import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criação do DataFrame

df_salarios = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
    'Salario': [5000, 6000, 5800, 7000, 6500],
    'Departamento': ['Vendas', 'Marketing', 'Vendas', 'TI', 'Marketing']
})

#df_salarios.head() # Exibe as primeiras linhas do DataFrame
#df_salarios.info() # Informações sobre o DataFrame

# Estatísticas Descritivas
#df_salarios.describe() # Estatísticas descritivas do DataFrame
#df_salarios['Salario'].mean() # Média dos salários

# Filtragem de Dados

#df_vendas = df_salarios[df_salarios['Departamento'] == 'Vendas'] # Filtra funcionários do departamento de Vendas
#df_vendas.head() # Exibe as primeiras linhas do DataFrame filtrado
df_salarios[df_salarios['Salario'] < 6000] # Filtra funcionários com salário menor que 6000

#exibir o resultado na tela:
#print(df_vendas)

df_salarios[df_salarios['Salario'] < 6000]

# Agrupamento de Dados
df_media_salario = df_salarios.groupby('Departamento')['Salario'].mean().reset_index() # Média salarial por departamento
#print(df_media_salario)


#Adicionar novos funcionários nos departamentos
novos_funcionarios = pd.DataFrame({
    'Nome': ['Carolina', 'Felipe', 'Renan', 'Julia'],
    'Salario': [6500, 7200, 8400, 6900],
    'Departamento': ['TI', 'Vendas', 'Marketing', 'TI']
})

df_salarios = pd.concat([df_salarios, novos_funcionarios], ignore_index=True) # Adiciona novos funcionários ao DataFrame original

# Exibir o DataFrame atualizado
#print(df_salarios)

#Grafico de linhas 
'''
plt.figure(figsize=(10,5))
plt.plot(df_salarios['Nome'], df_salarios['Salario'], marker='o')
plt.title('Salários dos Funcionários')
plt.xlabel('Nome')
plt.ylabel('Salário')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

'''
#Gráfico de barras
'''
plt.figure(figsize=(10,5))
plt.bar(df_salarios['Nome'], df_salarios['Salario'], color='skyblue')
plt.title('Salários dos Funcionários')
plt.xlabel('Nome')
plt.ylabel('Salário')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
'''

#Gráfico de pizza
plt.figure(figsize=(8,8))
df_departamento_counts = df_salarios['Departamento'].value_counts()
plt.pie(df_departamento_counts, labels=df_departamento_counts.index.tolist(), autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Funcionários por Departamento')
plt.show()