class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio * cantidad
        else:
            print("Stock insuficiente.")
            return 0


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for p in self.productos:
            print(f"{p.nombre} - Precio: ${p.precio} - Stock: {p.stock}")

    def comprar(self, nombre, cantidad):
        for p in self.productos:
            if p.nombre == nombre:
                total = p.vender(cantidad)
                if total > 0:
                    print(f"Compra realizada. Total a pagar: ${total}")
                return
        print("Producto no encontrado.")


# Uso del programa
tienda = Tienda("Tienda Online")
tienda.agregar_producto(Producto("Laptop", 800, 5))
tienda.agregar_producto(Producto("Mouse", 15, 20))

tienda.mostrar_productos()
tienda.comprar("Mouse", 3)
tienda.mostrar_productos()
