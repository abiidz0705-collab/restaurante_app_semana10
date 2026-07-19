from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano_onzas: int, tipo_envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano_onzas: int = tamano_onzas
        self.tipo_envase: str = tipo_envase

    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} (Tamaño: {self.tamano_onzas} oz | Envase: {self.tipo_envase})"