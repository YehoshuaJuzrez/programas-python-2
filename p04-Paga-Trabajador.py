# p04-Paga-Trabajador-Calcula la paga de un trabajador

print('Calculando la paga de un trabajador')

nombre = input("Dame tu nombre:")
horas = int(input("Horas:"))
paga = float(input("Paga por hora:"))
tasa = 0.3

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%")
print(f"Paga bruta: {pagabruta:,.2f}")
print(f"Impuessto: {impuesto:.2f}")
print(f"Paga neta: {paganeta:.2f}")