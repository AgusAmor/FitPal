
class Membresia:
    def __init__(self, id_membresia, nombre, precio, beneficios):
        self.id_membresia = id_membresia
        self.nombre = nombre
        self.precio = precio
        self.beneficios = beneficios

    def mostrar_membresia(self):
        print(f"Membresía ID: {self.id_membresia}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Beneficios: {', '.join(self.beneficios)}\n")

def main():
    # creamos membresias ficticias 
    membresia1 = Membresia(1, "Básico", 20.0, ["Acceso 1 sede", "Rutinas nivel 1", "Consultas via Mail"])
    membresia2 = Membresia(2, "Medio", 50.0, ["Acceso a todas las sedes", "Rutinas nivel 1 y 2", "Acceso a 2 clases especiales por mes"])
    membresia3 = Membresia(3, "VIP", 100.0, ["Acceso a todas las sedes", "Rutinas nivel 1, 2 y 3", "Consultas via mail y llamadas virtuales", "Acceso a clases especiales en cada  sede"])

    # mostramos las membresias que creamos 
    membresia1.mostrar_membresia()
    membresia2.mostrar_membresia()
    membresia3.mostrar_membresia()

