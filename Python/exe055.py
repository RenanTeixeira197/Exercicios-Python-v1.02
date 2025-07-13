#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    Calcula o fatorial de um número n.
    
    :param n: Número a calcular o fatorial.
    :param show: Se True, mostra o processo de cálculo.
    :return: Fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            if i == n:
                print(f"{i}", end="")
            else:
                print(f" x {i}", end="")
                if show and i == 1:
                    print(" = ", end="")
    if show:
        print(f)
    return f

# Programa principal
def main():
    print(fatorial(5, show=True))
    print(fatorial(4, show=False))
    print(fatorial(6, show=True))
if __name__ == "__main__":
    main()
    