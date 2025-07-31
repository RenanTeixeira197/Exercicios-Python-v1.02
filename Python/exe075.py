celsius = 0

def cabeçalho():
    print("*" * 30)
    print("Conversor Celsius > Fahrenheit".center(30))
    print("*" * 30)


def conversor():
    return (celsius * 9.5) + 32


cabeçalho()

celsius = float(input("Informe a temperatura em graus celsius para a conversao: "))

resultado = conversor()

conversao = print(f'A temperatura {celsius}°C em Fahrenheit é: {resultado}°F!')

"""
celsius = 0  # Variável global

def cabeçalho():
    print("*" * 30)
    print("Conversor Celsius > Fahrenheit".center(30))
    print("*" * 30)

def conversor():
    global celsius  # Declare que vai usar a variável global
    celsius = float(input("Informe a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9.5) + 32
    return fahrenheit

cabeçalho()
resultado = conversor()

print(f"A temperatura {celsius}°C em Fahrenheit é: {resultado}°F!")

"""

"""
EXEMPLO SEM USO DE VARIÁVEL GLOBAL:

def cabeçalho():
    print("*" * 30)
    print("Conversor Celsius > Fahrenheit".center(30))
    print("*" * 30)


def conversor(celsius):
    return (celsius * 9.5) + 32


cabeçalho()

celsius = float(input("Informe a temperatura em graus Celsius para a conversão: "))
resultado = conversor(celsius)

print(f'A temperatura {celsius}°C em Fahrenheit é: {resultado}°F!')

"""