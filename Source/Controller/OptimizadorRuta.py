import random
import copy
import Transporte

class OptimizadorRuta:
    def __init__(self, grafo):
        self.grafo = grafo
        self.mejor_ruta = None
        self.mejor_costo = None

    def optimizar_ruta_gwo(self, nodo_partida, nodo_llegada):
        poblacion = [[nodo_partida] + random.sample(self.grafo.nodos, len(self.grafo.nodos) - 1) for _ in range(5)]
        for iteracion in range(100):
            for lobo in poblacion:
                lobo_mejor = copy.deepcopy(lobo)
                for i in range(len(lobo)):
                    if random.random() < 0.5:
                        a = random.randint(0, len(lobo) - 1)
                        while a == i:
                            a = random.randint(0, len(lobo) - 1)
                        lobo[i], lobo[a] = lobo[a], lobo[i]
                if self.calcular_costo_ruta(lobo) < self.calcular_costo_ruta(lobo_mejor):
                    lobo_mejor = copy.deepcopy(lobo)
            poblacion.append(lobo_mejor)
            poblacion = sorted(poblacion, key=lambda x: self.calcular_costo_ruta(x))[:5]

        self.mejor_ruta = poblacion[0]
        self.mejor_costo = self.calcular_costo_ruta(self.mejor_ruta)
        return self.mejor_ruta

def calcular_costo_ruta(self, ruta):
    costo_total = 0
    combustible_camion = 90  # Capacidad inicial de combustible en el camión
    carga_camion = 5500  # Capacidad máxima de carga en el camión
    for i in range(len(ruta) - 1):
        nodo_actual = ruta[i]
        nodo_siguiente = ruta[i + 1]
        conexion = [c for c in self.conexiones if (c[0] == nodo_actual and c[1] == nodo_siguiente) or
                                                   (c[0] == nodo_siguiente and c[1] == nodo_actual)]
        if conexion:
            distancia_km = self.calcular_distancia_entre_nodos(nodo_actual, nodo_siguiente)
            if distancia_km > 100:
                # Evaluar cambio de transporte si la distancia es mayor que 100 km
                # Ejemplo: Cambiar a lancha si la distancia es demasiado larga para el camión
                if combustible_camion < (35 / 100) * distancia_km or carga_camion < 5000:
                    costo_total += conexion[0][2]['lancha']
                else:
                    costo_total += conexion[0][2]['camion']
            else:
                costo_total += conexion[0][2]['camion']  # Usar camión por defecto para distancias cortas
    return costo_total

