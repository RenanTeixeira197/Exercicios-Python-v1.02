#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Média do aluno: '))


if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'


print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')


print('-=' * 30)
print(f'{"Dicionário do Aluno":^60}')
print('-=' * 30)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')
print('-=' * 30)
print('Fim do programa.')