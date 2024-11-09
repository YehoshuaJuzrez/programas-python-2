#Lee datos y envia un saludo

print('Leyendo datos y enviando un saludo:\n')

nombre = input('Dame tu nombre:') #lee cadena
edad = int(input('Dame la edad:'))#Lee cadena y conviertete en entero
peso = float(input('Dame tu peso'))#Lee cadena y conviertete en float

print(f'{nombre} bienvenido a python, tu edad es de {edad}, tu peso es de {peso}')
print(type(nombre))
print(type(edad))
print(type(peso))