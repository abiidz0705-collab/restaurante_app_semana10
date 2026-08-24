class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion or not nombre or not correo:
            raise ValueError("Todos los campos del usuario son obligatorios.")
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.nombre} | ID: {self.identificacion} | Contacto: {self.correo}"