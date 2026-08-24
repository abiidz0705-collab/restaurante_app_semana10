import sys
from typing import Dict, Callable
from restaurante_app.modelos.producto import Producto
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio

servicio_restaurante = Restaurante()
servicio_archivo = ArchivoServicio()

def sincronizar_json() -> None:
    """Solicita guardar el estado actual de la colección en el archivo productos.json."""
    servicio_archivo.guardar_productos(servicio_restaurante.obtener_productos())

def opcion_registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría (Entrada, Fuerte, Postre, Bebida): ").strip()
    try:
        precio = float(input("Precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        if servicio_restaurante.registrar_producto(producto):
            sincronizar_json()
            print("¡Producto guardado exitosamente en memoria y en el archivo JSON!")
        else:
            print("Error: Ya existe un producto registrado con ese código.")
    except ValueError as err:
        print(f"Error de validación: {err}")

def opcion_buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Código del producto: ").strip()
    prod = servicio_restaurante.buscar_producto_por_codigo(codigo)
    if prod:
        print("Información encontrada:", prod.mostrar_informacion())
    else:
        print("No existe ningún producto registrado con ese código.")

def opcion_actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Código del producto a modificar: ").strip()
    prod = servicio_restaurante.buscar_producto_por_codigo(codigo)
    if prod:
        print(f"Producto actual: {prod.mostrar_informacion()}")
        nuevo_nombre = input("Nuevo nombre: ").strip()
        nueva_categoria = input("Nueva categoría: ").strip()
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            if servicio_restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
                sincronizar_json()
                print("¡Producto modificado y archivo JSON actualizado correctamente!")
        except ValueError as err:
            print(f"Error de entrada: {err}")
    else:
        print("Error: Producto no encontrado.")

def opcion_eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Código del producto a eliminar: ").strip()
    if servicio_restaurante.eliminar_producto(codigo):
        sincronizar_json()
        print("¡Producto eliminado del sistema y de productos.json!")
    else:
        print("Error: No se encontró ningún producto con ese código.")

def opcion_listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    productos = servicio_restaurante.obtener_productos()
    if not productos:
        print("No hay productos en la lista actualmente.")
    else:
        for p in productos:
            print(p.mostrar_informacion())

def opcion_salir() -> None:
    print("\nSaliendo de la aplicación...")
    sys.exit()

def ejecutar() -> None:
    print("Inicializando sistema...")
    productos_guardados = servicio_archivo.cargar_productos()
    servicio_restaurante.cargar_productos_desde_memoria(productos_guardados)

    menu: Dict[str, Callable[[], None]] = {
        "1": opcion_registrar_producto,
        "2": opcion_buscar_producto,
        "3": opcion_actualizar_producto,
        "4": opcion_eliminar_producto,
        "5": opcion_listar_productos,
        "6": opcion_salir
    }

    while True:
        print("\n====================================")
        print("     SISTEMA RESTAURANTE - SEMANA 10")
        print("====================================")
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Salir")
        print("====================================")
        opcion = input("Elija una opción (1-6): ").strip()

        accion = menu.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar()