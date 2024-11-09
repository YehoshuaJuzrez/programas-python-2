## Tercer examen parcial

# Clase para representar a un jugador
class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        beca_str = "Becado" if self.becado else "Sin Beca"
        return f'Nombre: {self.nombre.ljust(20)} AñoNac: {str(self.año_nac).ljust(5)} Sexo: {self.sexo.ljust(6)} Becado: {beca_str}'


# Clase para representar una categoría de jugadores
class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        """Agrega un jugador a la categoría."""
        self.jugadores.append(jugador)

    def total_ingresos(self):
        """Calcula los ingresos totales de la categoría, considerando becas."""
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)

    def __str__(self):
        return f'Nombre: {self.nombre.ljust(10)}   Rango: {self.rango.ljust(15)}  Costo: ${self.costo:,.2f}'


# Clase para representar la academia de fútbol
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    # Métodos para agregar categorías y contar total de categorías
    def agregar_categoria(self, categoria):
        """Agrega una categoría a la academia."""
        self.categorias.append(categoria)

    def total_categorias(self):
        return len(self.categorias)

    # Métodos para contar total de hombres y mujeres
    def total_hombres(self):
        return sum(jugador.sexo == 'Hombre' for categoria in self.categorias for jugador in categoria.jugadores)

    def total_mujeres(self):
        return sum(jugador.sexo == 'Mujer' for categoria in self.categorias for jugador in categoria.jugadores)

    # Método para calcular ingresos totales
    def total_ingresos(self):
        return sum(categoria.total_ingresos() for categoria in self.categorias)

    # Método para generar un reporte de la academia
    def generar_reporte(self):
        """Genera un reporte detallado de la academia."""
        reporte = (f"REPORTE DEL CLUB DEPORTIVO\n\n"
                   f"Nombre: {self.nombre}\n"
                   f"Propietario: {self.propietario}\n"
                   f"Domicilio: {self.domicilio}\n\n"
                   f"Total de Categorías: {self.total_categorias()}\n"
                   f"Total de Hombres: {self.total_hombres()}\n"
                   f"Total de Mujeres: {self.total_mujeres()}\n\n")

        # Información de las categorías
        categorias_info = '\n'.join([str(categoria) for categoria in self.categorias])
        reporte += f">> Datos generales de las Categorías\n\n{categorias_info}\n\n"

        # Información detallada de jugadores en cada categoría
        jugadores_info = ''
        for categoria in self.categorias:
            jugadores_info += f'> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})\n'
            for jugador in categoria.jugadores:
                jugadores_info += f'{str(jugador)}\n'
            subtotal = categoria.total_ingresos()
            jugadores_info += f'\n- SubTotal : ${subtotal:,.2f}\n\n'

        reporte += f">> Jugadores por Categoría:\n\n{jugadores_info}"
        reporte += f"-> Total : ${self.total_ingresos():,.2f}"

        return reporte


# Función principal para crear la academia, categorías y jugadores
def main():
    # Creación de la academia
    academia = Academia("Academia Futbol Elite", "Yehoshua Juarez", "Avenida Futbolista 456, Ciudad Deportiva")

    # Creación de categorías
    cat1 = Categoria("Chavorucos", "2000/2001/2002", 1500.00)
    cat2 = Categoria("Adultos chidos", "2003/2004/2005", 1200.00)
    cat3 = Categoria("casi adultos", "2006/2007/2008", 1000.00)
    cat4 = Categoria("adolecentes", "2009/2010/2011", 900.00)
    cat5 = Categoria("morritos", "2012/2013/2014", 800.00)

    # Agregando jugadores a cada categoría
    cat1.agregar_jugador(Jugador("Carlos Vázquez", 2000, "Hombre", False))
    cat1.agregar_jugador(Jugador("Roberto González", 2001, "Hombre", True))
    cat1.agregar_jugador(Jugador("Lucía Pérez", 2002, "Mujer", False))

    cat2.agregar_jugador(Jugador("María López", 2003, "Mujer", True))
    cat2.agregar_jugador(Jugador("José Ramírez", 2004, "Hombre", False))
    cat2.agregar_jugador(Jugador("Ana Sánchez", 2005, "Mujer", True))

    cat3.agregar_jugador(Jugador("Pedro Torres", 2006, "Hombre", False))
    cat3.agregar_jugador(Jugador("Luis Medina", 2007, "Hombre", True))
    cat3.agregar_jugador(Jugador("Sofía Moreno", 2008, "Mujer", False))

    cat4.agregar_jugador(Jugador("Elena García", 2009, "Mujer", False))
    cat4.agregar_jugador(Jugador("Ricardo Soto", 2010, "Hombre", False))
    cat4.agregar_jugador(Jugador("Carla Jiménez", 2011, "Mujer", True))

    cat5.agregar_jugador(Jugador("Diego Martínez", 2012, "Hombre", False))
    cat5.agregar_jugador(Jugador("Valeria Ruiz", 2013, "Mujer", True))
    cat5.agregar_jugador(Jugador("Andrea Navarro", 2014, "Mujer", False))

    # Agregando categorías a la academia
    academia.agregar_categoria(cat1)
    academia.agregar_categoria(cat2)
    academia.agregar_categoria(cat3)
    academia.agregar_categoria(cat4)
    academia.agregar_categoria(cat5)

    print(academia.generar_reporte())

if __name__ == "__main__":
    main()
  # prueba