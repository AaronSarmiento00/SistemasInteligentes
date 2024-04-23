import geopandas as gpd
import itertools
import geopy.distance

class GraphBuilder:
    def __init__(self, municipios_gdf):
        self.municipios_gdf = municipios_gdf
        self.nodos = list(self.municipios_gdf['name'])
        self.conexiones = []

    def calcular_peso_camion(self, distancia_km):
        # Cálculo del peso de la conexión para el camión
        return (35 / 100) * distancia_km

    def calcular_peso_lancha(self, distancia_km):
        # Cálculo del peso de la conexión para la lancha
        return (3 * distancia_km)  # Suponiendo una velocidad promedio en km/h

    def calcular_peso_dron(self):
        # Cálculo del peso de la conexión para el dron
        return 500

    def construir_grafo(self, umbral_distancia):
        # Calcular conexiones posibles entre municipios
        for municipio1, municipio2 in itertools.combinations(self.nodos, 2):
            geom1 = self.municipios_gdf[self.municipios_gdf['name'] == municipio1].geometry.values[0]
            geom2 = self.municipios_gdf[self.municipios_gdf['name'] == municipio2].geometry.values[0]

            # Calcular distancia entre centroides de los municipios en kilómetros
            distancia_km = geopy.distance.distance((geom1.centroid.y, geom1.centroid.x),
                                                    (geom2.centroid.y, geom2.centroid.x)).km

            # Definir conexión si la distancia es menor que el umbral
            if distancia_km < umbral_distancia:
                # Calcular peso de la conexión (considerando diferentes transportes)
                peso_camion = self.calcular_peso_camion(distancia_km)
                peso_lancha = self.calcular_peso_lancha(distancia_km)
                peso_dron = self.calcular_peso_dron()

                # Definir conexión como una tupla (municipio1, municipio2, pesos)
                self.conexiones.append((municipio1, municipio2, {
                    'camion': peso_camion,
                    'lancha': peso_lancha,
                    'dron': peso_dron,
                    'distancia': distancia_km  # Agregar distancia a los pesos
                }))

        return self.nodos, self.conexiones
