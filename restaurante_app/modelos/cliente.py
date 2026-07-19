class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Contacto: {self.correo}"