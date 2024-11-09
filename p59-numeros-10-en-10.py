# Imprime los números de 1 a n de 10 en 10

import os; os.system("clear")

n = int(input("Dame un número: "))

print("Salida:", end=" ")
for x in range(1, n + 1, 10):
    print(x, end=" ")