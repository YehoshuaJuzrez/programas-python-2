# Sistema de control de ventas
print("Bienvenido al sistema de inscripciones de la Universidad Patito")

ventas_totales = 0  # Acumular las ventas diarias

while True:
    print("\nElige una categoría de usuario:")
    print("1. Estudiante ($100)")
    print("2. Trabajador ($200)")
    print("3. Profesor ($500)")
    
    usuario = int(input("Introduce el número correspondiente a tu tipo de usuario: "))
    
    if usuario == 1:
        costo_usuario = 100
        tipo_usuario = "Estudiante"
        porcentaje_desc = 0.20
    elif usuario == 2:
        costo_usuario = 200
        tipo_usuario = "Trabajador"
        porcentaje_desc = 0.10
    elif usuario == 3:
        costo_usuario = 500
        tipo_usuario = "Profesor"
        porcentaje_desc = 0.05
    else:
        print("Error: Tipo de usuario inválido, por favor intenta nuevamente.")
        continue

    print("\nSelecciona un paquete de inscripción:")
    print("1. Solo conferencias ($600)")
    print("2. Conferencias + eventos sociales ($800)")
    print("3. Conferencias + kit de bienvenida ($900)")

    paquete = int(input("Introduce el número correspondiente al paquete: "))

    if paquete == 1:
        costo_paquete = 600
        tipo_paquete = "Solo conferencias"
    elif paquete == 2:
        costo_paquete = 800
        tipo_paquete = "Conferencias + eventos sociales"
    elif paquete == 3:
        costo_paquete = 900
        tipo_paquete = "Conferencias + kit de bienvenida"
    else:
        print("Error: Paquete no válido, intenta de nuevo.")
        continue

    # Pedir la cantidad de inscripciones
    inscripciones = int(input("\n¿Cuántas inscripciones deseas realizar? "))

    # Calcular el costo total antes del descuento
    precio_bruto = (costo_usuario + costo_paquete) * inscripciones

    # Aplicar descuentos si corresponde
    if precio_bruto > 5000:
        descuento = precio_bruto * porcentaje_desc
    else:
        descuento = 0

    precio_final = precio_bruto - descuento

    # Mostrar los detalles de la compra
    print(f"\nResumen de tu compra:")
    print(f"- Usuario: {tipo_usuario}")
    print(f"- Paquete: {tipo_paquete}")
    print(f"- Total de inscripciones: {inscripciones}")
    print(f"- Subtotal: ${precio_bruto:.2f}")
    print(f"- Descuento aplicado: ${descuento:.2f}")
    print(f"- Total a pagar: ${precio_final:.2f}")

    # Sumar al total del día
    ventas_totales += precio_final

    # Preguntar si se desea continuar
    continuar = input("\n¿Quieres procesar otra inscripción? (S/N): ").upper()
    if continuar == "N":
        print(f"\nTotal de ventas del día: ${ventas_totales:.2f}")
        print("Gracias por utilizar el sistema de inscripción. ¡Hasta pronto!")
        break