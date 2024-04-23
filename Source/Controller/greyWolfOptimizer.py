import random
import copy

class GreyWolfOptimizer:
    def __init__(self, graph_builder):
        self.graph_builder = graph_builder
        self.nodos, self.conexiones = self.graph_builder.construir_grafo(umbral_distancia=100)
        self.mejor_ruta = None

    def calcular_costo_ruta(self, ruta):
        costo_total = 0
        distancia_recorrida_km = 0
        transporte_actual = None
        cambios_transporte = []

        for i in range(len(ruta) - 1):
            nodo_actual = ruta[i]
            nodo_siguiente = ruta[i + 1]
            conexion = [c for c in self.conexiones if (c[0] == nodo_actual and c[1] == nodo_siguiente) or
                                                       (c[0] == nodo_siguiente and c[1] == nodo_actual)]
            if conexion:
                costo_total += conexion[0][2]['camion']  # Utilizar solo el peso del camión por ahora
                distancia_recorrida_km += conexion[0][2]['distancia']

                # Determinar el medio de transporte actual
                if transporte_actual is None:
                    transporte_actual = 'camion'
                elif conexion[0][2]['camion'] < conexion[0][2][transporte_actual]:
                    transporte_actual = 'camion'
                elif conexion[0][2]['lancha'] < conexion[0][2][transporte_actual]:
                    transporte_actual = 'lancha'
                elif conexion[0][2]['dron'] < conexion[0][2][transporte_actual]:
                    transporte_actual = 'dron'

                # Verificar si hubo cambio de transporte
                if len(cambios_transporte) == 0 or cambios_transporte[-1][1] != transporte_actual:
                    cambios_transporte.append((nodo_actual, transporte_actual))

        return costo_total, distancia_recorrida_km, cambios_transporte

    def optimizar_ruta_gwo(self, nodo_partida, nodo_llegada):
        poblacion = [[nodo_partida] + random.sample(self.nodos, len(self.nodos) - 1) for _ in range(5)]
        for iteracion in range(100):
            for lobo in poblacion:
                lobo_mejor = copy.deepcopy(lobo)
                for i in range(len(lobo)):
                    if random.random() < 0.5:
                        a = random.randint(0, len(lobo) - 1)
                        while a == i:
                            a = random.randint(0, len(lobo) - 1)
                        lobo[i], lobo[a] = lobo[a], lobo[i]
                if self.calcular_costo_ruta(lobo)[0] < self.calcular_costo_ruta(lobo_mejor)[0]:
                    lobo_mejor = copy.deepcopy(lobo)
            poblacion.append(lobo_mejor)
            poblacion = sorted(poblacion, key=lambda x: self.calcular_costo_ruta(x)[0])[:5]
        self.mejor_ruta = poblacion[0]

        # Asegurar que la ruta comience desde el nodo de partida y termine en el nodo de llegada
        if self.mejor_ruta[0] != nodo_partida:
            self.mejor_ruta.remove(nodo_partida)
            self.mejor_ruta.insert(0, nodo_partida)
        if self.mejor_ruta[-1] != nodo_llegada:
            self.mejor_ruta.remove(nodo_llegada)
            self.mejor_ruta.append(nodo_llegada)

        return self.mejor_ruta
