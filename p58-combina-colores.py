# Genera todas las combinaciones posibles entre los colores dados por el usuario 
import os

os.system("clear")
colores = input("Ingresa colores separados por espacio: ").split()
print(colores)

for color1 in colores:
    for color2 in colores:
        if color1 != color2:
            print(f"{color1.strip()} y {color2.strip()}")
    print()