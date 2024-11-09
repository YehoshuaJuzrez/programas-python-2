# Dividir en cifras un numero entero

import os

print('Dividir en unidades, decenas y centenas un numero entero')
n = int(input('Dame un número de 3 cifras: '))

c = n//100
d = (n - (c * 100)) // 10
u = ( n - (c * 100 + d * 10))

print ('el numero original es:', n)
print ('centenas:', c)
print ('decenas:', d)
print ('unidades:', u)
print ('/n numero de la suerte:',  c + d + u)

