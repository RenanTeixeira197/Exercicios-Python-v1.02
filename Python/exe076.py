def cabeçalho():
    print("-" * 30)
    print("CONVERSOR QUILOS/LIBRAS".center(30))
    print("-" * 30)


def converter(quilos):
    return quilos * 2.20462


cabeçalho()

quilos = float(input("Informe o peso em quilos (Kg): "))

resultado = converter(quilos)

print(f'O peso {quilos}Kg convertido para libras: {resultado}Lb ')
