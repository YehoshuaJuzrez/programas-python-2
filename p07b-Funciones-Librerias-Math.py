# ejemplifica el uso de algunas funciones de la libreria math

import math as mt

w=10.34
x=10
y=20
z=35

print(f'los numeros son: {x},{y},{z}')
print(f'maximo comun divisor: {mt.gcd(x,y,z)}')
print(f'valor maximo:{max(x,y,z)}')
print(f'valor minimo:{min(x,y,z)}')
print(f'elevar a una potencia:{pow(x,y)}\n')

print(f'redondear hacia arriba:{mt.ceil(w)}')
print(f'redondear hacia abajo:{mt.floor(w)}')
print(f'redondear:{round(w)}')
print(f'tunc :{mt.trunc(w)}')