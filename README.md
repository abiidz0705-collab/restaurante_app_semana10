# Sistema de Gestión Restaurante App - Semana 10

**Estudiante:** Abigail Deleg 
**Asignatura:** Programación Orientada a Objetos  
**Repositorio:** Evolución del proyecto restaurante_app (Persistencia en JSON)  

---

## Descripción del Proyecto

Esta décima entrega representa una evolución directa del proyecto `restaurante_app`. El objetivo principal consistió en implementar la **persistencia de datos** para los productos mediante el formato **JSON**, permitiendo que la información ingresada se mantenga guardada en el disco aunque el programa se cierre por completo.

Adicionalmente, se incorporó un servicio encargado del manejo del archivo y se incluyó una captura estricta de excepciones para garantizar la estabilidad del programa frente a fallos comunes de lectura o escritura.

---

## Estructura de Componentes

```text
restaurante_app/
├── datos/
│   └── productos.json         # Almacenamiento persistente de datos
├── modelos/
│   ├── __init__.py
│   ├── bebida.py              # Clase hija de Producto
│   ├── cliente.py             # Clase de entidad Cliente
│   └── producto.py            # Entidad base con métodos to_dict y desde_diccionario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py    # Servicio que gestiona la lectura y escritura JSON
│   └── restaurante.py        # Gestión de las colecciones en memoria
├── main.py                    # Coordinador del menú e interacción por consola
└── README.md