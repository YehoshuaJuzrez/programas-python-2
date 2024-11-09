# Calcular el area de un circulo

print('Calculando el area de un circulo:\n')
print("Dame el radio: ")
      
radio = float(input())

area = 3.1416 * radio * radio

print(f'El circulo de radio {radio} tiene un area de {area}')

# Calcular el area de un circulo con librerias

import math

print('Calculando el area de un circulo:\n')
print('Dame el radio: ')
      
radio = float(input())
area = math.pi * radio ** 2
print(f'El circulo de radio {radio} tiene un area de {area:.2f}')