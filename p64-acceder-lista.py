# Acceder a los elementos de una lista de numeros

import os; os.system("clear")

#     0   1   2   3   4   5   6   7   8   9
nums=[10, 20, 30, 40, 50, 60, 70, 10, 20, 99]
#     -9  -8  -7  -6  -5  -4  -3  -2  -1  0

print('Acceder a los elementos de una lista')
print('La lista       : ', nums)
print('# Elementos    : ', len(nums))
print('\nAcceder con indices positivos 0 .. 8')
print('Primero        : ', nums[0])
print('Ultimo         : ', nums[8])
print('Del 2 al 6     : ', nums[2:6])
print('Primeros 3     : ', nums[:3])
print('Ultimos 3      : ', nums[6:])
print('\nAcceder con indices positivos -9 .. -1')
print('Primero        : ', nums[-9])
print('Ultimo         : ', nums[-1])
print('Del 2 al 6     : ', nums[-7:-2])
print('Primeros 3     : ', nums[:-6])
print('Ultimos 3      : ', nums[-3:])
