
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
    # Crear algunas membresías
    membresia1 = Membresia(1, "Básica", 20.0, ["Acceso a gimnasio", "Clases en grupo"])
    membresia2 = Membresia(2, "Premium", 50.0, ["Acceso a gimnasio", "Clases en grupo", "Entrenador personal"])
    membresia3 = Membresia(3, "VIP", 100.0, ["Acceso a gimnasio", "Clases en grupo", "Entrenador personal", "Spa"])

    # Mostrar las membresías creadas
    membresia1.mostrar_membresia()
    membresia2.mostrar_membresia()
    membresia3.mostrar_membresia()

if __name__ == "__main__":
    main()
