class Plataforma: #creamos la clase Plataforma
    def __init__(self, nombre, precio): #creamos el método inicializador
        self.nombre = nombre
        self.precio = precio
    def calcular_subscripcion(self, meses): #creamos el método calcular_subscripción
        total = meses * dicc[self].precio
        return total