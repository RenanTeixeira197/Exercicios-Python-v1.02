#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Aprimore para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from typing import Dict, List

def main():
    """Função principal do programa."""
    
    jogadores: List[Dict[str, any]] = []

    while True:
        jogador: Dict[str, any] = {}
        jogador['nome'] = input('Nome do Jogador: ').strip().title()
        partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        jogador['partidas'] = partidas
        gols: List[int] = []

        for i in range(partidas):
            gols_partida = int(input(f'Quantos gols na partida {i + 1}? '))
            gols.append(gols_partida)

        jogador['gols'] = gols
        jogador['total_gols'] = sum(gols)
        jogadores.append(jogador)

        continuar = input('Deseja adicionar outro jogador? (s/n): ').strip().lower()
        if continuar != 's':
            break

    print('\nDados dos Jogadores:')
    for j in jogadores:
        print(f"\nNome: {j['nome']}")
        print(f"Partidas: {j['partidas']}")
        print(f"Gols por partida: {j['gols']}")
        print(f"Total de Gols: {j['total_gols']}")

    print('\nFim do programa.')