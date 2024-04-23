import geopy.distance
import itertools
class Graph:
    def __init__(self, municipios_gdf):
        self.municipios_gdf = municipios_gdf
        self.nodos = list(self.municipios_gdf['name'])
        self.conexiones = self._construir_conexiones()

    def _construir_conexiones(self):
        conexiones = []
        for municipio1, municipio2 in itertools.combinations(self.nodos, 2):
            geom1 = self.municipios_gdf[self.municipios_gdf['name'] == municipio1].geometry.values[0]
            geom2 = self.municipios_gdf[self.municipios_gdf['name'] == municipio2].geometry.values[0]
            distancia_km = geopy.distance.distance((geom1.centroid.y, geom1.centroid.x),
                                                    (geom2.centroid.y, geom2.centroid.x)).km
            # Definir conexión si la distancia es menor que el umbral
            if distancia_km < 100:
                conexiones.append((municipio1, municipio2, {'distancia': distancia_km}))
        return conexiones
