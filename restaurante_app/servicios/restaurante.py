from typing import List, Optional
from restaurante_app.modelos.producto import Producto

class Restaurante:
    """Servicio encargado de administrar la lógica de negocio del catálogo de productos."""

    def __init__(self) -> None:
        self.lista_productos: List[Producto] = []

    def cargar_productos_desde_memoria(self, productos: List[Producto]) -> None:
        """Carga la lista de productos al iniciar el sistema desde el servicio de archivo."""
        self.lista_productos = productos

    def obtener_productos(self) -> List[Producto]:
        """Devuelve la lista completa de productos."""
        return self.lista_productos

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código identificador."""
        for prod in self.lista_productos:
            if prod.codigo == codigo:
                return prod
        return None

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un nuevo producto si el código no se encuentra duplicado."""
        if self.buscar_producto_por_codigo(producto.codigo) is None:
            self.lista_productos.append(producto)
            return True
        return False

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        """Actualiza los datos de un producto existente."""
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            prod.nombre = nuevo_nombre
            prod.categoria = nueva_categoria
            prod.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto del catálogo."""
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            self.lista_productos.remove(prod)
            return True
        return False