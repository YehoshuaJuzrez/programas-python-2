# Imprime los pares de 2 a n y su suma

import os; os.system("clear")

n = int(input("Dame un número: "))

suma = 0
print("Salida:", end=" ")
for x in range(2, n + 1, 2):
    print(x, end=" ")
    suma += x

print(f", La suma es = {suma}")