
def cabeçalho():
    print("*" * 30)
    print("Conversor Celsius > Fahrenheit".center(30))
    print("*" * 30)


def conversor(celsius):
    total = (celsius * 9.5) + 32


cabeçalho()

temperatura = float(input("Informe a temperatura em graus celsius para a conversao: "))

resultado = conversor(temperatura)

conversao = print(f'A temperatura {temperatura}°C em Fahrenheit é: {resultado}°F!')