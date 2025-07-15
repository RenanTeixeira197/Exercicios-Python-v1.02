def reverter_nome(nome):
    return nome[::-1]


nome_normal = str(input("Informe seu nome: "))

nome_ao_contrario = reverter_nome(nome_normal)

print(f'Nome Original: {nome_normal} o mesmo nome ao contrário fica: {nome_ao_contrario}')