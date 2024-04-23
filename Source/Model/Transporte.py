class Transporte:
    def __init__(self, tipo):
        self.tipo = tipo

    def calcular_peso(self, distancia_km):
        if self.tipo == 'camion':
            return (35 / 100) * distancia_km
        elif self.tipo == 'lancha':
            return (3 * distancia_km)
        elif self.tipo == 'dron':
            return 500

    def obtener_tipo(self):
        return self.tipo
