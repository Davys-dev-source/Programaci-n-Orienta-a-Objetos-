# ============================================
# Ejemplo POO: uso de __init__ y __del__
# Todo en un solo archivo
# ============================================

class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor (__init__)
        Se ejecuta cuando se crea el objeto.
        Inicializa los atributos necesarios y abre un archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"[INIT] El archivo '{self.nombre_archivo}' fue abierto.")

    def escribir(self, texto):
        """
        Método que escribe texto dentro del archivo.
        """
        self.archivo.write(texto + "\n")
        print("[INFO] Texto escrito en el archivo.")

    def __del__(self):
        """
        Destructor (__del__)
        Se ejecuta cuando el objeto es eliminado o el programa finaliza.
        Intenta cerrar el archivo para liberar el recurso.
        Puede ejecutarse cuando:
        - se usa 'del objeto'
        - el programa termina
        - el recolector de basura elimina el objeto
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"[DEL] El archivo '{self.nombre_archivo}' fue cerrado.")


class GestorArchivos:
    """
    Clase de servicio que maneja la lógica del sistema.
    Usa la clase Archivo pero no mezcla responsabilidades.
    """

    def crear_archivo_y_escribir(self, nombre, mensaje):
        archivo = Archivo(nombre)
        archivo.escribir(mensaje)
        return archivo


# ============================================
# main (punto de entrada del programa)
# ============================================

if __name__ == "__main__":
    print("Inicio del programa")

    gestor = GestorArchivos()

    # Se crea el objeto y se ejecuta __init__
    archivo = gestor.crear_archivo_y_escribir(
        "ejemplo.txt",
        "Este es un ejemplo del uso de __init__ y __del__ en Python"
    )

    print("El programa continúa ejecutándose...")

    # Se elimina el objeto manualmente para mostrar el uso de __del__
    del archivo

    print("Fin del programa")
