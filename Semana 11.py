import json
import os

# =====================================
# CLASE PRODUCTO
# =====================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir objeto a diccionario (para guardar en JSON)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }


# =====================================
# CLASE INVENTARIO
# =====================================
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: ID -> Producto

    # Agregar producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado correctamente.")
        else:
            print("❌ Error: Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado correctamente.")
        else:
            print("❌ Error: Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if encontrados:
            print("\n🔎 Resultados encontrados:")
            for producto in encontrados:
                self.mostrar_producto(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    # Mostrar un producto
    def mostrar_producto(self, producto):
        print("----------------------------------")
        print(f"ID: {producto.get_id()}")
        print(f"Nombre: {producto.get_nombre()}")
        print(f"Cantidad: {producto.get_cantidad()}")
        print(f"Precio: ${producto.get_precio():.2f}")
        print("----------------------------------")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 LISTA DE PRODUCTOS:")
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    # Guardar en archivo
    def guardar_en_archivo(self, archivo="inventario.json"):
        datos = {id: producto.to_dict() for id, producto in self.productos.items()}
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print("💾 Inventario guardado correctamente.")

    # Cargar desde archivo
    def cargar_desde_archivo(self, archivo="inventario.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                datos = json.load(f)
                for id_producto, info in datos.items():
                    producto = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )
                    self.productos[id_producto] = producto
            print("📂 Inventario cargado correctamente.")
        else:
            print("📂 No existe archivo previo. Se iniciará un inventario vacío.")


# =====================================
# MENÚ PRINCIPAL
# =====================================
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("""
========= SISTEMA DE INVENTARIO =========
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Guardar y salir
=========================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Error: Cantidad o precio inválidos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("❌ Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")


# Ejecutar programa
if __name__ == "__main__":
    menu()