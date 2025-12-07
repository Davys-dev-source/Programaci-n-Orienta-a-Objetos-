# ============================================
#     SISTEMA DE RESCATE ANIMAL - POO COMPLETA
# ============================================
# Incluye:
# 1. Abstracción
# 2. Encapsulamiento
# 3. Herencia
# 4. Polimorfismo
# ============================================


# ============================================
#     CLASE BASE: Animal (ABSTRACCIÓN)
# ============================================

class Animal:
    def __init__(self, especie, edad, peso):
        # --------------------------------------------
        # ENCAPSULAMIENTO: Atributos protegidos
        # --------------------------------------------
        self._especie = especie
        self._edad = edad
        self._peso = peso

    # Método abstracto general
    def descripcion(self):
        return f"{self._especie}, {self._edad} años, {self._peso} kg"

    # Getters y setters controlados
    def get_peso(self):
        return self._peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self._peso = nuevo_peso

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad


# ============================================
#     HERENCIA: Perro y Ave
# ============================================

class Perro(Animal):
    def __init__(self, edad, peso, raza):
        super().__init__("Perro", edad, peso)
        self.raza = raza

    # POLIMORFISMO: método sobrescrito
    def descripcion(self):
        return f"Perro de raza {self.raza}, {self._edad} años, {self._peso} kg"


class Ave(Animal):
    def __init__(self, edad, peso, tipo_plumaje):
        super().__init__("Ave", edad, peso)
        self.tipo_plumaje = tipo_plumaje

    # POLIMORFISMO nuevamente aplicado
    def descripcion(self):
        return f"Ave con plumaje {self.tipo_plumaje}, {self._edad} años, {self._peso} kg"


# ============================================
#     PROGRAMA PRINCIPAL
# ============================================

p1 = Perro(5, 12.5, "Labrador")
a1 = Ave(2, 1.3, "Tropical")

# Demostración de polimorfismo
print(p1.descripcion())
print(a1.descripcion())

# Encapsulamiento: modificar valores de forma controlada
p1.set_peso(13.0)
a1.set_edad(3)

print("\nDespués de actualizar datos:")
print(p1.descripcion())
print(a1.descripcion())
