# Iterar por los elementos de una lista de numeros
import os; os.system("clear")

nums = [2,4,6,8,10,12,14,16]
print('Iterando sobre los elementos de una lista')

print('Numeros : ', nums, len(nums))

print('\nIterar usando un ciclo for ')
for num in nums:
    print(num, end=' ')

print('\nIterar usando el subindice positivo usando un ciclo for')
for i in range(len(nums)):
    print(nums[i], end=' ')

print('\nMostrar el arreglo donde a cada elemento se le suma 2')
for num in nums:
    print(num+2, end=' ')
print('\nQueda : ', nums)

print('Elevar al cuadradp cada elemento del arreglo')
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print('Queda : ', nums)
