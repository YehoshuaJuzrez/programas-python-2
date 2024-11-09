# Imprime la secuencia de números mostrados y el numero de renglones que el usuario desee

import os; os.system("clear")

n = int(input("Dame número ? "))

print("Salida:")
for x in range(1, n + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()  