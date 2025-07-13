import math

def area_circulo(raio):
    area = math.pi * raio ** 2
    return area

def perimetro_circulo(raio):
    perimetro = 2 * math.pi * raio
    return perimetro 

raio_circulo = float(input("Informe o raio: "))

print("A área do círculo é: ", round(area_circulo(raio_circulo), 2))
print("O Perímetro do círculo é: ", round(perimetro_circulo(raio_circulo), 2))