# - Calcula el area de un triangulo

print('Calculando el area de un triangulo:\n')
print('Dame la base y la altura separados por un Enter')
      
base, altura = int(input()), int(input())
area = base * altura / 2
print(f"El triangulo de base {base} y altura {altura} tiene un area de {area:.2f}")