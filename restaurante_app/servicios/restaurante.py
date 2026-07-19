from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self) -> None:
        self._inventario_productos: List[Producto] = []
        self._registro_clientes: List[Cliente] = []

    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        for producto in self._inventario_productos:
            if producto.codigo == nuevo_producto.codigo:
                return False
        self._inventario_productos.append(nuevo_producto)
        return True

    def registrar_cliente(self, nuevo_cliente: Cliente) -> bool:
        for cliente in self._registro_clientes:
            if cliente.identificacion == nuevo_cliente.identificacion:
                return False
        self._registro_clientes.append(nuevo_cliente)
        return True

    def obtener_productos(self) -> List[Producto]:
        return self._inventario_productos

    def obtener_clientes(self) -> List[Cliente]:
        return self._registro_clientes