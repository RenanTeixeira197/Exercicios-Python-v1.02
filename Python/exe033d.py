from random import randint
from time import sleep
lista = []
jogos = []

print('$'*30)
print("          MEGA SENA          ")
print('$'* 30)
quant = int(input("Quantos numeros voce quer que eu sorteie?: "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
           lista.append(num)
           cont += 1
        if cont >= 6:
           break
    lista.sort
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *3, f'SORTEANDO {quant} JOGOS', '-=' * 3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa Sorte!')