#Agregar elementos a una lista de numeros

import os; os.system("clear")

nums = [80.3, 12.5, 60.2, 30.4]
print('Agregar elementos a una lista de numeros')

print('Los numeros : ', nums, len(nums))

print('Agregar dos elementos adicionales')
nums.append(90)
nums.append(100)
print('Queda : ', nums, len(nums))

print('Insertar elemento en la posicion 1')
nums.insert(1,85.5)
print('Queda : ', nums, len(nums))

print('Insertar un rango de elementos')
nums.extend([110,120,130])
print('Queda : ', nums, len(nums))
