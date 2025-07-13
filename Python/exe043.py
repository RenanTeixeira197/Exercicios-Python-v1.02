#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from typing import Dict, List

def main():
    """Função principal do programa."""
    
    jogador: Dict[str, any] = {}

    jogador['nome'] = input('Nome do Jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? q'))
    jogador['partidas'] = partidas
    gols: List[int] = []

    for i in range(partidas):
        gols_partida = int(input(f'Quantos gols na partida {i + 1}? '))
        gols.append(gols_partida)

    jogador['gols'] = gols
    jogador['total_gols'] = sum(gols)

    print('\nDados do Jogador:')
    for chave, valor in jogador.items():
        if chave == 'gols':
            print(f'{chave.title()}: {valor} (Total: {jogador["total_gols"]})')
        else:
            print(f'{chave.title()}: {valor}')

    print('\nFim do programa.')