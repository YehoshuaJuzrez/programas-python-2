#Cambiar los elementos de una lista de numeros

import os; os.system("clear")

nums=[10, 9, 8.5, 6.5, 7.5, 6.2, 9.5]

print('Cambiar o modificar los elementos de la lista')

print(type(nums))
print('La lista : ', nums, len(nums))

print('Modificar los elementos en las posiciones 0 y 1')
nums [0] = 7
nums [1] = 7
print('Resulta en : ', nums)

print('Modificar los elementos en las posiciones 2 y 5')

nums[2:5] = [9.9, 9.0, 9.0]
print('Resulta en : ', nums)
