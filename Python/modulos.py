def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, taxa=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, taxa=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def porcentagem(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def resumo(preço, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, formato=True)}')
    print(f'Metade do preço: {metade(preço, formato=True)}')
    print(f'Aumento de {taxa}%: {aumentar(preço, taxa, formato=True)}')
    print(f'Diminuição de {taxar}%: {diminuir(preço, taxar, formato=True)}')
    print('-' * 30)


def resumo_formatado(preço, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, formato=True)}')
    print(f'Metade do preço: {metade(preço, formato=True)}')
    print(f'Aumento de {taxa}%: {aumentar(preço, taxa, formato=True)}')
    print(f'Diminuição de {taxar}%: {diminuir(preço, taxar, formato=True)}')
    print('-' * 30)
    print(f'Valor formatado: {moeda(preço)}')
    print('-' * 30)