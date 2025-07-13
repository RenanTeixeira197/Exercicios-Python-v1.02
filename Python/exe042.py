 #Crie o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
 # além da idade, com quantos anos a pessoa vai se aposentar.rie um programa que leia nome, ano de nascimento e 
 # carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 

# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime
from time import sleep
from typing import Dict

def calcular_idade(ano_nascimento: int) -> int:
    """Calcula a idade com base no ano de nascimento."""
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def calcular_aposentadoria(ano_contratacao: int, idade: int) -> int:

    """Calcula os anos restantes para aposentadoria."""
    anos_aposentadoria = 35  # Considerando 35 anos de contribuição
    anos_restantes = anos_aposentadoria - (datetime.now().year - ano_contratacao)
    return anos_restantes if anos_restantes > 0 else 0

def main():
    """Função principal do programa."""
   
    trabalhador: Dict[str, any] = {}
    
    trabalhador['nome'] = input('Nome: ').strip().title()
    ano_nascimento = int(input('Ano de nascimento: '))
    trabalhador['idade'] = calcular_idade(ano_nascimento)
    
    carteira_trabalho = int(input('Carteira de Trabalho (0 se não tiver): '))
    
    if carteira_trabalho != 0:
        trabalhador['carteira_trabalho'] = carteira_trabalho
        ano_contratacao = int(input('Ano de contratação: '))
        trabalhador['ano_contratacao'] = ano_contratacao
        trabalhador['salario'] = float(input('Salário: R$ '))
        trabalhador['anos_aposentadoria'] = calcular_aposentadoria(ano_contratacao, trabalhador['idade'])
    else:
        trabalhador['carteira_trabalho'] = 'Não possui'
        trabalhador['anos_aposentadoria'] = 'N/A'
    
    print('\nDados do Trabalhador:')
    for chave, valor in trabalhador.items():
        print(f'{chave.title()}: {valor}')
    
    sleep(2)
    print('\nFim do programa.')