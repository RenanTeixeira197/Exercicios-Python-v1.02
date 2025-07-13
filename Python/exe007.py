def area_trapezio(b1, b2, altura):
    return (b1 + b2) * altura / 2

base1 = float(input("Base 1 do trapezio: "))
base2 = float(input("Base 2 do trapezio: "))
altura = float(input("Altura do trapezio: "))

total = area_trapezio(base1, base2, altura)

print("A área total do trapézio é de: ", total)