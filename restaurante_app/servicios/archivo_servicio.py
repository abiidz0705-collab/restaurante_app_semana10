import json
import os
from typing import List
from restaurante_app.modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str = os.path.join("restaurante_app", "datos", "productos.json")) -> None:
        self.ruta_archivo: str = ruta_archivo

    def cargar_productos(self) -> List[Producto]:
        """Recupera los datos del archivo JSON y devuelve una lista de objetos Producto."""
        productos_recuperados: List[Producto] = []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
                if isinstance(contenido, list):
                    for registro in contenido:
                        try:
                            prod = Producto.desde_diccionario(registro)
                            productos_recuperados.append(prod)
                        except (KeyError, ValueError) as err:
                            print(f"[Advertencia] Se omitió un registro defectuoso: {err}")
                return productos_recuperados

        except FileNotFoundError:
            print("[Aviso] No se encontró 'productos.json'. Se iniciará con una lista vacía.")
            return []
        except json.JSONDecodeError:
            print("[Error] El archivo 'productos.json' tiene un formato inválido o está dañado. Iniciando con catálogo vacío.")
            return []
        except PermissionError:
            print("[Error] Permisos insuficientes para acceder a 'productos.json'.")
            return []

    def guardar_productos(self, lista_productos: List[Producto]) -> bool:
        """Convierte los objetos Producto a diccionarios y los almacena en el archivo JSON."""
        try:
            directorio = os.path.dirname(self.ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)

            datos = [prod.a_diccionario() for prod in lista_productos]

            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
            return True

        except PermissionError:
            print("[Error] No hay permisos de escritura para actualizar 'productos.json'.")
            return False
        except Exception as e:
            print(f"[Error inesperado al guardar datos]: {e}")
            return False