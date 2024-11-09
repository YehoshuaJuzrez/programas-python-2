# Imprime la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

import os; os.system("clear")
import math

n = int(input("¿Cuántos términos? "))

suma = 0
salida = []

print("Salida:", end=" ")

for i in range(1, n + 1):
    termino = 1 / math.factorial(i)
    salida.append(f"1/{i}!")
    suma += termino

print(" + ".join(salida), end=" , suma: ")
print(suma)