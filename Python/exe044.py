# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas B) 
# A média de idade C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip().title()
    pessoa['sexo'] = input('Sexo (M/F): ').strip().upper()
    while pessoa['sexo'] not in ('M', 'F'):
        print('Sexo inválido! Digite M ou F.')
        pessoa['sexo'] = input('Sexo (M/F): ').strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    
    pessoas.append(pessoa)
    
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar != 'S':
        break


total_pessoas = len(pessoas)
media_idade = sum(p['idade'] for p in pessoas) / total_pessoas if total_pessoas > 0 else 0
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
acima_media = [p['nome'] for p in pessoas if p['idade'] > media_idade]

print('\nDados Cadastrados:')
print(f'\nTotal de pessoas cadastradas: {total_pessoas}')
print(f'Média de idade: {media_idade:.2f}')
print(f'Mulheres cadastradas: {", ".join(mulheres) if mulheres else "Nenhuma"}')
print(f'Pessoas com idade acima da média: {", ".join(acima_media) if acima_media else "Nenhuma"}')
print('\nFim do programa.')