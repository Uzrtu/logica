'''
import random

num_int = random.randint(1, 100)
print(f"\nNúmero aleatório entre 1 e 100: {num_int}")
'''

import random

def imprime_matriz(matriz):
    for linha in range(1):
        for coluna in range(3):
            print(matriz[linha][coluna], end=" ")
    print()

while True:
    matriz = [[random.randint(1, 10) for coluna in range(3)] for linha in range(1)]
    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        imprime_matriz(matriz)
        print("Parabéns você ganhou!")
    else:
        imprime_matriz(matriz)
        print("Você perdeu, tente novamente!")
    continua = input("\nDeseja continuar?[s, n]: ").lower()
    if continua == "n":
        break