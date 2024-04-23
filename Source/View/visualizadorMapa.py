import matplotlib.pyplot as plt

class VisualizadorMapa:
    def __init__(self, grafo, mejor_ruta):
        self.grafo = grafo
        self.mejor_ruta = mejor_ruta

    def mostrar_mapa_todas_rutas(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        for conexion in self.grafo.conexiones:
            municipio1 = conexion[0]
            municipio2 = conexion[1]
            # Obtener coordenadas de los municipios
            geom1 = self.grafo.municipios_gdf[self.grafo.municipios_gdf['name'] == municipio1].geometry.values[0]
            geom2 = self.grafo.municipios_gdf[self.grafo.municipios_gdf['name'] == municipio2].geometry.values[0]
            x_coords = [geom1.centroid.x, geom2.centroid.x]
            y_coords = [geom1.centroid.y, geom2.centroid.y]
            ax.plot(x_coords, y_coords, 'b--', alpha=0.5)  # Línea azul para todas las conexiones
        ax.set_title("Todas las Rutas Disponibles")
        plt.show()

    def mostrar_mapa_mejor_ruta(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        for i in range(len(self.mejor_ruta) - 1):
            nodo_actual = self.mejor_ruta[i]
            nodo_siguiente = self.mejor_ruta[i + 1]
            geom1 = self.grafo.municipios_gdf[self.grafo.municipios_gdf['name'] == nodo_actual].geometry.values[0]
            geom2 = self.grafo.municipios_gdf[self.grafo.municipios_gdf['name'] == nodo_siguiente].geometry.values[0]
            x_coords = [geom1.centroid.x, geom2.centroid.x]
            y_coords = [geom1.centroid.y, geom2.centroid.y]
            ax.plot(x_coords, y_coords, 'r--', alpha=0.7)  # Línea roja para la mejor ruta
        ax.set_title("Ruta Más Óptima Encontrada")
        plt.show()
