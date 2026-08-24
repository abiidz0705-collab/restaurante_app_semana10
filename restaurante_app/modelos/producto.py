from typing import Dict, Any

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        if not codigo or not nombre or not categoria:
            raise ValueError("El código, nombre y categoría no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        return f"[{self.categoria.upper()}] Cód: {self.codigo} | {self.nombre} - Precio: ${self.precio:.2f}"

    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte el objeto Producto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def desde_diccionario(datos: Dict[str, Any]) -> "Producto":
        """Reconstruye un objeto Producto desde un diccionario."""
        try:
            return Producto(
                codigo=str(datos["codigo"]),
                nombre=str(datos["nombre"]),
                categoria=str(datos["categoria"]),
                precio=float(datos["precio"])
            )
        except KeyError as e:
            raise KeyError(f"Clave faltante en el registro JSON: {e}")
        except ValueError:
            raise ValueError("El precio registrado en el JSON no es un valor numérico válido.")