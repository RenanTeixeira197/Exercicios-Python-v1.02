#Crie um programa onde 4 jogadores joguem um dado 
# e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.

import random

jogadores = {}

for i in range(1, 5):
    nome = input(f'Nome do jogador {i}: ')
    jogadores[nome] = random.randint(1, 6)
print('\nResultados dos Jogadores:')

for jogador, resultado in jogadores.items():
    print(f'{jogador} tirou {resultado}')
print('\nRanking dos Jogadores:')

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for posicao, (jogador, resultado) in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador} com {resultado}')
print('\nFim do programa.')
