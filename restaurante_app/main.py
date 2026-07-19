import sys
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_menu() -> None:
    servicio_restaurante = Restaurante()

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("----------------------------------------")
        print("4. Listar productos")
        print("5. Listar clientes")
        print("----------------------------------------")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre del plato/producto: ").strip()
            categoria = input("Categoría (ej. Entrada, Fuerte): ").strip()
            try:
                precio = float(input("Precio: "))
                nuevo_producto = Producto(codigo, nombre, categoria, precio)
                if servicio_restaurante.registrar_producto(nuevo_producto):
                    print("¡Producto registrado con éxito!")
                else:
                    print("Error: El código ya se encuentra registrado.")
            except ValueError:
                print("Error: El precio debe ser un número válido.")

        elif opcion == "2":
            print("\n--- REGISTRAR BEBIDA ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre de la bebida: ").strip()
            categoria = "Bebida"
            try:
                precio = float(input("Precio: "))
                tamano = int(input("Tamaño (en onzas): "))
                envase = input("Tipo de envase (ej. Vidrio, Lata): ").strip()
                
                nueva_bebida = Bebida(codigo, nombre, categoria, precio, tamano, envase)
                if servicio_restaurante.registrar_producto(nueva_bebida):
                    print("¡Bebida registrada con éxito!")
                else:
                    print("Error: El código ya se encuentra registrado.")
            except ValueError:
                print("Error: Verifique que los valores numéricos sean correctos.")

        elif opcion == "3":
            print("\n--- REGISTRAR CLIENTE ---")
            identificacion = input("Identificación (Cédula/RUC): ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()
            
            nuevo_cliente = Cliente(identificacion, nombre, correo)
            if servicio_restaurante.registrar_cliente(nuevo_cliente):
                print("¡Cliente registrado con éxito!")
            else:
                print("Error: La identificación ya se encuentra registrada.")

        elif opcion == "4":
            print("\n--- LISTA DE PRODUCTOS Y BEBIDAS ---")
            productos = servicio_restaurante.obtener_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for prod in productos:
                    print(prod.mostrar_informacion())

        elif opcion == "5":
            print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
            clientes = servicio_restaurante.obtener_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for clie in clientes:
                    print(clie.mostrar_informacion())

        elif opcion == "6":
            print("\n¡Hasta luego!")
            sys.exit()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_menu()